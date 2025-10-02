from helpers.DummySpecificationFileTest import DummySpecificationFileTest
from src.basic_definitions.data import CRUD
import src.specification as specification
import src.functionalProcess as fp

class Test_FunctionalProcess(DummySpecificationFileTest):

    def test_get_fp_description(self):
        fp_description = "Récupérer les joyaux de la couronne"
        http_verb = "GET"
        functional_process = fp.FunctionalProcess(fp_description, http_verb)
        self.assertEqual(functional_process.get_fp_description(), fp_description)

    def test_get_http_verb(self):
        fp_description = "Récupérer les joyaux de la couronne"
        http_verb = "GET"
        functional_process = fp.FunctionalProcess(fp_description, http_verb)
        self.assertEqual(functional_process.get_http_verb(), http_verb)

    def test_get_crud_operation(self):
        fp_description = "Récupérer les joyaux de la couronne"
        http_verb = "GET"
        functional_process = fp.FunctionalProcess(fp_description, http_verb, CRUD.READ)
        self.assertEqual(functional_process.get_crud_operation(), CRUD.READ)

    def test_set_crud_operation(self):
        fp_description = "Récupérer les joyaux de la couronne"
        http_verb = "GET"
        functional_process = fp.FunctionalProcess(fp_description, http_verb)
        functional_process.set_crud_operation(CRUD.READ)
        self.assertEqual(functional_process.get_crud_operation(), CRUD.READ)