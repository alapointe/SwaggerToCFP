import unittest
from utils.functional_process_id_generator import Utils

class Test_FunctionalProcessIDGenerator(unittest.TestCase):

    def setUp(self):
        self.fpig = Utils()
        return super().setUp()
          
    def test_generate_fpid(self):
        path = '/pet'
        http_method = 'put'
        http_method_dict = {
            "tags":["pet"],"summary":"Update an existing pet.","description":"Update an existing pet by Id.","operationId":"updatePet","requestBody":{"description":"Update an existent pet in the store","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/x-www-form-urlencoded":{"schema":{"$ref":"#/components/schemas/Pet"}}},"required":'true'},"responses":{"200":{"description":"Successful operation","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Pet"}}}},"400":{"description":"Invalid ID supplied"},"404":{"description":"Pet not found"},"422":{"description":"Validation exception"},"default":{"description":"Unexpected error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}}},"security":[{"petstore_auth":["write:pets","read:pets"]}]
            }
        self.assertEqual(self.fpig.generate_fpid(path, http_method, http_method_dict), "Update an existing pet.putpet")

    def test_generate_fpid_without_summary(self):
        path = '/pet'
        http_method = 'put'
        http_method_dict = {
            "tags":["pet"],"description":"Update an existing pet by Id.","operationId":"updatePet","requestBody":{"description":"Update an existent pet in the store","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/x-www-form-urlencoded":{"schema":{"$ref":"#/components/schemas/Pet"}}},"required":'true'},"responses":{"200":{"description":"Successful operation","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Pet"}},"application/xml":{"schema":{"$ref":"#/components/schemas/Pet"}}}},"400":{"description":"Invalid ID supplied"},"404":{"description":"Pet not found"},"422":{"description":"Validation exception"},"default":{"description":"Unexpected error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Error"}}}}},"security":[{"petstore_auth":["write:pets","read:pets"]}]
            }
        self.assertEqual(self.fpig.generate_fpid(path, http_method, http_method_dict), "putpet")