import os
import unittest
from src.report_generation.ReportGenerator import ReportGenerator as rg
from src.report_generation.ReportGenerator import *
from src.basic_definitions import data
from src.DataGroup import DataGroup


class Test_Report_Generator(unittest.TestCase):
    fp_counter = 0
    fp_number = "" 


    reportGenerator = rg("./test/testdata/testMeasurements.csv")

    def test_set_fp_number(self):
        self.assertEqual(self.reportGenerator.set_fp_number(), 'PF001')
        self.assertEqual(self.reportGenerator.set_fp_number(), 'PF002')
        for i in range(2, 999):
            self.reportGenerator.set_fp_number()
        with self.assertRaises(ValueError):
            self.reportGenerator.set_fp_number()

