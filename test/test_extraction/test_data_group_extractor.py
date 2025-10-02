import unittest
from test.helpers.CalculationSpecificationFileTest import CalculationSpecificationFileTest
import src.extraction.DataGroupExtractor as dge
import src.extraction.Extractor as extractor
from test.helpers.helpers import Helpers

class Test_DataGroupExtractor(CalculationSpecificationFileTest):

    # TODO Mock schema
    def setUp(self) -> None:
        self.extractor = extractor.Extractor('./test/testdata/swagger_pet_store.yml') #Extractor()
        self.dge = dge.DataGroupExtractor(self.extractor)
        return super().setUp()

    def test_get_parameters(self):
        test_parameters_dict = {'Add a new pet to the store.postpet': {'summary': 'Add a new pet to the store.postpet', 'parameters': []}, 'Create user.postuser': {'summary': 'Create user.postuser', 'parameters': []}, 'Creates list of users with given input array.postcreateWithList': {'summary': 'Creates list of users with given input array.postcreateWithList', 'parameters': []}, 'Delete purchase order by identifier.delete{orderId}': {'summary': 'Delete purchase order by identifier.delete{orderId}', 'parameters': ['orderId']}, 'Delete user resource.delete{username}': {'summary': 'Delete user resource.delete{username}', 'parameters': ['username']}, 'Deletes a pet.delete{petId}': {'summary': 'Deletes a pet.delete{petId}', 'parameters': ['api_key', 'petId']}, 'Find pet by ID.get{petId}': {'summary': 'Find pet by ID.get{petId}', 'parameters': ['petId']}, 'Find purchase order by ID.get{orderId}': {'summary': 'Find purchase order by ID.get{orderId}', 'parameters': ['orderId']}, 'Finds Pets by status.getfindByStatus': {'summary': 'Finds Pets by status.getfindByStatus', 'parameters': ['status']}, 'Finds Pets by tags.getfindByTags': {'summary': 'Finds Pets by tags.getfindByTags', 'parameters': ['tags']}, 'Get user by user name.get{username}': {'summary': 'Get user by user name.get{username}', 'parameters': ['username']}, 'Logs out current logged in user session.getlogout': {'summary': 'Logs out current logged in user session.getlogout', 'parameters': []}, 'Logs user into the system.getlogin': {'summary': 'Logs user into the system.getlogin', 'parameters': ['username', 'password']}, 'Place an order for a pet.postorder': {'summary': 'Place an order for a pet.postorder', 'parameters': []}, 'Returns pet inventories by status.getinventory': {'summary': 'Returns pet inventories by status.getinventory', 'parameters': []}, 'Update an existing pet.putpet': {'summary': 'Update an existing pet.putpet', 'parameters': []}, 'Update user resource.put{username}': {'summary': 'Update user resource.put{username}', 'parameters': ['username']}, 'Updates a pet in the store with form data.post{petId}': {'summary': 'Updates a pet in the store with form data.post{petId}', 'parameters': ['status', 'name', 'petId']}, 'Uploads an image.postuploadImage': {'summary': 'Uploads an image.postuploadImage', 'parameters': ['additionalMetadata', 'petId']}}
        self.assertEqual(Helpers.sort_dict_by_keys_extended(self.dge.get_parameters()), Helpers.sort_dict_by_keys_extended(test_parameters_dict))

    def test_get_data_model(self):    
        expected_data_model = {
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
        self.assertEqual(self.dge.get_data_model(), expected_data_model)

    def test_get_content_objects_per_fp(self):
        expected_result = {'Update an existing pet.putpet': {'Pet': [], 'Error': []}, 'Add a new pet to the store.postpet': {'Pet': [], 'Error': []}, 'Finds Pets by status.getfindByStatus': {'Pet': [], 'Error': []}, 'Finds Pets by tags.getfindByTags': {'Pet': [], 'Error': []}, 'Find pet by ID.get{petId}': {'Pet': [], 'Error': []}, 'Updates a pet in the store with form data.post{petId}': {'Pet': [], 'Error': []}, 'Deletes a pet.delete{petId}': {'Error': []}, 'Uploads an image.postuploadImage': {'ApiResponse': [], 'Error': []}, 'Returns pet inventories by status.getinventory': {'Error': []}, 'Place an order for a pet.postorder': {'Order': [], 'Error': []}, 'Find purchase order by ID.get{orderId}': {'Order': [], 'Error': []}, 'Delete purchase order by identifier.delete{orderId}': {'Error': []}, 'Create user.postuser': {'User': [], 'Error': []}, 'Creates list of users with given input array.postcreateWithList': {'User': [], 'Error': []}, 'Logs user into the system.getlogin': {'Error': []}, 'Logs out current logged in user session.getlogout': {'Error': []}, 'Get user by user name.get{username}': {'User': [], 'Error': []}, 'Update user resource.put{username}': {'User': [], 'Error': []}, 'Delete user resource.delete{username}': {'Error': []}}
        self.assertEqual(self.dge.get_content_objects_per_fp() , expected_result)

    def test_extract_refs_per_fp(self):
        fpid = 'Add a new pet to the store.'

        data = {
            "tags":["pet"],"summary":"Add a new pet to the store.","description":"Add a new pet to the store.","operationId":"addPet","requestBody":{"description":"Create a new pet in the store","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/x-www-form-urlencoded":{"schema":{"$ref":"#/components/schemas/Pet"}}},"required":'true'},"responses":{"200":{"description":"Successful operation","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Pet"}}}},"400":{"description":"Invalid input"},"422":{"description":"Validation exception"},"default":{"description":"Unexpected error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}}},"security":[{"petstore_auth":["write:pets","read:pets"]}]
            }
        current_path = ['post']
        expected_result = {'Add a new pet to the store.': {'Pet': [], 'Error': []}}
        self.assertEqual(self.dge.extract_refs_per_fp(data,current_path, fpid), expected_result)

    def test_get_request_body(self):
        expected = {
            'Add a new pet to the store.postpet': {'Datagroups': ['Category','Pet','Tag']}, 
            'Create user.postuser': {'Datagroups': ['User']}, 
            'Creates list of users with given input array.postcreateWithList': {'Datagroups': ['User']}, 
            'Delete purchase order by identifier.delete{orderId}': {}, 
            'Delete user resource.delete{username}': {}, 
            'Deletes a pet.delete{petId}': {}, 
            'Find pet by ID.get{petId}': {}, 
            'Find purchase order by ID.get{orderId}': {}, 
            'Finds Pets by status.getfindByStatus': {}, 
            'Finds Pets by tags.getfindByTags': {}, 
            'Get user by user name.get{username}': {}, 
            'Logs out current logged in user session.getlogout': {}, 
            'Logs user into the system.getlogin': {}, 
            'Place an order for a pet.postorder': {'Datagroups': ['Order']}, 
            'Returns pet inventories by status.getinventory': {}, 
            'Update an existing pet.putpet': {'Datagroups': ['Category','Pet','Tag']}, 
            'Update user resource.put{username}': {'Datagroups': ['User']}, 
            'Updates a pet in the store with form data.post{petId}': {}, 
            'Uploads an image.postuploadImage': {'Datagroups': ['UNKNOWN']}
            }
        data_model = {
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
        self.assertEqual(Helpers.sort_dict_by_keys(self.dge.get_request_body(data_model)), Helpers.sort_dict_by_keys(expected))
    
    def test_get_responses_data_model(self) -> dict:
        expected_responses_data_model = {}
        self.assertEqual(Helpers.sort_dict_by_keys(self.dge.get_responses_data_model()),Helpers.sort_dict_by_keys(expected_responses_data_model))

    def test_get_nested_objects(self):
        data_model = {
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
        expected_objects = ['Category', 'Pet', 'Tag']
        content = 'Pet'
        self.assertEqual(self.dge.get_nested_objects(content, data_model), sorted(expected_objects))

    def test_get_responses(self):
        expected_responses = {'Update an existing pet.putpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Add a new pet to the store.postpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by status.getfindByStatus': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid status value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by tags.getfindByTags': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid tag value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find pet by ID.get{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Updates a pet in the store with form data.post{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Deletes a pet.delete{petId}': {'200': {'description': 'Pet deleted'}, '400': {'description': 'Invalid pet value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Uploads an image.postuploadImage': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiResponse'}}}}, '400': {'description': 'No file uploaded'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Returns pet inventories by status.getinventory': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Place an order for a pet.postorder': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find purchase order by ID.get{orderId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete purchase order by identifier.delete{orderId}': {'200': {'description': 'order deleted'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Create user.postuser': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Creates list of users with given input array.postcreateWithList': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs user into the system.getlogin': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs out current logged in user session.getlogout': {'200': {'description': 'successful operation'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Get user by user name.get{username}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Update user resource.put{username}': {'200': {'description': 'successful operation'}, '400': {'description': 'bad request'}, '404': {'description': 'user not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete user resource.delete{username}': {'200': {'description': 'User deleted'}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}
        self.assertEqual(self.dge.get_responses(), expected_responses)

    def test_get_responses_when_no_content(self):
        expected_responses = {
            'Update an existing pet.putpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Add a new pet to the store.postpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Finds Pets by status.getfindByStatus': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid status value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Finds Pets by tags.getfindByTags': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid tag value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Find pet by ID.get{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Updates a pet in the store with form data.post{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Deletes a pet.delete{petId}': {'200': {'description': 'Pet deleted'}, '400': {'description': 'Invalid pet value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Uploads an image.postuploadImage': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiResponse'}}}}, '400': {'description': 'No file uploaded'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Returns pet inventories by status.getinventory': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Place an order for a pet.postorder': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Find purchase order by ID.get{orderId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Delete purchase order by identifier.delete{orderId}': {'200': {'description': 'order deleted'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Create user.postuser': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Creates list of users with given input array.postcreateWithList': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Logs user into the system.getlogin': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Logs out current logged in user session.getlogout': {'200': {'description': 'successful operation'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Get user by user name.get{username}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Update user resource.put{username}': {'200': {'description': 'successful operation'}, '400': {'description': 'bad request'}, '404': {'description': 'user not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 
            'Delete user resource.delete{username}': {'200': {'description': 'User deleted'}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}
            }  
        self.assertEqual(self.dge.get_responses(), expected_responses)

    def test_get_http_status_codes(self):
        expected_http_status_codes = {'Update an existing pet.putpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Add a new pet to the store.postpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by status.getfindByStatus': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid status value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by tags.getfindByTags': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid tag value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find pet by ID.get{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Updates a pet in the store with form data.post{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Deletes a pet.delete{petId}': {'200': {'description': 'Pet deleted'}, '400': {'description': 'Invalid pet value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Uploads an image.postuploadImage': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiResponse'}}}}, '400': {'description': 'No file uploaded'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Returns pet inventories by status.getinventory': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Place an order for a pet.postorder': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find purchase order by ID.get{orderId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete purchase order by identifier.delete{orderId}': {'200': {'description': 'order deleted'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Create user.postuser': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Creates list of users with given input array.postcreateWithList': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs user into the system.getlogin': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs out current logged in user session.getlogout': {'200': {'description': 'successful operation'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Get user by user name.get{username}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Update user resource.put{username}': {'200': {'description': 'successful operation'}, '400': {'description': 'bad request'}, '404': {'description': 'user not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete user resource.delete{username}': {'200': {'description': 'User deleted'}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}
        self.assertEqual(self.dge.get_http_status_codes(), expected_http_status_codes)

    def test_extract_ref(self):
        data = {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}
        data_2 = {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/User'}}}}
        data_3 = {'application/json-patch+json': {'schema': {'$ref' : "#/components/schemas/Code"}}}
        data_4 = {'application/*+json' : {'schema' : {}}}
            
        self.assertEqual(self.dge.extract_ref(data), 'Order')
        self.assertEqual(self.dge.extract_ref(data_2), 'User')
        self.assertEqual(self.dge.extract_ref(data_3), 'Code')
        self.assertEqual(self.dge.extract_ref(data_4), "UNKNOWN")