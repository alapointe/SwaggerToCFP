from lib.openapi3.openapi3 import OpenAPI
import src.extraction.Extractor as ext
from utils.functional_process_id_generator import Utils as fpig

class DataGroupExtractor():

    def __init__(self, spec) -> None:
        self.spec = spec

    def get_parameters(self) -> dict:
        """
            In OpenAPI 3.0, parameters are defined in the parameters section of an operation or path. 
            To describe a parameter, you specify its name, location (in), data type (defined by either schema or content) and other attributes, such as description or required.
            OpenAPI 3.0 distinguishes between the following parameter types based on the parameter location. The location is determined by the parameter’s in key, for example, in: query or in: path.

                - path parameters, such as /users/{id}
                - query parameters, such as /users?role=admin
                - header parameters, such as X-MyHeader: Value
                - cookie parameters, which are passed in the Cookie header, such as Cookie: debug=0; csrftoken=BUSe35dohU3O1MZvDCU
            https://swagger.io/docs/specification/describing-parameters/

            In the context of this project, all parameters will be returned.

        """
        paths = self.spec.get_paths()
        parameters = {}
        for path, http_method in paths.items():
            for http_method, http_method_dict in http_method.items():
                fpid = fpig.generate_fpid(path, http_method, http_method_dict)
                params = []
                if 'parameters' in http_method_dict:
                    if http_method_dict["parameters"] == []:
                        parameters.update({fpid: {"summary" : fpid, "parameters": []}})
                    else:
                        for param_name in http_method_dict["parameters"]:
                            if "name" in param_name: 
                                params.append(param_name["name"])
                                params = list(set(params))
                                parameters.update({fpid: {"summary" : fpid, "parameters": params}})
                else:
                    parameters.update({fpid: {"summary" : fpid, "parameters": params}})
        return parameters
    
    def get_data_model(self, openapi_schemas):
        """
        Convertit les schémas OpenAPI complexes au format data_model
        Gère allOf, propriétés imbriquées, et références multiples
        """
        data_model = {}
        
        def convert_property(prop_def):
            """Convertit une propriété OpenAPI en format data_model"""
            if '$ref' in prop_def:
                # Référence directe à un autre schéma
                ref_name = prop_def['$ref'].split('/')[-1]
                return {'type': 'object', 'ref': ref_name}
            elif prop_def.get('type') == 'object' and 'properties' in prop_def:
                # Objet imbriqué avec propriétés
                nested_props = {}
                for nested_name, nested_def in prop_def['properties'].items():
                    nested_props[nested_name] = convert_property(nested_def)
                return {'type': 'object', 'properties': nested_props}
            elif prop_def.get('type') == 'array' and 'items' in prop_def:
                # Tableau
                items = prop_def['items']
                if '$ref' in items:
                    # Tableau d'objets référencés
                    ref_name = items['$ref'].split('/')[-1]
                    return {'type': 'array', 'items': {'type': 'object', 'ref': ref_name}}
                elif items.get('type') == 'object' and 'properties' in items:
                    # Tableau d'objets avec propriétés définies
                    item_props = {}
                    for item_prop_name, item_prop_def in items['properties'].items():
                        item_props[item_prop_name] = convert_property(item_prop_def)
                    return {'type': 'array', 'items': {'type': 'object', 'properties': item_props}}
                else:
                    # Tableau de primitives
                    return {'type': 'array', 'items': {'type': 'properties'}}
            else:
                # Type primitif (string, integer, boolean, etc.)
                return {'type': 'properties'}
        
        def process_schema(schema_name, schema_def, processed=None):
            """Traite un schéma et ses dépendances récursivement"""
            if processed is None:
                processed = set()
            if schema_name in processed or schema_name in data_model:
                return
            processed.add(schema_name)
            
            properties = {}
            
            # Gestion des allOf (héritage)
            if 'allOf' in schema_def:
                allof_refs = []
                for bloc in schema_def['allOf']:
                    if '$ref' in bloc:
                        # Référence à un parent
                        ref_name = bloc['$ref'].split('/')[-1]
                        allof_refs.append({'type': 'object', 'ref': ref_name})
                        # Traite récursivement le parent
                        if ref_name in openapi_schemas:
                            process_schema(ref_name, openapi_schemas[ref_name], processed)
                    elif 'properties' in bloc:
                        # Propriétés définies directement dans le bloc allOf
                        for prop_name, prop_def in bloc['properties'].items():
                            properties[prop_name] = convert_property(prop_def)
                            # Si c'est une référence, traite l'objet référencé
                            if '$ref' in prop_def:
                                ref_name = prop_def['$ref'].split('/')[-1]
                                if ref_name in openapi_schemas:
                                    process_schema(ref_name, openapi_schemas[ref_name], processed)
                
                if allof_refs:
                    properties['allOf_refs'] = allof_refs
            
            # Propriétés directes du schéma
            if 'properties' in schema_def:
                for prop_name, prop_def in schema_def['properties'].items():
                    properties[prop_name] = convert_property(prop_def)
                    # Si c'est une référence, traite l'objet référencé
                    if '$ref' in prop_def:
                        ref_name = prop_def['$ref'].split('/')[-1]
                        if ref_name in openapi_schemas:
                            process_schema(ref_name, openapi_schemas[ref_name], processed)
                    # Si c'est un objet imbriqué avec des références
                    elif prop_def.get('type') == 'object' and 'properties' in prop_def:
                        for nested_name, nested_def in prop_def['properties'].items():
                            if '$ref' in nested_def:
                                nested_ref = nested_def['$ref'].split('/')[-1]
                                if nested_ref in openapi_schemas:
                                    process_schema(nested_ref, openapi_schemas[nested_ref], processed)
                    # Si c'est un tableau avec des références
                    elif prop_def.get('type') == 'array' and 'items' in prop_def:
                        items = prop_def['items']
                        if '$ref' in items:
                            items_ref = items['$ref'].split('/')[-1]
                            if items_ref in openapi_schemas:
                                process_schema(items_ref, openapi_schemas[items_ref], processed)
            
            data_model[schema_name] = properties
        
        # Traite tous les schémas
        for schema_name, schema_def in openapi_schemas.items():
            process_schema(schema_name, schema_def)
        
        return data_model

    def get_responses_data_model(self) -> dict:
        return self.spec.get_responses()

    def get_content_objects_per_fp(self):
        # Getting all $ref recursilvely from path
        paths = self.spec.get_paths()
        result = {}

        if paths is None:
            return result
        
        for path, http_method in paths.items():
            for http_method, http_method_dict in http_method.items():
                fpid = fpig.generate_fpid(path, http_method, http_method_dict)

                refs = self.extract_refs_per_fp(http_method_dict, [http_method], fpid)
                result.update(refs)
                # print(result)
        return result

    def extract_refs_per_fp(self, data, current_path, fpid, result = None):
        """Extrait récursivement les valeurs $ref d'un dictionnaire YAML.

        Args:
            data: Le dictionnaire YAML à analyser.
            current_path: Le chemin actuel dans le dictionnaire (utilisé pour la récursivité).
            result: Le dictionnaire de résultats accumulé (utilisé pour la récursivité).

        Returns:
            Un dictionnaire où les clés sont les noms des opérations et les valeurs sont les dictionnaires de références.
        """
        counter = 0
        if data is None:
            data = self.spec.get_paths()
        

        if result is None:
            result = {}

        if current_path is None:
            current_path = []  # Chemin vide au début
        
        for key, value in data.items():
            refs = []
            new_path = current_path + [key]
            if isinstance(value, dict):
                
                if "$ref" in value:
                    if fpid not in result:
                        result[fpid] = {}
                    result[fpid][value["$ref"].split("/")[-1]] = []  # Nom du schéma référencé
                    
                else:
                    self.extract_refs_per_fp(value, new_path, fpid, result)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.extract_refs_per_fp(item, new_path, fpid, result)
        return result
    
    def get_request_body(self, data_model) -> dict:
        paths = self.spec.get_paths()
        result = {}

        if paths is None:
            return result
        
        for path, http_method in paths.items():
            for http_method, http_method_dict in http_method.items():
                fpid = fpig.generate_fpid(path, http_method, http_method_dict)
                if 'requestBody' in http_method_dict:
                    content =   self.extract_ref(http_method_dict['requestBody']['content'])
                    result.update({fpid : {'Datagroups' : self.get_nested_objects(content, data_model)}})

                else:
                    result.update({ fpid : {}})
        return result

    def get_nested_objects(self, content, data_model):
        nested = set()
        nested.add(content)

        def find_refs(properties):
            refs = set()
            for prop_value in properties.values():
                if isinstance(prop_value, dict):
                    # Référence directe (type: object + ref)
                    if prop_value.get('type') == 'object' and 'ref' in prop_value:
                        refs.add(prop_value['ref'])
                    # Tableau d'objets référencés
                    elif prop_value.get('type') == 'array':
                        items = prop_value.get('items', {})
                        if items.get('type') == 'object' and 'ref' in items:
                            refs.add(items['ref'])
                    # allOf imbriqué dans la propriété (pas usuel ici, mais inclus par robustesse)
                    if 'allOf' in prop_value:
                        for allof in prop_value['allOf']:
                            if 'ref' in allof:
                                refs.add(allof['ref'])
                            elif isinstance(allof, dict) and 'properties' in allof:
                                refs.update(find_refs(allof['properties']))
            return refs

        # Gestion spéciale du format data_model avec clé 'allOf_refs'
        model_props = data_model.get(content, {})


        refs = set()
        # Ajout des références listées dans 'allOf_refs' s'il y en a
        if isinstance(model_props, dict):
            if 'allOf_refs' in model_props:
                for refdict in model_props['allOf_refs']:
                    if isinstance(refdict, dict) and 'ref' in refdict:
                        refs.add(refdict['ref'])
            # Cherche aussi "classiquement" (propriétés, array, allOf imbriqué)
            props_copy = model_props.copy()
            props_copy.pop('allOf_refs', None)
            refs.update(find_refs(props_copy))

        # Parcours récursif des références trouvées
        for ref in refs:
            if ref not in nested:
                nested.add(ref)
                nested.update(self.get_nested_objects(ref, data_model))

        return sorted(nested)

    def get_responses(self) -> dict:
        paths = self.spec.get_paths()
        # print(paths)
        # component_responses = self.extractor.get_responses()
        responses = {}

        if paths is None:
            return responses
        
        for path, http_method in paths.items():
            for http_method, http_method_dict in http_method.items():
                fpid = fpig.generate_fpid(path, http_method, http_method_dict)
                if 'responses' in http_method_dict:
                    responses.update({ fpid : http_method_dict['responses']})
                else:
                    responses.update({ fpid : {}})
        # print('responses')
        # print(responses)
        return responses

    def get_http_status_codes(self) -> dict:
        return self.get_responses()

    def extract_ref(self, data):
        # Parcourt tous les types de contenu (application/json, etc.)
        for content_type, media_type in data.items():
            schema = media_type.get('schema', {})
            
            # Cas 1 : Référence directe dans le schéma
            ref = schema.get('$ref')
            if ref:
                return ref.split('/')[-1]
            
            # Cas 2 : Référence dans les items d'un tableau
            items = schema.get('items', {})
            ref = items.get('$ref')
            if ref:
                return ref.split('/')[-1]
        
        # Aucune référence trouvée → retourne 'UNKNOWN'
        return "UNKNOWN"