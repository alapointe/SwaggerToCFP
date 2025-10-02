from lib.openapi3.openapi3 import OpenAPI
import yaml

import os

def test_open_api_yaml(open_api_yml):
    # load the spec file and read the yaml
    with open(open_api_yml, encoding="utf8") as f:
        spec = yaml.safe_load(f.read())

    # parse the spec into python - this will raise if the spec is invalid
    OpenAPI(spec)

