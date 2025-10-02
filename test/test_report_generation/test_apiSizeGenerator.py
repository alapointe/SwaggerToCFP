import os
import unittest
from src.report_generation.ApiSizeGenerator import ApiSizeGenerator as asg
from src.basic_definitions import data
from src.DataGroup import DataGroup
from src.report_generation.ReportGenerator import ReportGenerator


class Test_ApiSizeGenerator(unittest.TestCase):
    fp_counter = 0
    fp_number = "" 


    apiSizeGenerator = asg("./test/testdata/testApiEffort.csv")
    row = ["API17", "Swagger Pet Store", "68"]
    # reportGenerator = ReportGenerator(row, "./test/testdata/testMeasurements.csv")