import unittest
from src.basic_definitions.data import DataMovementType
from test.helpers.CalculationSpecificationFileTest import CalculationSpecificationFileTest
import src.function_points_processing.FunctionPointsCalculator as fpc
import src.basic_definitions as data

class Test_FunctionPointsCalculator(CalculationSpecificationFileTest):
    movement_types = {
            'Add a new pet to the store.': {
                DataMovementType.ENTRY: ['Category', 'Pet', 'Tag'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Category', 'Pet', 'Tag', 'Error']
            },
            'Create user.': {
                DataMovementType.ENTRY: ['User'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['User', 'Error']
            },
            'Creates list of users with given input array.': {
                DataMovementType.ENTRY: ['User'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['User', 'Error']
            },
            'Delete purchase order by identifier.': {
                DataMovementType.ENTRY: ['UNKNOWN'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Delete user resource.': {
                DataMovementType.ENTRY: ['User'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Deletes a pet.': {
                DataMovementType.ENTRY: ['Order'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Update an existing pet.': {
                DataMovementType.ENTRY: ['Category', 'Pet', 'Tag'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Category', 'Pet', 'Tag', 'Error']
            },
            'Finds Pets by status.': {
                DataMovementType.ENTRY: ['Order', 'Pet'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Category', 'Pet', 'Tag', 'Error']
            },
            'Finds Pets by tags.': {
                DataMovementType.ENTRY: ['Pet'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Category', 'Pet', 'Tag', 'Error']
            },
            'Find pet by ID.': {
                DataMovementType.ENTRY: ['Order'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Category', 'Pet', 'Tag', 'Error']
            },
            'Updates a pet in the store with form data.': {
                DataMovementType.ENTRY: ['Category', 'Order', 'Pet', 'Tag'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Category', 'Pet', 'Tag', 'Error']
            },
            'Find purchase order by ID.': {
                DataMovementType.ENTRY: ['UNKNOWN'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Order', 'Error']
            },
            'Get user by user name.': {
                DataMovementType.ENTRY: ['User'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['User', 'Error']
            },
            'Logs out current logged in user session.': {
                DataMovementType.ENTRY: ['UNKNOWN'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Logs user into the system.': {
                DataMovementType.ENTRY: ['User'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Place an order for a pet.': {
                DataMovementType.ENTRY: ['Order'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Order', 'Error']
            },
            'Returns pet inventories by status.': {
                DataMovementType.ENTRY: ['UNKNOWN'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Update user resource.': {
                DataMovementType.ENTRY: ['User'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['Error']
            },
            'Uploads an image.': {
                DataMovementType.ENTRY: ['Order', 'UNKNOWN'],
                DataMovementType.READ: [],
                DataMovementType.WRITE: [],
                DataMovementType.EXIT: ['ApiResponse', 'Error']
            }
        }
    fpc = fpc.FunctionPointsCalculator(movement_types)
    fpid1 = "Update an existing pet."
    fpid2 = "Add a new pet to the store."
    fpid3 = "Finds Pets by status."

    def test_calculate_entry_count(self):
        self.assertEqual(3, self.fpc.calculate_entry_count(self.fpid1))
        self.assertEqual(3, self.fpc.calculate_entry_count(self.fpid2))
        self.assertEqual(2, self.fpc.calculate_entry_count(self.fpid3))           

    def test_calculate_read_count(self):
        self.assertEqual(0, self.fpc.calculate_read_count(self.fpid1))
        self.assertEqual(0, self.fpc.calculate_read_count(self.fpid2))
        self.assertEqual(0, self.fpc.calculate_read_count(self.fpid3))    

    def test_calculate_write_count(self):
        self.assertEqual(0, self.fpc.calculate_write_count(self.fpid1))
        self.assertEqual(0, self.fpc.calculate_write_count(self.fpid2))
        self.assertEqual(0, self.fpc.calculate_write_count(self.fpid3))

    def test_calculate_exit_count(self):
        self.assertEqual(4, self.fpc.calculate_exit_count(self.fpid1))
        self.assertEqual(4, self.fpc.calculate_exit_count(self.fpid2))
        self.assertEqual(4, self.fpc.calculate_exit_count(self.fpid3))
   
    def test_calculate_total_count(self):
        self.assertEqual(7, self.fpc.calculate_total_count(self.fpid1))
        self.assertEqual(7, self.fpc.calculate_total_count(self.fpid2))
        self.assertEqual(6, self.fpc.calculate_total_count(self.fpid3))

    def test_calculate_total_per_spec(self):
        self.assertEqual(71, self.fpc.calculate_total_per_spec(self.movement_types))

