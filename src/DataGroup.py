from lib.openapi3.openapi3 import OpenAPI
import utils.jsonDataHandler as jdh

class DataGroup():

    def __init__(self, id) -> None:
        self.id = id

    def store_datagroups(schema, file_path = './data/datagroups.yml') -> str:
        datagroups = {}
        data_handler = jdh.JsonDataHandler(file_path)
        for cle, valeur in schema.items():
            liste_properties = []
            
            if "properties" in valeur:
                properties = valeur["properties"]
                for property in properties.keys():
                    liste_properties.append(property)
                datagroups[cle] = liste_properties
                data_handler.store_data(datagroups)
        return file_path
