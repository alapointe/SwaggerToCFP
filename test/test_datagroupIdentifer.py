import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.DatagroupIdentifier import DataGroupIdentifier
import src.extraction.Extractor as extractor
import src.extraction.DataGroupExtractor as dge
from test.helpers.helpers import Helpers

class Test_DataGroupIdentifier(unittest.TestCase):
    def setUp(self):
        self.dgi = DataGroupIdentifier()  

    def test_identify_datagroups(self):
        test_data_model_dict  = {
            'Order': ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'], 
            'Category': ['id', 'name'], 
            'User': ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'], 
            'Tag': ['id', 'name'], 
            'Pet': ['id', 'name', 'category', 'photoUrls', 'tags', 'status'], 
            'ApiResponse': ['code', 'type', 'message'], 
            'Error': ['code', 'message']
            }
        self.assertEqual(self.dgi.identify_datagroups(test_data_model_dict) , test_data_model_dict)
    
    def test_identify_datagroups_per_fp(self):
        test_data_model_dict  = {
            'Order': ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'], 
            'Category': ['id', 'name'], 
            'User': ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'], 
            'Tag': ['id', 'name'], 
            'Pet': ['id', 'name', 'category', 'photoUrls', 'tags', 'status'], 
            'ApiResponse': ['code', 'type', 'message'], 
            'Error': ['code', 'message']
            }
        self.assertEqual(self.dgi.identify_datagroups_per_fp(test_data_model_dict) , test_data_model_dict)
    
    def test_get_parameters_datagroups(self):
        dgi = DataGroupIdentifier() 
        data_model = {
            'Order': ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'], 
            'Category': ['id', 'name'], 
            'User': ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'], 
            'Tag': ['id', 'name'], 
            'Pet': ['id', 'name', 'category', 'photoUrls', 'tags', 'status'], 
            'ApiResponse': ['code', 'type', 'message'], 
            'Error': ['code', 'message']
            }
        parameters = {
            'Add a new pet to the store.': {'summary': 'Add a new pet to the store.', 'parameters': []}, 
            'Create user.': {'summary': 'Create user.', 'parameters': []}, 
            'Creates list of users with given input array.': {'summary': 'Creates list of users with given input array.', 'parameters': []}, 
            'Delete purchase order by identifier.': {'summary': 'Delete purchase order by identifier.', 'parameters': ['orderId']}, 
            'Delete user resource.': {'summary': 'Delete user resource.', 'parameters': ['username']}, 
            'Deletes a pet.': {'summary': 'Deletes a pet.', 'parameters': ['api_key', 'petId']}, 
            'Find pet by ID.': {'summary': 'Find pet by ID.', 'parameters': ['petId']}, 
            'Find purchase order by ID.': {'summary': 'Find purchase order by ID.', 'parameters': ['orderId']}, 
            'Finds Pets by status.': {'summary': 'Finds Pets by status.', 'parameters': ['status']}, 
            'Finds Pets by tags.': {'summary': 'Finds Pets by tags.', 'parameters': ['tags']}, 
            'Get user by user name.': {'summary': 'Get user by user name.', 'parameters': ['username']}, 
            'Logs out current logged in user session.': {'summary': 'Logs out current logged in user session.', 'parameters': []}, 
            'Logs user into the system.': {'summary': 'Logs user into the system.', 'parameters': ['username', 'password']}, 
            'Place an order for a pet.': {'summary': 'Place an order for a pet.', 'parameters': []}, 
            'Returns pet inventories by status.': {'summary': 'Returns pet inventories by status.', 'parameters': []}, 
            'Update an existing pet.': {'summary': 'Update an existing pet.', 'parameters': []}, 
            'Update user resource.': {'summary': 'Update user resource.', 'parameters': ['username']}, 
            'Updates a pet in the store with form data.': {'summary': 'Updates a pet in the store with form data.', 'parameters': ['petId', 'name', 'status']}, 
            'Uploads an image.': {'summary': 'Uploads an image.', 'parameters': ['petId', 'additionalMetadata']}
            }
        request_body = {
               'Add a new pet to the store.postpet': {'Datagroups': ['Category', 'Pet', 'Tag']}, 
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
               'Update an existing pet.putpet': {'Datagroups': ['Category', 'Pet', 'Tag']}, 
               'Update user resource.put{username}': {'Datagroups': ['User']}, 'Updates a pet in the store with form data.post{petId}': {}, 
               'Uploads an image.postuploadImage': {'Datagroups': ['UNKNOWN']}
               } 
        parameters_datagroups = {
            'Add a new pet to the store.': [], 'Create user.': [], 'Creates list of users with given input array.': [], 'Delete purchase order by identifier.': [], 'Delete user resource.': ['User'], 'Deletes a pet.': ['Order'], 'Find pet by ID.': ['Order'], 'Find purchase order by ID.': [], 'Finds Pets by status.': ['Order'], 'Finds Pets by tags.': ['Pet'], 'Get user by user name.': ['User'], 'Logs out current logged in user session.': [], 'Logs user into the system.': ['User'], 'Place an order for a pet.': [], 'Returns pet inventories by status.': [], 'Update an existing pet.': [], 'Update user resource.': ['User'], 'Updates a pet in the store with form data.': ['Category', 'Order', 'Pet'], 'Uploads an image.': ['Order']}
        self.assertEqual(Helpers.sort_dict_by_keys_extended(dgi.get_parameters_datagroups(data_model, parameters, request_body)) , Helpers.sort_dict_by_keys_extended(parameters_datagroups))

    def test_get_request_body_datagroups(self):
        request_body = {
               'Add a new pet to the store.postpet': {'Datagroups': ['Category', 'Pet', 'Tag']}, 
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
               'Update an existing pet.putpet': {'Datagroups': ['Category', 'Pet', 'Tag']}, 
               'Update user resource.put{username}': {'Datagroups': ['User']}, 'Updates a pet in the store with form data.post{petId}': {}, 
               'Uploads an image.postuploadImage': {'Datagroups': ['UNKNOWN']}
               } 
        expected = {
               'Add a new pet to the store.postpet': {'Datagroups': ['Category', 'Pet', 'Tag']}, 
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
               'Update an existing pet.putpet': {'Datagroups': ['Category', 'Pet', 'Tag']}, 
               'Update user resource.put{username}': {'Datagroups': ['User']}, 'Updates a pet in the store with form data.post{petId}': {}, 
               'Uploads an image.postuploadImage': {'Datagroups': ['UNKNOWN']}
               }
        self.assertEqual(Helpers.sort_dict_by_keys_extended(self.dgi.get_request_body_datagroups(request_body)) , Helpers.sort_dict_by_keys_extended(expected))

    def test_get_responses_datagroups(self):
        response_data_model = {}        
        data_model = {'Order': {'id': {'type': 'properties'}, 'petId': {'type': 'properties'}, 'quantity': {'type': 'properties'}, 'shipDate': {'type': 'properties'}, 'status': {'type': 'properties'}, 'complete': {'type': 'properties'}}, 'Category': {'id': {'type': 'properties'}, 'name': {'type': 'properties'}}, 'User': {'id': {'type': 'properties'}, 'username': {'type': 'properties'}, 'firstName': {'type': 'properties'}, 'lastName': {'type': 'properties'}, 'email': {'type': 'properties'}, 'password': {'type': 'properties'}, 'phone': {'type': 'properties'}, 'userStatus': {'type': 'properties'}}, 'Tag': {'id': {'type': 'properties'}, 'name': {'type': 'properties'}}, 'Pet': {'id': {'type': 'properties'}, 'name': {'type': 'properties'}, 'category': {'type': 'object', 'ref': 'Category'}, 'photoUrls': {'type': 'array', 'items': {'type': 'properties'}}, 'tags': {'type': 'array', 'items': {'type': 'object', 'ref': 'Tag'}}, 'status': {'type': 'properties'}}, 'ApiResponse': {'code': {'type': 'properties'}, 'type': {'type': 'properties'}, 'message': {'type': 'properties'}}, 'Error': {'code': {'type': 'properties'}, 'message': {'type': 'properties'}}}
        extracted_responses = {'Update an existing pet.putpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Add a new pet to the store.postpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by status.getfindByStatus': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid status value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by tags.getfindByTags': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid tag value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find pet by ID.get{petId}': {'200': {'description': 
'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Updates a pet in the store with form data.post{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, 
'400': {'description': 'Invalid input'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Deletes a pet.delete{petId}': {'200': {'description': 'Pet deleted'}, '400': {'description': 'Invalid pet value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Uploads an image.postuploadImage': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiResponse'}}}}, '400': {'description': 'No file uploaded'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Returns pet inventories by status.getinventory': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}, 'default': {'description': 'Unexpected error', 
'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Place an order for a pet.postorder': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': 
{'$ref': '#/components/schemas/Error'}}}}}, 'Find purchase order by ID.get{orderId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete purchase order by identifier.delete{orderId}': {'200': {'description': 'order deleted'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Create user.postuser': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Creates list of users with given input array.postcreateWithList': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs user into the system.getlogin': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs out current logged in user session.getlogout': {'200': {'description': 'successful operation'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Get user by user name.get{username}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Update user resource.put{username}': {'200': {'description': 'successful operation'}, '400': {'description': 'bad request'}, '404': {'description': 'user not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete user resource.delete{username}': {'200': {'description': 'User deleted'}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}
        expected_responses_datagroups = {
            'Add a new pet to the store.postpet': ['Category', 'Error', 'Pet', 'Tag'], 
            'Create user.postuser': ['Error', 'User'], 
            'Creates list of users with given input array.postcreateWithList': ['Error', 'User'], 
            'Delete purchase order by identifier.delete{orderId}': ['Error'], 'Delete user resource.delete{username}': ['Error'], 
            'Deletes a pet.delete{petId}': ['Error'], 'Find pet by ID.get{petId}': ['Category', 'Error', 'Pet', 'Tag'], 
            'Find purchase order by ID.get{orderId}': ['Error', 'Order'], 
            'Finds Pets by status.getfindByStatus': ['Category', 'Error', 'Pet', 'Tag'], 
            'Finds Pets by tags.getfindByTags': ['Category', 'Error', 'Pet', 'Tag'], 
            'Get user by user name.get{username}': ['Error', 'User'], 
            'Logs out current logged in user session.getlogout': ['Error'], 
            'Logs user into the system.getlogin': ['Error'], 
            'Place an order for a pet.postorder': ['Error', 'Order'], 
            'Returns pet inventories by status.getinventory': ['Error'], 
            'Update an existing pet.putpet': ['Category', 'Error', 'Pet', 'Tag'], 
            'Update user resource.put{username}': ['Error'], 
            'Updates a pet in the store with form data.post{petId}': ['Category', 'Error', 'Pet', 'Tag'], 
            'Uploads an image.postuploadImage': ['ApiResponse', 'Error']
            }
        self.assertEqual(Helpers.sort_dict_by_keys(self.dgi.get_responses_datagroups(extracted_responses, data_model, response_data_model)) , Helpers.sort_dict_by_keys(expected_responses_datagroups))  

    def test_get_responses_datagroups_when_no_content(self):
        data_model = {
            'Order': ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'], 
            'Category': ['id', 'name'], 
            'User': ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'], 
            'Tag': ['id', 'name'], 
            'Pet': ['id', 'name', 'category', 'photoUrls', 'tags', 'status'], 
            'ApiResponse': ['code', 'type', 'message'], 
            'Error': ['code', 'message']
            }
        extracted_responses = {'Update an existing pet.putpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Add a new pet to the store.postpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by status.getfindByStatus': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid status value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by tags.getfindByTags': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid tag value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find pet by ID.get{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Updates a pet in the store with form data.post{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Deletes a pet.delete{petId}': {'200': {'description': 'Pet deleted'}, '400': {'description': 'Invalid pet value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Uploads an image.postuploadImage': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiResponse'}}}}, '400': {'description': 'No file uploaded'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Returns pet inventories by status.getinventory': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Place an order for a pet.postorder': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find purchase order by ID.get{orderId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete purchase order by identifier.delete{orderId}': {'200': {'description': 'order deleted'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Create user.postuser': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Creates list of users with given input array.postcreateWithList': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs user into the system.getlogin': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs out current logged in user session.getlogout': {'200': {'description': 'successful operation'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Get user by user name.get{username}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Update user resource.put{username}': {'200': {'description': 'successful operation'}, '400': {'description': 'bad request'}, '404': {'description': 'user not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete user resource.delete{username}': {'200': {'description': 'User deleted'}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}
        expected_responses_datagroups = {'Add a new pet to the store.postpet': ['Error', 'Pet'], 'Create user.postuser': ['Error', 'User'], 'Creates list of users with given input array.postcreateWithList': ['Error', 'User'], 'Delete purchase order by identifier.delete{orderId}': ['Error'], 'Delete user resource.delete{username}': ['Error'], 'Deletes a pet.delete{petId}': ['Error'], 'Find pet by ID.get{petId}': ['Error', 'Pet'], 'Find purchase order by ID.get{orderId}': ['Error', 'Order'], 'Finds Pets by status.getfindByStatus': ['Error', 'Pet'], 'Finds Pets by tags.getfindByTags': ['Error', 'Pet'], 'Get user by user name.get{username}': ['Error', 'User'], 'Logs out current logged in user session.getlogout': ['Error'], 'Logs user into the system.getlogin': ['Error'], 'Place an order for a pet.postorder': ['Error', 'Order'], 'Returns pet inventories by status.getinventory': ['Error'], 'Update an existing pet.putpet': ['Error', 'Pet'], 'Update user resource.put{username}': ['Error'], 'Updates a pet in the store with form data.post{petId}': ['Error', 'Pet'], 'Uploads an image.postuploadImage': ['ApiResponse', 'Error']}
        response_data_model = {}
        self.assertEqual(Helpers.sort_dict_by_keys(self.dgi.get_responses_datagroups(extracted_responses, data_model, response_data_model)) , Helpers.sort_dict_by_keys(expected_responses_datagroups))

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
        self.assertEqual(sorted(self.dgi.get_nested_objects(content, data_model)), sorted(expected_objects))
        
    @unittest.skip('needs racftoring')
    def test_get_nested_responses(self):
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
        responses_data_model = {}
        content = ''
        expected_responses = []
        self.assertEqual(self.dgi.get_nested_responses(content, data_model, responses_data_model), expected_responses)

    def test_dict_in_data_model(self):
        data_model = {
            'Order': ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'], 
            'Category': ['id', 'name'], 
            'User': ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'], 
            'Tag': ['id', 'name'], 
            'Pet': ['id', 'name', 'category', 'photoUrls', 'tags', 'status'], 
            'ApiResponse': ['code', 'type', 'message'], 
            'Error': ['code', 'message']
            }
        dict_name = 'Order'
        self.assertTrue(self.dgi.dict_in_data_model(data_model, dict_name))
        dict_name = 'Felix El Gato'
        self.assertFalse(self.dgi.dict_in_data_model(data_model, dict_name))
    
    def test_get_http_status_datagroups(self):
        extracted_status_codes = {}
        self.assertEqual(self.dgi.get_http_status_datagroups(extracted_status_codes) , extracted_status_codes)

    def test_extract_ref_with_direct_ref(self):
        data = {'$ref': '#/components/schemas/User'}
        expected_result = 'User'
        self.assertEqual(self.dgi.extract_ref(data), expected_result)

    def test_extract_ref_with_nested_ref(self):
        data = {'property': {'type': 'object', 'properties': {'nested_prop': {'$ref': '#/components/schemas/Address'}}}}
        expected_result = 'Address'
        self.assertEqual(self.dgi.extract_ref(data), expected_result)

    def test_extract_ref_with_list(self):
        data = [{'$ref': '#/components/schemas/Item'}, {'other_data': 'value'}]
        expected_result = 'Item'
        self.assertEqual(self.dgi.extract_ref(data), expected_result)

    def test_extract_ref_no_ref_found(self):
        data = {'property': {'type': 'string'}}
        expected_result = None
        self.assertEqual(self.dgi.extract_ref(data), expected_result)

    def test_validate_schema(self):
        extracted_responses = {'Update an existing pet.putpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Add a new pet to the store.postpet': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by status.getfindByStatus': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid status value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Finds Pets by tags.getfindByTags': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}, 'application/xml': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Pet'}}}}}, '400': {'description': 'Invalid tag value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find pet by ID.get{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Updates a pet in the store with form data.post{petId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Pet'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Pet'}}}}, '400': {'description': 'Invalid input'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Deletes a pet.delete{petId}': {'200': {'description': 'Pet deleted'}, '400': {'description': 'Invalid pet value'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Uploads an image.postuploadImage': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ApiResponse'}}}}, '400': {'description': 'No file uploaded'}, '404': {'description': 'Pet not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Returns pet inventories by status.getinventory': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Place an order for a pet.postorder': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid input'}, '422': {'description': 'Validation exception'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Find purchase order by ID.get{orderId}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Order'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/Order'}}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete purchase order by identifier.delete{orderId}': {'200': {'description': 'order deleted'}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Create user.postuser': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Creates list of users with given input array.postcreateWithList': {'200': {'description': 'Successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs user into the system.getlogin': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Logs out current logged in user session.getlogout': {'200': {'description': 'successful operation'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Get user by user name.get{username}': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/User'}}, 'application/xml': {'schema': {'$ref': '#/components/schemas/User'}}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Update user resource.put{username}': {'200': {'description': 'successful operation'}, '400': {'description': 'bad request'}, '404': {'description': 'user not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}, 'Delete user resource.delete{username}': {'200': {'description': 'User deleted'}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}, 'default': {'description': 'Unexpected error', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Error'}}}}}}
        data = 'Error'
        expected = []
        self.assertEqual(self.dgi.validate_schema(data, extracted_responses), expected)