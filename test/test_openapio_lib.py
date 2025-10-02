from openapi3 import OpenAPI
import yaml
import src.openapiinctest as openapiIncTest   # The code to test
import src.specification as specification
import unittest   # The test framework
import os

class Test_TestOpenAPILibtestYamlCanBeOpened(unittest.TestCase):
    @unittest.skip("Needs refactor")
    def test_openapi_specs(self):
        directory_path = './data/spec/'

        for (root, dirs, files) in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(directory_path, file_name)
                openapiIncTest.test_open_api_yaml(file_path)

    def test_openapiObjetsSchema(self):  

        returnedSchema = specification.test_objets_schema('./test/testdata/swagger_pet_store.yml')
        object = 'Order'
        found = False
        if object in returnedSchema:
            found  = True

        if not found:
             self.fail()

        objectCount = 0
        for object in returnedSchema:
            objectCount += 1
        
        self.assertEqual(objectCount, 7, "Number of objects detected is invalid.")

    def test_openapiProprietesObjets(self):
        specification.test_objets_schema('./test/testdata/swagger_pet_store.yml')


if __name__ == '__main__':
    unittest.main()