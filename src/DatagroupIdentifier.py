from utils.functional_process_id_generator import Utils

class DataGroupIdentifier():

    # def __init__(self) -> None:
    #     pass

    def identify_datagroups(self, data_model) -> dict:
        """
            Simplistic approach: All keys in data_model are datagroups and all values are attributes

            Eventually, should remove technical datagroups such as horodateurs, ProblemeREST, codeUsagerCreation, etc.

            Morevoer, should compare with internal dictionnary of business objects.
        """

        return data_model

    def get_parameters_datagroups(self, data_model, parameters, request_body) -> dict:
        parameters_datagroups = {}
        for fpid, param_info in parameters.items():
            # 1. Récupérer tous les datagroups du request body pour cette opération
            datagroups_rb = set()
            if fpid in request_body and 'Datagroups' in request_body[fpid]:
                datagroups_rb = set(request_body[fpid]['Datagroups'])
            # 2. Collecter tous les attributs de ces datagroups, y compris attributs "nested"
            params_in_rb = set()
            stack = list(datagroups_rb)
            seen = set()
            while stack:
                dg = stack.pop()
                if dg in seen or dg not in data_model:
                    continue
                seen.add(dg)
                group = data_model[dg]
                # cas dict : attributs + découverte de sous-objets (par ref ou allOf)
                if isinstance(group, dict):
                    for key, val in group.items():
                        params_in_rb.add(key)
                        # ref "classique"
                        if isinstance(val, dict) and 'ref' in val and val['ref'] not in seen:
                            stack.append(val['ref'])
                        # allOf
                        if isinstance(val, dict) and 'allOf_refs' in val:
                            for refd in val['allOf_refs']:
                                if 'ref' in refd and refd['ref'] not in seen:
                                    stack.append(refd['ref'])
                elif isinstance(group, list):
                    params_in_rb.update(group)
            # 3. Logique principale "flat" ensuite
            datagroups_param = []
            for param in param_info['parameters']:
                if param in params_in_rb:
                    continue
                for datagroup, attributes in data_model.items():
                    attrs = attributes.keys() if isinstance(attributes, dict) else attributes
                    if param in attrs and datagroup not in datagroups_rb and datagroup not in datagroups_param:
                        datagroups_param.append(datagroup)
                        break  # Premier datagroup éligible
            parameters_datagroups[fpid] = datagroups_param
        return parameters_datagroups

    def identify_datagroups_per_fp(self, data_model) -> dict:
        return data_model
    
    def get_request_body_datagroups(self, request_body, **kwargs):
        return request_body
    
    def get_responses_datagroups(self, extracted_responses, data_model, response_data_model):
        responses_datagroups = {}
        for process_id, response in extracted_responses.items():
            all_refs = set()
            for rep_code, rep_def in response.items():
                # Il faut aller trouver tous les schémas $ref et les tableaux d'items
                if isinstance(rep_def, dict) and "content" in rep_def:
                    for mime, mime_def in rep_def["content"].items():
                        schema = mime_def.get("schema")
                        if schema:
                            # Cas $ref direct
                            if "$ref" in schema:
                                obj = schema["$ref"].split("/")[-1]
                                all_refs.update(self.get_nested_objects(obj, data_model))
                            # Cas tableau d'objets
                            elif schema.get("type") == "array" and "items" in schema:
                                items = schema["items"]
                                if "$ref" in items:
                                    obj = items["$ref"].split("/")[-1]
                                    all_refs.update(self.get_nested_objects(obj, data_model))
                # Support pour schéma unique sous rep_def (rare)
                elif isinstance(rep_def, dict) and "$ref" in rep_def:
                    obj = rep_def["$ref"].split("/")[-1]
                    all_refs.update(self.get_nested_objects(obj, data_model))

            responses_datagroups[process_id] = sorted(all_refs)
        return responses_datagroups 

    @classmethod
    def dict_in_data_model(self, data_model, dict_name):
        return dict_name in data_model

    @classmethod
    def get_nested_array_objects(self, obj_name, data_model):
        if obj_name not in data_model:
            return set()
        result = set([obj_name])
        def collect_array_refs(name, visited=None):
            if visited is None:
                visited = set()
            if name in visited or name not in data_model:
                return set()
            visited.add(name)
            refs = set()
            obj_def = data_model[name]
            # Propriétés de type array
            if isinstance(obj_def, dict):
                for prop, val in obj_def.items():
                    if isinstance(val, dict) and val.get("type") == "array":
                        items = val.get("items", {})
                        if isinstance(items, dict) and items.get("type") == "object" and "ref" in items:
                            ref = items["ref"]
                            refs.add(ref)
                            refs.update(collect_array_refs(ref, visited))
            # Héritage via allOf_refs
            if isinstance(obj_def, dict) and "allOf_refs" in obj_def and isinstance(obj_def["allOf_refs"], list):
                for ref_info in obj_def["allOf_refs"]:
                    if isinstance(ref_info, dict):
                        parent = ref_info.get("ref")
                        if parent:
                            # On recherche les arrays du parent uniquement, le parent lui-même non (sauf si racine)
                            refs.update(collect_array_refs(parent, visited))
            return refs
        result.update(collect_array_refs(obj_name))
        return sorted(result)
        
    @classmethod
    def get_nested_objects(self, content, data_model):
        nested = set()
        nested.add(content)
        def find_refs(properties):
            refs = set()
            if isinstance(properties, list):
                for item in properties:
                    if isinstance(item, dict):
                        refs.update(find_refs(item))
            elif isinstance(properties, dict):
                for prop in properties.values():
                    if isinstance(prop, list):
                        refs.update(find_refs(prop))
                    elif isinstance(prop, dict):
                        if prop.get('type') == 'object' and 'ref' in prop:
                            refs.add(prop['ref'])
                        elif prop.get('type') == 'array':
                            items = prop.get('items', {})
                            # Correction : si les items référencent un objet, il faut le chercher
                            if isinstance(items, dict) and items.get('type') == 'object' and 'ref' in items:
                                refs.add(items['ref'])
                            # Recur dans les items aussi au cas où
                            refs.update(find_refs(items))
            return refs

        model_props = data_model.get(content, {})
        refs = find_refs(model_props)
        for ref in refs:
            if ref not in nested:
                nested.update(self.get_nested_objects(ref, data_model))
        return sorted(nested)

    @classmethod
    def get_nested_responses(self, content, data_model, responses_data_model):
        def _find_ref(schema):
            # Cherche la référence dans un schéma
            if "$ref" in schema:
                ref = schema["$ref"].split('/')[-1]
                return ref
            return None

        found = []

        # 1. On récupère la référence du schema dans la réponse (ex: 'ProblemeRest')
        response = responses_data_model.get(content)
        if not response:
            return []

        schema = (
            response
            .get("content", {})
            .get("application/json", {})
            .get("schema", {})
        )
        first_ref = _find_ref(schema)
        if not first_ref:
            return []

        def _traverse(ref):
            if ref not in found:
                found.append(ref)
                if ref in data_model:
                    for prop in data_model[ref]:
                        # Cas propriété (objet natif ou $ref)
                        prop_data = data_model[ref][prop]
                        if isinstance(prop_data, dict):
                            if "ref" in prop_data:
                                nested_ref = prop_data["ref"]
                                _traverse(nested_ref)
                            if "$ref" in prop_data:
                                nested_ref = prop_data["$ref"].split('/')[-1]
                                _traverse(nested_ref)
                            # Recherche dans les array/items imbriqués
                            if "items" in prop_data:
                                items_data = prop_data["items"]
                                if "ref" in items_data:
                                    nested_ref = items_data["ref"]
                                    _traverse(nested_ref)
                                if "$ref" in items_data:
                                    nested_ref = items_data["$ref"].split('/')[-1]
                                    _traverse(nested_ref)

        _traverse(first_ref)
        return found

    def get_http_status_datagroups(self, extracted_responses):
        return extracted_responses
    
    @classmethod
    def extract_ref(self, data):
        if isinstance(data, dict):
            if '$ref' in data:
                return data['$ref'].split('/')[-1]  # Extract last word after '/'
            else:
                for value in data.values():
                    result = self.extract_ref(value)
                    if result:
                        return result
        elif isinstance(data, list):    
            for item in data:
                result = self.extract_ref(item)
                if result:
                    return result
        return None 

    @staticmethod
    def validate_schema(data, data_model):
        """
        Vérifie si `data` correspond à l'un des schémas définis dans `data_model`.
        Retourne une liste des schémas utilisés ou, en cas d'erreur,
        [].
        """

        # Cas trivial : erreur de type (par exemple string au lieu de dict)
        if not isinstance(data, dict):
            return []

        matched_schemas = []
        for schema_name, schema_def in data_model.items():
            # Les schémas "vides" (ex: ProjetRetraite: {}) ne sont pas validables
            if not schema_def:
                continue

            # Vérifier que toutes les clés de schema_def soient dans data
            if all(
                field in data
                for field in schema_def.keys()
            ):
                matched_schemas.append(schema_name)

        # Si rien n'a matché, on renvoie l’erreur générique
        if not matched_schemas:
            return []

        return matched_schemas