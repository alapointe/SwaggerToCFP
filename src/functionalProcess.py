from lib.openapi3.openapi3 import OpenAPI
from src.basic_definitions.data import CRUD
import src.specification as specification
import yaml

class FunctionalProcess():
    number_of_fp = 0
    functional_processes = []
    # paths = specification.get_paths(openApiYml)

    def __init__(self, fp_description, http_verb = None, crud_operation = CRUD.UNDEFINED) -> None:
        self.number_of_fp += 1
        self.fp_description = fp_description
        self.http_verb = http_verb
        self.crud_operation = crud_operation
        self.apis = []
        self.dataMouvement = []
        self.functional_processes.append(self.__dict__)
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    
    def get_fp_description(self):
        return self.fp_description

    def get_http_verb(self):
        return self.http_verb

    def get_crud_operation(self):
        return self.crud_operation
    
    def get_functional_processes(self):
        return self.fp

    def get_functional_processes_per_api():
        pass
        return []
    
    def set_crud_operation(self, crud_op):
        self.crud_operation = crud_op
    
    def get_methods():
        pass
        return []
    