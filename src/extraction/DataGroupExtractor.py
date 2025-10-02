from lib.openapi3.openapi3 import OpenAPI
import src.extraction.Extractor as ext
from utils.functional_process_id_generator import Utils as fpig

class DataGroupExtractor():

    def __init__(self, extractor) -> None:
        self.extractor = extractor

    # TODO Could be simplified by retrurning only a dict of fpid with associated parameters
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
        paths = self.extractor.get_paths()
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
                            if "name" in param_name: # TODO Crash si le champ name est absent, l'ajout du if est une patch temporaire
                                params.append(param_name["name"])
                                params = list(set(params))
                                parameters.update({fpid: {"summary" : fpid, "parameters": params}})
                else:
                    parameters.update({fpid: {"summary" : fpid, "parameters": params}})
        return parameters
    
    # TODO Refactor if necessecary
    # def get_properties(self) -> list:
    #     schema = self.extractor.get_schema()
    #     if "properties" not in schema:
    #         return []  # No properties found

    #     return list(schema["properties"].keys())
    """
            expected_data_model_2 = {
                "Order": {
                    "id": {"type": "properties"},
                    "petId": {"type": "properties"},
                    "quantity": {"type": "properties"},
                    "shipDate": {"type": "properties"},
                    "status": {"type": "properties"},
                    "complete": {"type": "properties"}
                },
                "Category": {
                    "id": {"type": "properties"},
                    "name": {"type": "properties"}
                },
                "User": {
                    "id": {"type": "properties"},
                    "username": {"type": "properties"},
                    "firstName": {"type": "properties"},
                    "lastName": {"type": "properties"},
                    "email": {"type": "properties"},
                    "password": {"type": "properties"},
                    "phone": {"type": "properties"},
                    "userStatus": {"type": "properties"}
                },
                "Tag": {
                    "id": {"type": "properties"},
                    "name": {"type": "properties"}
                },
                "Pet": {
                    "id": {"type": "properties"},
                    "name": {"type": "properties"},
                    "category": {"type": "object", "ref": "Category"},
                    "photoUrls": {"type": "array", "items": {"type": "properties"}},
                    "tags": {"type": "array", "items": {"type": "object", "ref": "Tag"}},
                    "status": {"type": "properties"}
                },
                "ApiResponse": {
                    "code": {"type": "properties"},
                    "type": {"type": "properties"},
                    "message": {"type": "properties"}
                },
                "Error": {
                    "code": {"type": "properties"},
                    "message": {"type": "properties"}
                }
            }

        schema = {
            'Order': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'petId': {'type': 'integer', 'format': 'int64', 'example': 198772}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 7}, 'shipDate': {'type': 'string', 'format': 'date-time'}, 'status': {'type': 'string', 'description': 'Order Status', 'example': 'approved', 'enum': ['placed', 'approved', 'delivered']}, 'complete': {'type': 'boolean'}}, 'xml': {'name': 'order'}}, 'Category': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 1}, 'name': {'type': 'string', 'example': 'Dogs'}}, 'xml': {'name': 'category'}}, 'User': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'username': {'type': 'string', 'example': 'theUser'}, 'firstName': {'type': 'string', 'example': 'John'}, 'lastName': {'type': 'string', 'example': 'James'}, 'email': {'type': 'string', 'example': 'john@email.com'}, 'password': {'type': 'string', 'example': '12345'}, 'phone': {'type': 'string', 'example': '12345'}, 'userStatus': {'type': 'integer', 'description': 'User Status', 'format': 'int32', 'example': 1}}, 'xml': {'name': 'user'}}, 'Tag': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'tag'}}, 'Pet': {'required': ['name', 'photoUrls'], 'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'name': {'type': 'string', 'example': 'doggie'}, 'category': {'$ref': '#/components/schemas/Category'}, 'photoUrls': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'type': 'string', 'xml': {'name': 'photoUrl'}}}, 'tags': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'$ref': '#/components/schemas/Tag'}}, 'status': {'type': 'string', 'description': 'pet status in the store', 'enum': ['available', 'pending', 'sold']}}, 'xml': {'name': 'pet'}}, 'ApiResponse': {'type': 'object', 'properties': {'code': {'type': 'integer', 'format': 'int32'}, 'type': {'type': 'string'}, 'message': {'type': 'string'}}, 'xml': {'name': '##default'}}, 'Error': {'type': 'object', 'properties': {'code': {'type': 'string'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}
            }

    """

    def get_data_model(self) -> dict:
        expected_model = {}
        input_schema = self.extractor.get_schema()

        for model_name, model_def in input_schema.items():
            properties = {}

            # --- Gérer allOf ---
            if 'allOf' in model_def:
                # On fusionne toutes les propriétés et références de chaque sous-bloc allOf
                for bloc in model_def['allOf']:
                    # Sous-partie avec propriétés classiques
                    if 'properties' in bloc:
                        for prop_name, prop_def in bloc['properties'].items():
                            # Cas 1 : Référence à un autre schéma ($ref)
                            if '$ref' in prop_def:
                                ref_path = prop_def['$ref'].split('/')[-1]
                                properties[prop_name] = {"type": "object", "ref": ref_path}
                            # Cas 2 : Tableau (array)
                            elif prop_def.get('type') == 'array':
                                items = prop_def.get('items', {})
                                if '$ref' in items:
                                    ref_path = items['$ref'].split('/')[-1]
                                    items_type = {"type": "object", "ref": ref_path}
                                else:
                                    items_type = {"type": "properties"}
                                properties[prop_name] = {"type": "array", "items": items_type}
                            # Cas 3 : Type primitif
                            else:
                                properties[prop_name] = {"type": "properties"}
                    # Sous-partie référence directe à un autre schéma (allOf + $ref)
                    if '$ref' in bloc:
                        ref_path = bloc['$ref'].split('/')[-1]
                        # Propriété spéciale "allOf_ref" (pour tracer la structure composite)
                        properties.setdefault('allOf_refs', []).append({"type": "object", "ref": ref_path})
            # --- Fin gestion allOf ---

            # Traitement classique quand il n'y a pas de allOf à ce niveau
            else:
                for prop_name, prop_def in model_def.get('properties', {}).items():
                    if '$ref' in prop_def:
                        ref_path = prop_def['$ref'].split('/')[-1]
                        properties[prop_name] = {"type": "object", "ref": ref_path}
                    elif prop_def.get('type') == 'array':
                        items = prop_def.get('items', {})
                        if '$ref' in items:
                            ref_path = items['$ref'].split('/')[-1]
                            items_type = {"type": "object", "ref": ref_path}
                        else:
                            items_type = {"type": "properties"}
                        properties[prop_name] = {"type": "array", "items": items_type}
                    else:
                        properties[prop_name] = {"type": "properties"}

            expected_model[model_name] = properties

        return expected_model

    def get_responses_data_model(self) -> dict:
        # print('ICICICICICICICICICICIIC')
        # print(self.extractor.get_responses())
        return self.extractor.get_responses()

    def get_content_objects_per_fp(self):
        # Getting all $ref recursilvely from path
        paths = self.extractor.get_paths()
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
            data = self.extractor.get_paths()
        

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
        # Ajout des attributs aux schémas référencés
        # TODO Implement for version 2
        # for fpid, schemas in result.items():
        #     print(schemas)
        #     for schema_name in schemas:
        #         print(schema_name)
        #         schema_path = [part for part in current_path if part in ["components", "schemas", schema_name]]
        #         schema_data = data
        #         print("schema_data: ")
        #         print(schema_data)
        #         for part in schema_path:
        #             schema_data = schema_data[part]
        #         if "properties" in schema_data:
        #             print("schema property")
        #             print(schema_data["properties"].keys())
        #             result[fpid][schema_name] = list(schema_data["properties"].keys())
            # print(result)
        return result
    
    def get_request_body(self, data_model) -> dict:
        paths = self.extractor.get_paths()
        result = {}

        if paths is None:
            return result
        
        for path, http_method in paths.items():
            # print("path: " + path)
            for http_method, http_method_dict in http_method.items():
                # print("http_method : " + http_method)
                fpid = fpig.generate_fpid(path, http_method, http_method_dict)
                if 'requestBody' in http_method_dict:
                    # print("fpid with request_body: " + fpid)
                    # print(http_method_dict['requestBody']['content'])
                    content =   self.extract_ref(http_method_dict['requestBody']['content'])
                    result.update({fpid : {'Datagroups' : self.get_nested_objects(content, data_model)}})
                    # print('content')
                    # print(content)
                    # print(type(content))
                    # print('result')
                    # print(result)
                else:
                    result.update({ fpid : {}})
        # print("La génèse de request body:")
        # print(result)
        return result

    def get_nested_objects(self, content, data_model):
        nested = set()
        # print('CONTENT')
        # print(content)
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
        paths = self.extractor.get_paths()
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