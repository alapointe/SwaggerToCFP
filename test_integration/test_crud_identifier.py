import unittest
from src.basic_definitions import data
import src.CRUDIdentifier as ext
from src.functionalProcess import FunctionalProcess
import src.mappingRules as mr

class Test_CrudOperation(unittest.TestCase):

    mappingRules = mr.MappingRules()
    crud_op = ext.CRUDIdentifier()
    
    def test_identify_crud_operations(self):
        http_verbs = {
            'Update an existing pet.' : {'Update an existing pet.' : "PUT"}, 'Add a new pet to the store.' : {'Add a new pet to the store.' : "POST"}, "Finds Pets by status." : {"Finds Pets by status." : "PUT"}
            }
        crud_operations = {"Update an existing pet." : data.CRUD.UPDATE, 'Add a new pet to the store.' : data.CRUD.CREATE, "Finds Pets by status." : data.CRUD.READ}
        self.assertEqual(sorted(crud_operations) , sorted(self.crud_op.identify_crud_operations(http_verbs)))

    def test_identify_crud_operation_per_fp(self):
        http_verbs = {
            'Update an existing pet.' : {'Update an existing pet.' : "PUT"}, 'Add a new pet to the store.' : {'Add a new pet to the store.' : "POST"}, "Finds Pets by status." : {"Finds Pets by status." : "PUT"}
            }
        fpid = 'Update an existing pet.'
        crud_operation = data.CRUD.UPDATE
        self.assertEqual(crud_operation , self.crud_op.identify_crud_operation_per_fp(http_verbs, fpid))
