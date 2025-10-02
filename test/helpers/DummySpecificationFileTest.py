import src.openapiinctest as openapiIncTest   # The code to test
import src.specification as specification
import unittest   # The test framework
import os

class DummySpecificationFileTest(unittest.TestCase):
    
    file_path = './test/testdata/swagger_pet_store.yml'
    datagroup_file = './test/testdata/testdatagroups.json'
    
    def open_spec_file(self):
        directory_path = './data/spec/'

        for (root, dirs, files) in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(directory_path, file_name)
                # print('\n' + "Filepath : " + file_path)
                openapiIncTest.test_open_api_yaml(file_path)
    
    def get_schema(self):
        return specification.test_objets_schema(self.file_path)
    
    def get_paths(self):
        return specification.test_objets_path(self.file_path)