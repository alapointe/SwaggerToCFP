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
        def collect_all_attributes(datagroup_name, model, visited=None):
            """Collecte récursivement tous les attributs d'un datagroup, y compris ceux des objets référencés"""
            if visited is None:
                visited = set()
            if datagroup_name in visited or datagroup_name not in model:
                return set()
            visited.add(datagroup_name)
            
            attributes = set()
            group = model[datagroup_name]
            
            if isinstance(group, dict):
                # Ajoute tous les attributs directs
                attributes.update(group.keys())
                
                # Explore les références et héritages
                for key, val in group.items():
                    if isinstance(val, dict):
                        # Référence directe
                        if 'ref' in val:
                            attributes.update(collect_all_attributes(val['ref'], model, visited))
                        # Héritage allOf
                        if 'allOf_refs' in val:
                            for refd in val['allOf_refs']:
                                if 'ref' in refd:
                                    attributes.update(collect_all_attributes(refd['ref'], model, visited))
                        # Arrays d'objets référencés
                        if val.get('type') == 'array' and 'items' in val:
                            items = val['items']
                            if isinstance(items, dict) and 'ref' in items:
                                attributes.update(collect_all_attributes(items['ref'], model, visited))
                
                # Gestion spécifique des allOf_refs au niveau racine
                if 'allOf_refs' in group:
                    for allof in group['allOf_refs']:
                        if 'ref' in allof:
                            attributes.update(collect_all_attributes(allof['ref'], model, visited))
                            
            elif isinstance(group, list):
                attributes.update(group)
                
            return attributes

        parameters_datagroups = {}
        
        for fpid, param_info in parameters.items():
            datagroups_rb = set()
            if fpid in request_body and 'Datagroups' in request_body[fpid]:
                datagroups_rb = set(request_body[fpid]['Datagroups'])
            
            params_in_rb = set()
            for dg in datagroups_rb:
                params_in_rb.update(collect_all_attributes(dg, data_model))
            
            datagroups_param = []
            for param in param_info['parameters']:
                if param in params_in_rb:
                    continue
                    
                for datagroup_name in data_model.keys():
                    if datagroup_name in datagroups_rb:
                        continue
                        
                    all_attributes = collect_all_attributes(datagroup_name, data_model)
                    
                    if param in all_attributes and datagroup_name not in datagroups_param:
                        datagroups_param.append(datagroup_name)
                        break
            
            parameters_datagroups[fpid] = datagroups_param
        
        return parameters_datagroups

    def identify_datagroups_per_fp(self, data_model) -> dict:
        return data_model
    
    def get_request_body_datagroups(self, request_body, **kwargs):
        return request_body
    
    @classmethod
    def collect_all_refs(self, type_name, model, found=None):
        if found is None:
            found = set()
        if type_name not in model or type_name in found:
            return found
        
        found.add(type_name)
        props = model[type_name]
        
        # Gestion allOf_refs (héritage)
        if 'allOf_refs' in props:
            for bloc in props['allOf_refs']:
                ref = bloc.get('ref')
                if ref:
                    self.collect_all_refs(ref, model, found)
        
        # Parcours TOUTES les propriétés de façon récursive
        def traverse_properties(properties_dict):
            for prop_name, prop_def in properties_dict.items():
                if isinstance(prop_def, dict):
                    # Référence directe
                    if prop_def.get('ref'):
                        self.collect_all_refs(prop_def['ref'], model, found)
                    # Objet imbriqué avec propriétés
                    elif prop_def.get('type') == 'object':
                        if 'ref' in prop_def:
                            self.collect_all_refs(prop_def['ref'], model, found)
                        elif 'properties' in prop_def:
                            # Descend récursivement dans les propriétés imbriquées
                            traverse_properties(prop_def['properties'])
                    # Tableau d'objets
                    elif prop_def.get('type') == 'array' and 'items' in prop_def:
                        items = prop_def['items']
                        if isinstance(items, dict):
                            if items.get('ref'):
                                self.collect_all_refs(items['ref'], model, found)
                            elif items.get('type') == 'object':
                                if 'ref' in items:
                                    self.collect_all_refs(items['ref'], model, found)
                                elif 'properties' in items:
                                    # Descend récursivement dans les propriétés des items
                                    traverse_properties(items['properties'])
        
        traverse_properties(props)
        return found

    @classmethod
    def get_responses_datagroups(self, extracted_responses, data_model, response_data_model):
        # Si le data_model semble être des réponses d'API, on utilise les schémas OpenAPI
        if any(key for key in data_model.keys() if '.' in key and any(c.isdigit() for c in key)):
            # Récupère les schémas OpenAPI et les convertit
            openapi_schemas = self.extractor.get_schema()
            actual_data_model = self.convert_openapi_to_data_model(openapi_schemas)
        else:
            # Utilise le data_model fourni
            actual_data_model = data_model
        
        def collect_all_refs(type_name, model, found=None):
            if found is None:
                found = set()
            if type_name not in model or type_name in found:
                return found
            
            found.add(type_name)
            props = model[type_name]
            
            # Gestion allOf_refs (héritage)
            if 'allOf_refs' in props:
                for bloc in props['allOf_refs']:
                    ref = bloc.get('ref')
                    if ref:
                        collect_all_refs(ref, model, found)
            
            # Parcours TOUTES les propriétés de façon récursive
            def traverse_properties(properties_dict):
                if isinstance(properties_dict, list):
                    # Pour une liste, pas de propriétés imbriquées à traverser
                    return
                for prop_name, prop_def in properties_dict.items():
                    if isinstance(prop_def, dict):
                        # Référence directe
                        if prop_def.get('ref'):
                            collect_all_refs(prop_def['ref'], model, found)
                        # Objet imbriqué avec propriétés
                        elif prop_def.get('type') == 'object':
                            if 'ref' in prop_def:
                                collect_all_refs(prop_def['ref'], model, found)
                            elif 'properties' in prop_def:
                                # Descend récursivement dans les propriétés imbriquées
                                traverse_properties(prop_def['properties'])
                        # Tableau d'objets
                        elif prop_def.get('type') == 'array' and 'items' in prop_def:
                            items = prop_def['items']
                            if isinstance(items, dict):
                                if items.get('ref'):
                                    collect_all_refs(items['ref'], model, found)
                                elif items.get('type') == 'object':
                                    if 'ref' in items:
                                        collect_all_refs(items['ref'], model, found)
                                    elif 'properties' in items:
                                        # Descend récursivement dans les propriétés des items
                                        traverse_properties(items['properties'])
            
            traverse_properties(props)
            return found

        def resolve_response_ref(ref_path):
            """Résout une référence de type '#/components/responses/BadRequest'"""
            if '#/components/responses/' in ref_path:
                response_name = ref_path.split('/')[-1]
                if response_name in response_data_model:
                    response_def = response_data_model[response_name]
                    # Extrait les schémas de cette réponse
                    refs = set()
                    if 'content' in response_def:
                        for mime_def in response_def['content'].values():
                            schema = mime_def.get('schema')
                            if schema and '$ref' in schema:
                                schema_name = schema['$ref'].split('/')[-1]
                                if schema_name in actual_data_model:
                                    refs.update(collect_all_refs(schema_name, actual_data_model))
                    return refs
            return set()
        
        responses_datagroups = {}
        for process_id, response in extracted_responses.items():
            refs = set()
            
            for rep_code, rep_def in response.items():
                # Gestion des références vers components/responses
                if isinstance(rep_def, dict) and '$ref' in rep_def:
                    # Ex: '$ref': '#/components/responses/BadRequest'
                    refs.update(resolve_response_ref(rep_def['$ref']))
                # Content avec schéma
                elif isinstance(rep_def, dict) and 'content' in rep_def:
                    for mime_def in rep_def['content'].values():
                        schema = mime_def.get('schema')
                        if schema:
                            # $ref direct
                            if '$ref' in schema:
                                type_name = schema['$ref'].split('/')[-1]
                                if type_name in actual_data_model:
                                    refs.update(collect_all_refs(type_name, actual_data_model))
                            # Array d'objets
                            elif schema.get('type') == 'array' and 'items' in schema:
                                items = schema['items']
                                if '$ref' in items:
                                    type_name = items['$ref'].split('/')[-1]
                                    if type_name in actual_data_model:
                                        refs.update(collect_all_refs(type_name, actual_data_model))
            
            responses_datagroups[process_id] = sorted(refs)
        
        return responses_datagroups
   
    # def get_responses_datagroups(self, extracted_responses, data_model, response_data_model):
    #     responses_datagroups = {}
    #     for process_id, response in extracted_responses.items():
    #         all_refs = set()
    #         for rep_code, rep_def in response.items():
    #             # Il faut aller trouver tous les schémas $ref et les tableaux d'items
    #             if isinstance(rep_def, dict) and "content" in rep_def:
    #                 for mime, mime_def in rep_def["content"].items():
    #                     schema = mime_def.get("schema")
    #                     if schema:
    #                         # Cas $ref direct
    #                         if "$ref" in schema:
    #                             obj = schema["$ref"].split("/")[-1]
    #                             all_refs.update(self.get_nested_objects(obj, data_model))
    #                         # Cas tableau d'objets
    #                         elif schema.get("type") == "array" and "items" in schema:
    #                             items = schema["items"]
    #                             if "$ref" in items:
    #                                 obj = items["$ref"].split("/")[-1]
    #                                 all_refs.update(self.get_nested_objects(obj, data_model))
    #             # Support pour schéma unique sous rep_def (rare)
    #             elif isinstance(rep_def, dict) and "$ref" in rep_def:
    #                 obj = rep_def["$ref"].split("/")[-1]
    #                 all_refs.update(self.get_nested_objects(obj, data_model))

    #         responses_datagroups[process_id] = sorted(all_refs)
    #     return responses_datagroups 

    @classmethod
    def dict_in_data_model(self, data_model, dict_name):
        return dict_name in data_model

    def get_ref_from_prop(prop_def):
        """Retourne la référence d'une propriété si présente."""
        if prop_def.get('ref'):
            return prop_def['ref']
        if prop_def.get('$ref'):
            return prop_def['$ref'].split('/')[-1]
        return None
        
    @classmethod
    def get_nested_objects(self, obj, data_model, visited=None):
        if visited is None:
            visited = set()
        if obj in visited:
            return set()
        visited.add(obj)
        refs = set()
        refs.add(obj)
        model_def = data_model.get(obj, {})
        # Gestion "allOf_refs" (composite/héritage)
        if 'allOf_refs' in model_def:
            for bloc in model_def['allOf_refs']:
                ref = bloc.get('ref')
                if ref:
                    refs.update(self.get_nested_objects(ref, data_model, visited))
        # Parcours propriétés
        for prop_name, prop_def in model_def.items():
            if isinstance(prop_def, dict):
                # Cas objet $ref
                if prop_def.get('ref'):
                    refs.update(self.get_nested_objects(prop_def['ref'], data_model, visited))
                # Cas array imbriqué
                if prop_def.get('type') == 'array' and 'items' in prop_def:
                    items = prop_def['items']
                    if isinstance(items, dict) and items.get('ref'):
                        refs.update(self.get_nested_objects(items['ref'], data_model, visited))
        return refs
    # def get_nested_objects(self, content, data_model):
    #     nested = set()
    #     nested.add(content)
    #     def find_refs(properties):
    #         refs = set()
    #         if isinstance(properties, list):
    #             for item in properties:
    #                 if isinstance(item, dict):
    #                     refs.update(find_refs(item))
    #         elif isinstance(properties, dict):
    #             for prop in properties.values():
    #                 if isinstance(prop, list):
    #                     refs.update(find_refs(prop))
    #                 elif isinstance(prop, dict):
    #                     if prop.get('type') == 'object' and 'ref' in prop:
    #                         refs.add(prop['ref'])
    #                     elif prop.get('type') == 'array':
    #                         items = prop.get('items', {})
    #                         # Correction : si les items référencent un objet, il faut le chercher
    #                         if isinstance(items, dict) and items.get('type') == 'object' and 'ref' in items:
    #                             refs.add(items['ref'])
    #                         # Recur dans les items aussi au cas où
    #                         refs.update(find_refs(items))
    #         return refs

    #     model_props = data_model.get(content, {})
    #     refs = find_refs(model_props)
    #     for ref in refs:
    #         if ref not in nested:
    #             nested.update(self.get_nested_objects(ref, data_model))
    #     return sorted(nested)

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