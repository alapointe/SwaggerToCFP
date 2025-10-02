from lib.openapi3.openapi3 import OpenAPI
import yaml
import logging

# class Specification:
#     def __init__(self, file_path):
#         self.file_path = './data/spec/SwaggerPetStore.yml' # eventually file_path from main

#     def get_specification(self):
#         # load the spec file and read the yaml
#         with open(self.file_path, encoding="utf8") as f:
#             spec = yaml.safe_load(f.read())
#         return spec

yamlFile = './test/testdata/swagger_pet_store.yml'
specification_path = './test/testdata/swagger_pet_store.yml'

def get_specification(specification_path) -> dict:
    with open(specification_path, encoding="utf8") as f:
        spec = yaml.safe_load(f.read())
    return spec

def test_objets_schema(open_api_yml):
    # load the spec file and read the yaml
    with open(open_api_yml, encoding="utf8") as f:
        spec = yaml.safe_load(f.read())
    # parse the spec into python - this will raise if the spec is invalid
    OpenAPI(spec)

    return spec['components']['schemas'] 

def test_objets_path(open_api_yml):
    # load the spec file and read the yaml
    with open(open_api_yml) as f:
        spec = yaml.safe_load(f.read())
    # parse the spec into python - this will raise if the spec is invalid
    OpenAPI(spec)

    return spec['paths']
