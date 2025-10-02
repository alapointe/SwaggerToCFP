from src import DatagroupIdentifier
from src.basic_definitions.data import DataMovementType
from src.extraction import DataGroupExtractor, HTTPVerbExtractor
from src.function_points_processing import MovementTypeIdentifier
from src.function_points_processing.FunctionPointsCalculator import FunctionPointsCalculator
from src.extraction.Extractor import Extractor
from src.report_generation import ReportGenerator
from src.CRUDIdentifier import CRUDIdentifier
import logging

# create logger
logger = logging.getLogger('LOG')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

class Aggregator:

    spec_path = './test/testdata/swagger_pet_store.yml'

    global api_counter 
    api_counter = 0

    def __init__(self, api_context) -> None:
        self.api_context = api_context

    def aggregate_new_specification(self) -> list:
        self.fpc = self.api_context.fpc
        self.crud_operations = self.api_context.crud_operations
        self.entries = self.api_context.entries
        self.reads = self.api_context.reads
        self.writes = self.api_context.writes
        self.exits = self.api_context.exits
        self.rg = self.api_context.rg


        # """ TODO For each fp (use fp)"""
        api_number = self.get_new_api_number()
        for fpid in self.fpc.movement_types:

            entry_info = ReportGenerator.DataMovementInfo(DataMovementType.ENTRY, self.get_entry_count(self.fpc, fpid), self.get_entry_datagroups(self.entries, fpid))
            # logger.debug("Aggregating fpid " + fpid)
            read_info = ReportGenerator.DataMovementInfo(DataMovementType.READ, self.get_read_count(self.fpc, fpid), self.get_read_datagroups(self.reads, fpid))
            write_info = ReportGenerator.DataMovementInfo(DataMovementType.WRITE, self.get_write_count(self.fpc, fpid), self.get_write_datagroups(self.writes, fpid))
            exit_info = ReportGenerator.DataMovementInfo(DataMovementType.EXIT, self.get_exit_count(self.fpc, fpid), self.get_exit_datagroups(self.exits, fpid))
            data_movements = ReportGenerator.DataMovementInfos(entry_info, read_info, write_info, exit_info)
            self.rg.add_functional_process(fpid, self.get_crud_type(self.crud_operations, fpid), data_movements, self.get_total_count(self.fpc, fpid), api_number)

    # def print_fp(self):
    #     print(self.api_contexts)
        # FunctionPointsCalculator

    def aggregate_fp_description(self): #, api_description):
        self.rg.generate_report()

    def get_new_api_number(self):
        global api_counter
        api_counter += 1
        return 'API' + str(api_counter)
        
    def get_functional_process_description(self, fpid):
        return fpid
    
    def get_crud_type(self, crud_operations, fpid):
        return crud_operations[fpid]

    def get_entry_count(self, fpc, fpid):
        return fpc.calculate_entry_count(fpid)
    
    def get_read_count(self, fpc, fpid):
        return fpc.calculate_read_count(fpid)

    def get_write_count(self, fpc, fpid):
        return fpc.calculate_write_count(fpid)

    def get_exit_count(self, fpc, fpid):
        return fpc.calculate_exit_count(fpid)
    
    def get_total_count(self, fpc, fpid):
        return fpc.calculate_total_count(fpid)

    def get_entry_datagroups(self, entries, fpid):
        # entries = mti.identify_entries(dge.get_request_body())
        for data_type, values in entries[fpid].items():
            return sorted(values)

    def get_read_datagroups(self, reads, fpid):
        # logger.debug("Getting read datagroups for fpid " + fpid + "from ")
        # reads = mti.identify_reads(dgi.get_parameters_datagroups, dgi.get_request_body_datagroups)
        for data_type, values in reads[fpid].items():
            return sorted(values)
    
    def get_write_datagroups(self, writes, fpid) -> list:

        # writes = mti.identify_writes(dge.get_http_status_codes())q
        for data_type, values in writes[fpid].items():
            return sorted(values)
    
    def get_exit_datagroups(self, exits, fpid):
        # exits = mti.identify_exits(dgi.get_responses_datagroups(dge.get_responses()))
        for data_type, values in exits[fpid].items():
            return sorted(values)