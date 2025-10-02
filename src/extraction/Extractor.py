import src.specification as specification
import logging

class Extractor():

    # TODO Should eventually receive a spec object, not a spec_path
    def __init__(self, spec_path):
        self.spec = specification.get_specification(spec_path)       
        self.spec_path = spec_path

    def get_metadata() -> list:
        # TODO Refactor to return api name, desc and url in one method
        """
            Every API definition must include the version of the OpenAPI Specification that this definition is based on:
            1.     openapi: 3.0.0
            The OpenAPI version defines the overall structure of an API definition – what you can document and how you document it. OpenAPI 3.0 uses semantic versioning with a three-part version number. The available versions are 3.0.0, 3.0.1, 3.0.2, and 3.0.3; they are functionally the same.
            The info section contains API information: title, description (optional), version:
            title is your API name. description is extended information about your API. It can be multiline and supports the CommonMark dialect of Markdown for rich text representation. HTML is supported to the extent provided by CommonMark (see HTML Blocks in CommonMark 0.27 Specification). version is an arbitrary string that specifies the version of your API (do not confuse it with file revision or the openapi version). You can use semantic versioning like major.minor.patch, or an arbitrary string like 1.0-beta or 2017-07-25. info also supports other keywords for contact information, license, terms of service, and other details.

            Reference: Info Object. (https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#infoObject)
        """
        metadata = []

        return metadata
        
    def get_spec_version(self) -> dict:
        return {'openapi' : self.spec['openapi']}

    def get_api_name(self) -> str:
        return self.spec['info']['title']

    def get_api_description(self) -> str:
        return self.spec['info']['description']
    
    def get_api_version(self) -> str:
        return self.spec['info']['version']

    def get_api_server_url(self) -> list:
        """
            Servers
            The servers section specifies the API server and base URL. You can define one or several servers, such as production and sandbox.
            servers:
                - url: http://api.example.com/v1
                    description: Optional server description, e.g. Main (production) server
                - url: http://staging-api.example.com
                    description: Optional server description, e.g. Internal staging server for testing
            All API paths are relative to the server URL. In the example above, /users means http://api.example.com/v1/users or http://staging-api.example.com/users, depending on the server used. For more information, see API Server and Base Path. 
        """
        urls = []
        if 'servers' in self.spec:   
            for url in self.spec['servers']:
                urls.append(url['url'])
        else:
            logging.info(str(self.spec_path) + " doesn't have a server url.")  
        return urls
        
    def get_paths(self) -> dict:
        """
            The paths section defines individual endpoints (paths) in your API, and the HTTP methods (operations) supported by these endpoints. 
            For example, GET /users can be described as:

                paths:
                /users:
                    get:
                    summary: Returns a list of users.
                    description: Optional extended description in CommonMark or HTML
                    responses:
                        '200':
                        description: A JSON array of user names
                        content:
                            application/json:
                            schema: 
                                type: array
                                items: 
                                type: string

            An operation definition includes parameters, request body (if any), possible response status codes (such as 200 OK or 404 Not Found) and response contents. 
            For more information, see Paths and Operations. (https://swagger.io/docs/specification/paths-and-operations/)
        """
        return self.spec['paths']
    
    def get_schema(self) -> dict:
        """"
            Swagger 2.0 : Schema doesn't exist, should return definition
        """
        # print(self.spec['components']['schemas'])
        return self.spec['components']['schemas']

    def get_responses(self) -> dict:
        """"
            Swagger 2.0 : Schema doesn't exist, should return definition
        """
        if 'components' in self.spec and 'responses' in self.spec['components']:
            return self.spec['components']['responses']
        else:
            logging.info("La clé 'responses' n'existe pas dans 'components'")
            return {}
        # print(self.spec.get('components', {}).get('responses', {}))
        # return self.spec.get('components', {}).get('responses', {})
    
    def get_request_body(openapi_dict, path='/pet', method='put'):
        """
            Récupère le requestBody pour un chemin et une méthode donnés dans un document OpenAPI.
            Args:
                openapi_dict (dict): Le document OpenAPI parsé (YAML ou JSON).
                path (str): Le chemin d'API (par défaut '/pet').
                method (str): La méthode HTTP (par défaut 'put').
            Returns:
                dict ou None: Le requestBody s'il existe, sinon None.
        """
        # On s'assure que le chemin et la méthode existent dans le document
        path_item = openapi_dict.get('paths', {}).get(path, {})
        operation = path_item.get(method, {})
        return operation.get('requestBody')

    def get_request_body_content(self, path):
        paths = self.get_paths()
        for path, http_method in paths.items():
            for http_method, items in http_method.items():
                for item, list_value in items.items():
                    request_body_content = items.get('requestBody', {})
                    # print("\nrequest_body_content\n")
                    # print(request_body_content)

        return request_body_content
    
    def get_href_from_request_body(self, request_body):
        """
            Retourne le contenu de 'href' selon la priorité :
            1. application/json
            2. application/xml
            3. application/x-www-form-urlencoded
            Si non trouvé, retourne None.
        """
        content = request_body.get('content', {})
        mime_types = [
            'application/json',
            'application/xml',
            'application/x-www-form-urlencoded'
        ]
        for mime in mime_types:
            schema = content.get(mime, {}).get('schema', {})
            href = schema.get('$ref')
            if href is not None:
                return href
        return None

    def get_summaries(self) -> list:
        summaries = []
        for method_keys, method_val in self.spec['paths'].items():
            for methods_summaries, method_value in method_val.items():
                if 'summary' in method_value:
                    summaries.append(method_value['summary'])
                else:
                    logging.info("Field summary is missing")
                    summaries.append(self.get_summaries_from_http_operation(method_keys, methods_summaries))
        return summaries
    
    def get_summaries_from_http_operation(self, http_operation, http_verb) -> str:
        segments = http_operation.split('/')
        summary = http_verb+segments[-1]
        return summary