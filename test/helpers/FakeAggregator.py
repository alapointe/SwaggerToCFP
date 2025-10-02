from src.basic_definitions.data import DataMovementType
from src.report_generation import ReportGenerator


class FakeAggregator:

    spec_path = './test/testdata/swagger_pet_store.yml'

    global api_counter 
    api_counter = 0


    def aggregate_new_specification(self) -> list:
        pass

    def aggregate_fp_description(self): #, api_description):
        pass

    def get_new_api_number(self):
        global api_counter
        api_counter += 1
        return 'API' + str(api_counter)
