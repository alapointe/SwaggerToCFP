import logging
import os
import argparse
from src.extraction import HTTPVerbExtractor as HTTPVerbExtractor
from src.extraction import DataGroupExtractor as dge
from src.functionalProcess import FunctionalProcess
from utils.jsonDataHandler import JsonDataHandler
import src.specification as specification
from src.extraction import HTTPVerbExtractor as hve

import src.extraction.Extractor as extractor
import src.aggregator as aggregator
import src.report_generation.ReportGenerator as reportGenerator
import src.function_points_processing.FunctionPointsCalculator as functionPointsCalculator
import src.function_points_processing.MovementTypeIdentifier as movementTypeIdentifier
import src.extraction.DataGroupExtractor as dataGroupExtractor
from src.CRUDIdentifier import CRUDIdentifier
from src.DatagroupIdentifier import DataGroupIdentifier
from src.basic_definitions.api_context import APIContext
from utils.logger import Logger as lg

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
if not logger.hasHandlers():
    logger.addHandler(ch)

def initiate_storage_file(self):
    file = JsonDataHandler('./data/spec/datagroups.json')

def store_data_groups(self):
    file = JsonDataHandler('./data/spec/datagroups.json')

folder_path = "./data/spec/" 

def main():
    filepaths = read_filepaths_in_folder(folder_path)
    rg = reportGenerator.ReportGenerator('.result.csv')
    for spec in filepaths:
        logger.info("Sizing " + spec)
        ext = extractor.Extractor(spec)
        dge = dataGroupExtractor.DataGroupExtractor(ext)
        schema = ext.get_schema()
        data_model = dge.get_data_model(schema)
        responses = dge.get_responses() # Ici ne retourne toujours pas les groupes imbriqués dans les réponses
        response_data_model = dge.get_responses_data_model()
        parameters = dge.get_parameters()
        request_body = dge.get_request_body(data_model) # Ici on retourne les groupes imbriqués dans le request_body
        dgi = DataGroupIdentifier
        request_body_datagroups = dgi.get_request_body_datagroups(dgi, request_body) # Ici on retourne les groupes imbriqués dans le request_body
        parameters_datagroups = dgi.get_parameters_datagroups(dgi, data_model, parameters, request_body)
        responses_datagroups = dgi.get_responses_datagroups(responses, data_model, response_data_model) # Ici ne retourne toujours pas les groupes imbriqués dans les réponses
        mti = movementTypeIdentifier.MovementTypeIdentifier()
        hve = HTTPVerbExtractor.HTTPVerbExtractor
        http_verbs = hve.get_http_verbs(hve, ext)
        entries = mti.identify_entries(request_body_datagroups, parameters_datagroups, data_model)
        reads = mti.identify_reads(parameters_datagroups)
        writes = mti.identify_writes(parameters_datagroups)
        exits = mti.identify_exits(mti, responses_datagroups)
        movement_types = mti.get_movement_types(entries, reads, writes, exits)

        ci = CRUDIdentifier
        crud_operations = ci.identify_crud_operations(ci, http_verbs)

        fpc = functionPointsCalculator.FunctionPointsCalculator(movement_types)
        api_context = APIContext(fpc, crud_operations, entries, reads, writes, exits, rg)
        ag = aggregator.Aggregator(api_context)
        ag.aggregate_new_specification()
    
    rg.generate_report()

def read_filepaths_in_folder(folder_path):
    """
    Reads all file paths within a specified folder.

    Args:
        folder_path: The path to the folder.

    Returns:
        A list of file paths within the folder.
    """
    filepaths = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)  
        if os.path.isfile(filepath):
            filepaths.append(filepath)
    return filepaths

if __name__ == "__main__":
    main()
    logger.info("Finish!")