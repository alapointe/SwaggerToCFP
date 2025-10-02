from src import CRUDIdentifier, DatagroupIdentifier
from src.extraction import HTTPVerbExtractor
from src.extraction.DataGroupExtractor import DataGroupExtractor
from src.extraction.Extractor import Extractor
from src.function_points_processing import FunctionPointsCalculator, MovementTypeIdentifier
from src.report_generation import ReportGenerator


class APIContext():
    paths = []
    
    def __init__(self, fpc : FunctionPointsCalculator, crud_operations : dict, entries : list, reads : list, writes : list, exits : list, rg : ReportGenerator) -> None:
        self.fpc = fpc
        self.crud_operations = crud_operations
        self.entries = entries
        self.reads = reads
        self.writes = writes
        self.exits = exits
        self.rg = rg


