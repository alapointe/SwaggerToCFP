import csv
from src import aggregator as ag
from src.DataGroup import DataGroup
from src.basic_definitions import data

type DataGroups = list[DataGroup]

class DataMovementInfo():
    def __init__(self, dmt : data.DataMovementType, data_movement_type_count, dgs : DataGroups):
        self.dmt = dmt
        self.data_movement_type_count = data_movement_type_count
        self.dgs = dgs
        
class DataMovementInfos():
    def __init__(self, entry_info : DataMovementInfo, read_info : DataMovementInfo, write_info : DataMovementInfo, exit_info : DataMovementInfo) -> None:
        self.entry_info = entry_info
        self.read_info = read_info
        self.write_info = write_info
        self.exit_info = exit_info

class ApiSizeGenerator():
        
    def __init__(self, file_path="./test/testdata/testMeasurements.csv"):
        self.file_path = file_path
        self.api_rows = []
        self.fields = ["No API", "Nom de l'API", 'E', 'L', 'C', 'S', 'Total']

    def _write_report(self): 
        file_path = self.file_path
        with open(file_path, 'w', encoding='utf-8') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields

            csvwriter.writerow(self.fields)
            # writing the data rows
            csvwriter.writerows(self.pf_rows)

    def add_api(self, api_id, api_desc, data_movement_infos : DataMovementInfos, cfp_total):
        # self.fields = ["No API", "Nom de l'API", 'E', 'L', 'C', 'S', 'Total']
        self.api_rows.append([api_id, api_desc, data_movement_infos.entry_info.data_movement_type_count, data_movement_infos.read_info.data_movement_type_count, data_movement_infos.write_info.data_movement_type_count, data_movement_infos.exit_info.data_movement_type_count, cfp_total])
        # print(self.pf_rows)

    def generate_report(self):  
        file_path = self.file_path
        with open(file_path, 'w', encoding='utf-8') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile, lineterminator='\n')
            # writing the fields
            csvwriter.writerow(self.fields)
            # writing the data rows
            csvwriter.writerows(self.pf_rows)