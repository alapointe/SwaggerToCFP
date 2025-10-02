import csv
from src import aggregator as ag
from src.basic_definitions import data
from src.DataGroup import DataGroup

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

class ReportGenerator():

    def __init__(self, file_path="./test/testdata/testMeasurements.csv"):
        self.file_path = file_path
        self.pf_rows = []
        self.fields = ['No PF', 'Processus fonctionnel', 'CRUD', 'E', 'Données E', 'L', 'Données L', 'C', 'Données C', 'S', 'Données S', 'Total', 'No API', 'No API 2', 'Qualité', 'Notes', 'Nb verbes', 'Verbe 1', 'Verbe 2', 'Verbe 3']
        self.fp_counter = 0
        # self.fields = ['FP ID', 'Functional process description', 'CRUD type', 'Entry count', 'Entry data groups', 'Read count', 'Read data groups', 'Write count', 'Write data groups', 'Exit count', 'Exit data groups', 'CFP Total', 'API ID']

    def _write_report(self): 
        file_path = self.file_path
        with open(file_path, 'w', encoding='utf-8') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields

            csvwriter.writerow(self.fields)
            # writing the data rows
            csvwriter.writerows(self.pf_rows)

    def add_functional_process(self, fp_desc, crud_type, data_movement_infos : DataMovementInfos, cfp_total, api_id):
        # self.fields = ['FF ID', 'Functional process description', 'CRUD type', 'E', 'Données E', 'L', 'Données L', 'Write count', 'Write data groups', 'Exit count', 'Exit data groups', 'CFP Total', 'API ID']
        fp_id = self.set_fp_number()
        entry_data_group_ids = " ".join(str(data_group) for data_group in data_movement_infos.entry_info.dgs)
        read_data_group_ids = " ".join(str(data_group) for data_group in data_movement_infos.read_info.dgs)
        write_data_group_ids = " ".join(str(data_group) for data_group in data_movement_infos.write_info.dgs)
        exit_data_group_ids = " ".join(str(data_group) for data_group in data_movement_infos.exit_info.dgs)
        self.pf_rows.append([fp_id, fp_desc, str(crud_type), data_movement_infos.entry_info.data_movement_type_count, entry_data_group_ids, data_movement_infos.read_info.data_movement_type_count, read_data_group_ids, data_movement_infos.write_info.data_movement_type_count, write_data_group_ids, data_movement_infos.exit_info.data_movement_type_count, exit_data_group_ids, cfp_total, api_id]) #,
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

    def set_fp_number(self):
        self.fp_counter += 1
        if self.fp_counter > 999:
            raise ValueError(f"{self.fp_counter} exceeds number of processes limit. The maximum number of processes is 999.")
        elif self.fp_counter < 10 :
            return 'PF00' + str(self.fp_counter)
        elif self.fp_counter < 100 :
            return 'PF0' + str(self.fp_counter)
        else :
            return 'PF' + str(self.fp_counter)
        