import unittest   # The test framework
from src.basic_definitions.functionnal_process_context import FunctionnalProcessContext

class Test_BasicDefinitions(unittest.TestCase):

    def test_functionnal_process_context(self):
        fpc = FunctionnalProcessContext;
        self.assertIs(fpc, FunctionnalProcessContext)