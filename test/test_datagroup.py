import json
import os
import unittest
from src.DataGroup import DataGroup as dg
import utils.jsonDataHandler as jdh

class Test_Datagroup(unittest.TestCase):
    datagroup_file = './data/datagroups.yml'

    def setUp(self):
        self.datagroup_file = './data/datagroups.yml'
    
    def test_datagroup_creation(self):
        pass

    def test_store_datagroups(self):
        expected_datagroups = {
            'Order': ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'], 'Category': ['id', 'name'], 'User': ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'], 'Tag': ['id', 'name'], 'Pet': ['id', 'name', 'category', 'photoUrls', 'tags', 'status'], 'ApiResponse': ['code', 'type', 'message'], 'Error': ['code', 'message']
            }
        schema = {
            'Order': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'petId': {'type': 'integer', 'format': 'int64', 'example': 198772}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 7}, 'shipDate': {'type': 'string', 'format': 'date-time'}, 'status': {'type': 'string', 'description': 'Order Status', 'example': 'approved', 'enum': ['placed', 'approved', 'delivered']}, 'complete': {'type': 'boolean'}}, 'xml': {'name': 'order'}}, 'Category': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 1}, 'name': {'type': 'string', 'example': 'Dogs'}}, 'xml': {'name': 'category'}}, 'User': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'username': {'type': 'string', 'example': 'theUser'}, 'firstName': {'type': 'string', 'example': 'John'}, 'lastName': {'type': 'string', 'example': 'James'}, 'email': {'type': 'string', 'example': 'john@email.com'}, 'password': {'type': 'string', 'example': '12345'}, 'phone': {'type': 'string', 'example': '12345'}, 'userStatus': {'type': 'integer', 'description': 'User Status', 'format': 'int32', 'example': 1}}, 'xml': {'name': 'user'}}, 'Tag': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'tag'}}, 'Pet': {'required': ['name', 'photoUrls'], 'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'name': {'type': 'string', 'example': 'doggie'}, 'category': {'$ref': '#/components/schemas/Category'}, 'photoUrls': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'type': 'string', 'xml': {'name': 'photoUrl'}}}, 'tags': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'$ref': '#/components/schemas/Tag'}}, 'status': {'type': 'string', 'description': 'pet status in the store', 'enum': ['available', 'pending', 'sold']}}, 'xml': {'name': 'pet'}}, 'ApiResponse': {'type': 'object', 'properties': {'code': {'type': 'integer', 'format': 'int32'}, 'type': {'type': 'string'}, 'message': {'type': 'string'}}, 'xml': {'name': '##default'}}, 'Error': {'type': 'object', 'properties': {'code': {'type': 'string'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}
            }
         
        with open(dg.store_datagroups(schema), 'r') as file:
            data = json.load(file)
        self.assertEqual(data, expected_datagroups)
    def tearDown(self):
        if os.path.isfile(self.datagroup_file): # Eventually swap for test_file_exists method when fixed
            os.remove(self.datagroup_file)