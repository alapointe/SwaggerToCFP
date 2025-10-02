import unittest
from src.basic_definitions.data import DataMovementType
from src.extraction.HTTPVerbExtractor import HTTPVerbExtractor
from test.helpers.CalculationSpecificationFileTest import CalculationSpecificationFileTest
from src.DatagroupIdentifier import DataGroupIdentifier
import src.function_points_processing.MovementTypeIdentifier as mti
import src.extraction.Extractor as extractor
from test.helpers.helpers import Helpers

class Test_MovementTypeIdentifier(CalculationSpecificationFileTest):

    def setUp(self) -> None:
        self.extractor = extractor.Extractor('./test/testdata/swagger_pet_store.yml')
        self.dgi = DataGroupIdentifier
        self.mti = mti.MovementTypeIdentifier()
        return super().setUp()
    
    def test_get_movement_types(self):
        entries = {
            'Add a new pet to the store.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Create user.': {DataMovementType.ENTRY : ['User']},
            'Creates list of users with given input array.': {DataMovementType.ENTRY : ['User']},
            'Delete purchase order by identifier.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Delete user resource.': {DataMovementType.ENTRY : ['User']},
            'Deletes a pet.': {DataMovementType.ENTRY : ['Order']}, 
            'Find pet by ID.': {DataMovementType.ENTRY : ['Order']},
            'Find purchase order by ID.': {DataMovementType.ENTRY : ['UNKNOWN']}, 
            'Finds Pets by status.': {DataMovementType.ENTRY : ['Order','Pet']},
            'Finds Pets by tags.': {DataMovementType.ENTRY : ['Pet']},
            'Get user by user name.': {DataMovementType.ENTRY : ['User']},
            'Logs out current logged in user session.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Logs user into the system.': {DataMovementType.ENTRY : ['User']},
            'Place an order for a pet.': {DataMovementType.ENTRY : ['Order']},
            'Returns pet inventories by status.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Update an existing pet.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Update user resource.': {DataMovementType.ENTRY : ['User']}, 
            'Updates a pet in the store with form data.': {DataMovementType.ENTRY : ['Category','Order','Pet','Tag']}, 
            'Uploads an image.': {DataMovementType.ENTRY : ['Order', 'UNKNOWN']}
            }
        reads = {
            'Add a new pet to the store.': {DataMovementType.READ : []}, 
            'Create user.': {DataMovementType.READ : []},
            'Creates list of users with given input array.': {DataMovementType.READ : []},
            'Delete purchase order by identifier.': {DataMovementType.READ : []},
            'Delete user resource.': {DataMovementType.READ : []},
            'Deletes a pet.': {DataMovementType.READ : []}, 
            'Find pet by ID.': {DataMovementType.READ : []},
            'Find purchase order by ID.': {DataMovementType.READ : []}, 
            'Finds Pets by status.': {DataMovementType.READ : []},
            'Finds Pets by tags.': {DataMovementType.READ : []},
            'Get user by user name.': {DataMovementType.READ : []},
            'Logs out current logged in user session.': {DataMovementType.READ : []},
            'Logs user into the system.': {DataMovementType.READ : []},
            'Place an order for a pet.': {DataMovementType.READ : []},
            'Returns pet inventories by status.': {DataMovementType.READ : []},
            'Update an existing pet.': {DataMovementType.READ : []}, 
            'Update user resource.': {DataMovementType.READ : []}, 
            'Updates a pet in the store with form data.': {DataMovementType.READ : []}, 
            'Uploads an image.': {DataMovementType.ENTRY : []}
            }
        writes = {
            'Add a new pet to the store.': {DataMovementType.WRITE : []}, 
            'Create user.': {DataMovementType.WRITE : []},
            'Creates list of users with given input array.': {DataMovementType.WRITE : []},
            'Delete purchase order by identifier.': {DataMovementType.WRITE : []},
            'Delete user resource.': {DataMovementType.WRITE : []},
            'Deletes a pet.': {DataMovementType.WRITE : []}, 
            'Find pet by ID.': {DataMovementType.WRITE : []},
            'Find purchase order by ID.': {DataMovementType.WRITE : []}, 
            'Finds Pets by status.': {DataMovementType.WRITE : []},
            'Finds Pets by tags.': {DataMovementType.WRITE : []},
            'Get user by user name.': {DataMovementType.WRITE : []},
            'Logs out current logged in user session.': {DataMovementType.WRITE : []},
            'Logs user into the system.': {DataMovementType.WRITE : []},
            'Place an order for a pet.': {DataMovementType.WRITE : []},
            'Returns pet inventories by status.': {DataMovementType.WRITE : []},
            'Update an existing pet.': {DataMovementType.WRITE : []}, 
            'Update user resource.': {DataMovementType.WRITE : []}, 
            'Updates a pet in the store with form data.': {DataMovementType.WRITE : []}, 
            'Uploads an image.': {DataMovementType.WRITE : []}
            }
        exits = {
            'Update an existing pet.': {DataMovementType.EXIT : ['Category', 'Pet', 'Tag', 'Error']},             
            'Add a new pet to the store.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Finds Pets by status.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Finds Pets by tags.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Find pet by ID.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Updates a pet in the store with form data.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']}, 
            'Create user.': {DataMovementType.EXIT : ['User', 'Error']},
            'Creates list of users with given input array.': {DataMovementType.EXIT : ['User', 'Error']},
            'Delete purchase order by identifier.': {DataMovementType.EXIT : ['Error']},
            'Delete user resource.': {DataMovementType.EXIT : ['Error']},
            'Deletes a pet.': {DataMovementType.EXIT : ['Error']}, 
            'Find purchase order by ID.': {DataMovementType.EXIT : ['Order', 'Error']}, 
            'Get user by user name.': {DataMovementType.EXIT : ['User', 'Error']},
            'Logs out current logged in user session.': {DataMovementType.EXIT : ['Error']},
            'Logs user into the system.': {DataMovementType.EXIT : ['Error']},
            'Place an order for a pet.': {DataMovementType.EXIT : ['Order', 'Error']},
            'Returns pet inventories by status.': {DataMovementType.EXIT : ['Error']},
            'Update user resource.': {DataMovementType.EXIT : ['Error']}, 
            'Uploads an image.': {DataMovementType.EXIT : ['ApiResponse', 'Error']}
            }   
        expected_movement_types = {
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
        self.assertEqual(Helpers.sort_dict_by_keys(self.mti.get_movement_types(entries, reads, writes, exits)), Helpers.sort_dict_by_keys(expected_movement_types))


    def test_aggregate_movement_types(self):
        entries = {
            'Add a new pet to the store.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Create user.': {DataMovementType.ENTRY : ['User']},
            'Creates list of users with given input array.': {DataMovementType.ENTRY : ['User']},
            'Delete purchase order by identifier.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Delete user resource.': {DataMovementType.ENTRY : ['User']},
            'Deletes a pet.': {DataMovementType.ENTRY : ['Order']}, 
            'Find pet by ID.': {DataMovementType.ENTRY : ['Order']},
            'Find purchase order by ID.': {DataMovementType.ENTRY : ['UNKNOWN']}, 
            'Finds Pets by status.': {DataMovementType.ENTRY : ['Order','Pet']},
            'Finds Pets by tags.': {DataMovementType.ENTRY : ['Pet']},
            'Get user by user name.': {DataMovementType.ENTRY : ['User']},
            'Logs out current logged in user session.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Logs user into the system.': {DataMovementType.ENTRY : ['User']},
            'Place an order for a pet.': {DataMovementType.ENTRY : ['Order']},
            'Returns pet inventories by status.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Update an existing pet.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Update user resource.': {DataMovementType.ENTRY : ['User']}, 
            'Updates a pet in the store with form data.': {DataMovementType.ENTRY : ['Category','Order','Pet','Tag']}, 
            'Uploads an image.': {DataMovementType.ENTRY : ['Order', 'UNKNOWN']}
            }
        reads = {
            'Add a new pet to the store.': {DataMovementType.READ : []}, 
            'Create user.': {DataMovementType.READ : []},
            'Creates list of users with given input array.': {DataMovementType.READ : []},
            'Delete purchase order by identifier.': {DataMovementType.READ : []},
            'Delete user resource.': {DataMovementType.READ : []},
            'Deletes a pet.': {DataMovementType.READ : []}, 
            'Find pet by ID.': {DataMovementType.READ : []},
            'Find purchase order by ID.': {DataMovementType.READ : []}, 
            'Finds Pets by status.': {DataMovementType.READ : []},
            'Finds Pets by tags.': {DataMovementType.READ : []},
            'Get user by user name.': {DataMovementType.READ : []},
            'Logs out current logged in user session.': {DataMovementType.READ : []},
            'Logs user into the system.': {DataMovementType.READ : []},
            'Place an order for a pet.': {DataMovementType.READ : []},
            'Returns pet inventories by status.': {DataMovementType.READ : []},
            'Update an existing pet.': {DataMovementType.READ : []}, 
            'Update user resource.': {DataMovementType.READ : []}, 
            'Updates a pet in the store with form data.': {DataMovementType.READ : []}, 
            'Uploads an image.': {DataMovementType.ENTRY : []}
            }
        writes = {
            'Add a new pet to the store.': {DataMovementType.WRITE : []}, 
            'Create user.': {DataMovementType.WRITE : []},
            'Creates list of users with given input array.': {DataMovementType.WRITE : []},
            'Delete purchase order by identifier.': {DataMovementType.WRITE : []},
            'Delete user resource.': {DataMovementType.WRITE : []},
            'Deletes a pet.': {DataMovementType.WRITE : []}, 
            'Find pet by ID.': {DataMovementType.WRITE : []},
            'Find purchase order by ID.': {DataMovementType.WRITE : []}, 
            'Finds Pets by status.': {DataMovementType.WRITE : []},
            'Finds Pets by tags.': {DataMovementType.WRITE : []},
            'Get user by user name.': {DataMovementType.WRITE : []},
            'Logs out current logged in user session.': {DataMovementType.WRITE : []},
            'Logs user into the system.': {DataMovementType.WRITE : []},
            'Place an order for a pet.': {DataMovementType.WRITE : []},
            'Returns pet inventories by status.': {DataMovementType.WRITE : []},
            'Update an existing pet.': {DataMovementType.WRITE : []}, 
            'Update user resource.': {DataMovementType.WRITE : []}, 
            'Updates a pet in the store with form data.': {DataMovementType.WRITE : []}, 
            'Uploads an image.': {DataMovementType.WRITE : []}
            }
        exits = {
            'Update an existing pet.': {DataMovementType.EXIT : ['Category', 'Pet', 'Tag', 'Error']},             
            'Add a new pet to the store.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Finds Pets by status.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Finds Pets by tags.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Find pet by ID.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Updates a pet in the store with form data.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']}, 
            'Create user.': {DataMovementType.EXIT : ['User', 'Error']},
            'Creates list of users with given input array.': {DataMovementType.EXIT : ['User', 'Error']},
            'Delete purchase order by identifier.': {DataMovementType.EXIT : ['Error']},
            'Delete user resource.': {DataMovementType.EXIT : ['Error']},
            'Deletes a pet.': {DataMovementType.EXIT : ['Error']}, 
            'Find purchase order by ID.': {DataMovementType.EXIT : ['Order', 'Error']}, 
            'Get user by user name.': {DataMovementType.EXIT : ['User', 'Error']},
            'Logs out current logged in user session.': {DataMovementType.EXIT : ['Error']},
            'Logs user into the system.': {DataMovementType.EXIT : ['Error']},
            'Place an order for a pet.': {DataMovementType.EXIT : ['Order', 'Error']},
            'Returns pet inventories by status.': {DataMovementType.EXIT : ['Error']},
            'Update user resource.': {DataMovementType.EXIT : ['Error']}, 
            'Uploads an image.': {DataMovementType.EXIT : ['ApiResponse', 'Error']}
            }   
        expected_movement_types = {
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
        self.assertEqual(Helpers.sort_dict_by_value(expected_movement_types), Helpers.sort_dict_by_value(self.mti.aggregate_movement_types(entries, reads, writes, exits)))

    def test_identify_entries(self):
        data_model = {
            "Order": {
                "id": {"type": "properties"},
                "petId": {"type": "properties"},
                "quantity": {"type": "properties"},
                "shipDate": {"type": "properties"},
                "status": {"type": "properties"},
                "complete": {"type": "properties"}
            },
            "Category": {
                "id": {"type": "properties"},
                "name": {"type": "properties"}
            },
            "User": {
                "id": {"type": "properties"},
                "username": {"type": "properties"},
                "firstName": {"type": "properties"},
                "lastName": {"type": "properties"},
                "email": {"type": "properties"},
                "password": {"type": "properties"},
                "phone": {"type": "properties"},
                "userStatus": {"type": "properties"}
            },
            "Tag": {
                "id": {"type": "properties"},
                "name": {"type": "properties"}
            },
            "Pet": {
                "id": {"type": "properties"},
                "name": {"type": "properties"},
                "category": {"type": "object", "ref": "Category"},
                "photoUrls": {"type": "array", "items": {"type": "properties"}},
                "tags": {"type": "array", "items": {"type": "object", "ref": "Tag"}},
                "status": {"type": "properties"}
            },
            "ApiResponse": {
                "code": {"type": "properties"},
                "type": {"type": "properties"},
                "message": {"type": "properties"}
            },
            "Error": {
                "code": {"type": "properties"},
                "message": {"type": "properties"}
            }
        }
        request_body = {
            'Add a new pet to the store.': {'Datagroups': ['Category','Pet','Tag']}, 
            'Create user.': {'Datagroups': ['User']}, 
            'Creates list of users with given input array.': {'Datagroups': ['User']}, 
            'Delete purchase order by identifier.': {}, 
            'Delete user resource.': {}, 
            'Deletes a pet.': {}, 
            'Find pet by ID.': {}, 
            'Find purchase order by ID.': {}, 
            'Finds Pets by status.': {}, 
            'Finds Pets by tags.': {}, 
            'Get user by user name.': {}, 
            'Logs out current logged in user session.': {}, 
            'Logs user into the system.': {}, 
            'Place an order for a pet.': {'Datagroups': ['Order']}, 
            'Returns pet inventories by status.': {}, 
            'Update an existing pet.': {'Datagroups': ['Category','Pet','Tag']}, 
            'Update user resource.': {'Datagroups': ['User']}, 
            'Updates a pet in the store with form data.': {}, 
            'Uploads an image.': {'Datagroups': ['UNKNOWN']}
            }
        parameters_datagroups = {
            'Add a new pet to the store.': [], 
            'Create user.': [], 
            'Creates list of users with given input array.': [], 
            'Delete purchase order by identifier.': [], 
            'Delete user resource.': ['User'], 
            'Deletes a pet.': ['Order'], 
            'Find pet by ID.': ['Order'], 
            'Find purchase order by ID.': [], 
            'Finds Pets by status.': ['Pet', 'Order'], 
            'Finds Pets by tags.': ['Pet'], 
            'Get user by user name.': ['User'], 
            'Logs out current logged in user session.': [], 
            'Logs user into the system.': ['User'], 
            'Place an order for a pet.': [], 
            'Returns pet inventories by status.': [], 
            'Update an existing pet.': [], 
            'Update user resource.': ['User'], 
            'Updates a pet in the store with form data.': ['Pet', 'Order', 'Tag', 'Category'], 
            'Uploads an image.': ['Order']
            }
        expected_entries = {
            'Add a new pet to the store.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Create user.': {DataMovementType.ENTRY : ['User']},
            'Creates list of users with given input array.': {DataMovementType.ENTRY : ['User']},
            'Delete purchase order by identifier.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Delete user resource.': {DataMovementType.ENTRY : ['User']},
            'Deletes a pet.': {DataMovementType.ENTRY : ['Order']}, 
            'Find pet by ID.': {DataMovementType.ENTRY : ['Order']},
            'Find purchase order by ID.': {DataMovementType.ENTRY : ['UNKNOWN']}, 
            'Finds Pets by status.': {DataMovementType.ENTRY : ['Order','Pet']},
            'Finds Pets by tags.': {DataMovementType.ENTRY : ['Pet']},
            'Get user by user name.': {DataMovementType.ENTRY : ['User']},
            'Logs out current logged in user session.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Logs user into the system.': {DataMovementType.ENTRY : ['User']},
            'Place an order for a pet.': {DataMovementType.ENTRY : ['Order']},
            'Returns pet inventories by status.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Update an existing pet.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Update user resource.': {DataMovementType.ENTRY : ['User']}, 
            'Updates a pet in the store with form data.': {DataMovementType.ENTRY : ['Category','Order','Pet','Tag']}, 
            'Uploads an image.': {DataMovementType.ENTRY : ['Order', 'UNKNOWN']}
            }
        self.assertEqual(Helpers.sort_dict_by_keys_extended(self.mti.identify_entries(request_body, parameters_datagroups, data_model)), Helpers.sort_dict_by_keys_extended(expected_entries))

    def test_param_in_properties(self):
        data_model = {'Order': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'petId': {'type': 'integer', 'format': 'int64', 'example': 198772}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 7}, 'shipDate': {'type': 'string', 'format': 'date-time'}, 'status': {'type': 'string', 'description': 'Order Status', 'example': 'approved', 'enum': ['placed', 'approved', 'delivered']}, 'complete': {'type': 'boolean'}}, 'xml': {'name': 'order'}}, 'Category': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 1}, 'name': {'type': 'string', 'example': 'Dogs'}}, 'xml': {'name': 'category'}}, 'User': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'username': {'type': 'string', 'example': 'theUser'}, 'firstName': {'type': 'string', 'example': 'John'}, 'lastName': {'type': 'string', 'example': 'James'}, 'email': {'type': 'string', 'example': 'john@email.com'}, 'password': {'type': 'string', 'example': '12345'}, 'phone': {'type': 'string', 'example': '12345'}, 'userStatus': {'type': 'integer', 'description': 'User Status', 'format': 'int32', 'example': 1}}, 'xml': {'name': 'user'}}, 'Tag': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'tag'}}, 'Pet': {'required': ['name', 'photoUrls'], 'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'name': {'type': 'string', 'example': 'doggie'}, 'category': {'$ref': '#/components/schemas/Category'}, 'photoUrls': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'type': 'string', 'xml': {'name': 'photoUrl'}}}, 'tags': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'$ref': '#/components/schemas/Tag'}}, 'status': {'type': 'string', 'description': 'pet status in the store', 'enum': ['available', 'pending', 'sold']}}, 'xml': {'name': 'pet'}}, 'ApiResponse': {'type': 'object', 'properties': {'code': {'type': 'integer', 'format': 'int32'}, 'type': {'type': 'string'}, 'message': {'type': 'string'}}, 'xml': {'name': '##default'}}, 'Error': {'type': 'object', 'properties': {'code': {'type': 'string'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}
        param = 'id'
        self.assertTrue(self.mti.param_in_properties(param, data_model))

    def test_find_parent_group(self):
        data_model = {'Order': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'petId': {'type': 'integer', 'format': 'int64', 'example': 198772}, 'quantity': {'type': 'integer', 'format': 'int32', 'example': 7}, 'shipDate': {'type': 'string', 'format': 'date-time'}, 'status': {'type': 'string', 'description': 'Order Status', 'example': 'approved', 'enum': ['placed', 'approved', 'delivered']}, 'complete': {'type': 'boolean'}}, 'xml': {'name': 'order'}}, 'Category': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 1}, 'name': {'type': 'string', 'example': 'Dogs'}}, 'xml': {'name': 'category'}}, 'User': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'username': {'type': 'string', 'example': 'theUser'}, 'firstName': {'type': 'string', 'example': 'John'}, 'lastName': {'type': 'string', 'example': 'James'}, 'email': {'type': 'string', 'example': 'john@email.com'}, 'password': {'type': 'string', 'example': '12345'}, 'phone': {'type': 'string', 'example': '12345'}, 'userStatus': {'type': 'integer', 'description': 'User Status', 'format': 'int32', 'example': 1}}, 'xml': {'name': 'user'}}, 'Tag': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'tag'}}, 'Pet': {'required': ['name', 'photoUrls'], 'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64', 'example': 10}, 'name': {'type': 'string', 'example': 'doggie'}, 'category': {'$ref': '#/components/schemas/Category'}, 'photoUrls': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'type': 'string', 'xml': {'name': 'photoUrl'}}}, 'tags': {'type': 'array', 'xml': {'wrapped': True}, 'items': {'$ref': '#/components/schemas/Tag'}}, 'status': {'type': 'string', 'description': 'pet status in the store', 'enum': ['available', 'pending', 'sold']}}, 'xml': {'name': 'pet'}}, 'ApiResponse': {'type': 'object', 'properties': {'code': {'type': 'integer', 'format': 'int32'}, 'type': {'type': 'string'}, 'message': {'type': 'string'}}, 'xml': {'name': '##default'}}, 'Error': {'type': 'object', 'properties': {'code': {'type': 'string'}, 'message': {'type': 'string'}}, 'required': ['code', 'message']}}
        param = 'id'
        self.assertEqual(self.mti.find_parent_group(param, data_model), 'Order')

    def test_identify_reads(self):
        parameters_datagroups = {
            'Add a new pet to the store.': [], 
            'Create user.': [], 
            'Creates list of users with given input array.': [], 
            'Delete purchase order by identifier.': [], 'Delete user resource.': ['User'], 
            'Deletes a pet.': ['Order'], 
            'Find pet by ID.': ['Order'], 
            'Find purchase order by ID.': [], 
            'Finds Pets by status.': ['Order', 'Pet'], 
            'Finds Pets by tags.': ['Pet'], 
            'Get user by user name.': ['User'], 
            'Logs user into the system.': ['User', 'User'],
            'Logs out current logged in user session.': ['UNKNOWN'],
            'Place an order for a pet.': [], 
            'Returns pet inventories by status.': [], 
            'Update an existing pet.': [], 
            'Update user resource.': ['User'], 
            'Updates a pet in the store with form data.': ['Order', 'Category', 'Tag', 'Pet', 'Order', 'Pet'], 
            'Uploads an image.': ['Order']
            }     
        expected_reads = {
            'Add a new pet to the store.': {DataMovementType.READ : []}, 
            'Create user.': {DataMovementType.READ : []},
            'Creates list of users with given input array.': {DataMovementType.READ : []},
            'Delete purchase order by identifier.': {DataMovementType.READ : []},
            'Delete user resource.': {DataMovementType.READ : []},
            'Deletes a pet.': {DataMovementType.READ : []}, 
            'Find pet by ID.': {DataMovementType.READ : []},
            'Find purchase order by ID.': {DataMovementType.READ : []}, 
            'Finds Pets by status.': {DataMovementType.READ : []},
            'Finds Pets by tags.': {DataMovementType.READ : []},
            'Get user by user name.': {DataMovementType.READ : []},
            'Logs out current logged in user session.': {DataMovementType.READ : []},
            'Logs user into the system.': {DataMovementType.READ : []},
            'Place an order for a pet.': {DataMovementType.READ : []},
            'Returns pet inventories by status.': {DataMovementType.READ : []},
            'Update an existing pet.': {DataMovementType.READ : []}, 
            'Update user resource.': {DataMovementType.READ : []}, 
            'Updates a pet in the store with form data.': {DataMovementType.READ : []}, 
            'Uploads an image.': {DataMovementType.READ : []}
            }
        self.assertEqual(Helpers.sort_dict_by_keys_extended(self.mti.identify_reads(parameters_datagroups)), Helpers.sort_dict_by_keys_extended(expected_reads))

    def test_identify_writes(self):
        parameters_datagroups = {
            'Add a new pet to the store.': [], 
            'Create user.': [], 
            'Creates list of users with given input array.': [], 
            'Delete purchase order by identifier.': [], 'Delete user resource.': ['User'], 
            'Deletes a pet.': ['Order'], 
            'Find pet by ID.': ['Order'], 
            'Find purchase order by ID.': [], 
            'Finds Pets by status.': ['Order', 'Pet'], 
            'Finds Pets by tags.': ['Pet'], 
            'Get user by user name.': ['User'], 
            'Logs user into the system.': ['User', 'User'],
            'Logs out current logged in user session.': ['UNKNOWN'],
            'Place an order for a pet.': [], 
            'Returns pet inventories by status.': [], 
            'Update an existing pet.': [], 
            'Update user resource.': ['User'], 
            'Updates a pet in the store with form data.': ['Order', 'Category', 'Tag', 'Pet', 'Order', 'Pet'], 
            'Uploads an image.': ['Order']
            }
        expected_writes = {
            'Add a new pet to the store.': {DataMovementType.WRITE : []}, 
            'Create user.': {DataMovementType.WRITE : []},
            'Creates list of users with given input array.': {DataMovementType.WRITE : []},
            'Delete purchase order by identifier.': {DataMovementType.WRITE : []},
            'Delete user resource.': {DataMovementType.WRITE : []},
            'Deletes a pet.': {DataMovementType.WRITE : []}, 
            'Find pet by ID.': {DataMovementType.WRITE : []},
            'Find purchase order by ID.': {DataMovementType.WRITE : []}, 
            'Finds Pets by status.': {DataMovementType.WRITE : []},
            'Finds Pets by tags.': {DataMovementType.WRITE : []},
            'Get user by user name.': {DataMovementType.WRITE : []},
            'Logs out current logged in user session.': {DataMovementType.WRITE : []},
            'Logs user into the system.': {DataMovementType.WRITE : []},
            'Place an order for a pet.': {DataMovementType.WRITE : []},
            'Returns pet inventories by status.': {DataMovementType.WRITE : []},
            'Update an existing pet.': {DataMovementType.WRITE : []}, 
            'Update user resource.': {DataMovementType.WRITE : []}, 
            'Updates a pet in the store with form data.': {DataMovementType.WRITE : []}, 
            'Uploads an image.': {DataMovementType.WRITE : []}
            }
        self.assertEqual(Helpers.sort_dict_by_keys(self.mti.identify_writes(parameters_datagroups)), Helpers.sort_dict_by_keys(expected_writes))

    def test_identify_exits(self):
        responses_datagroups = {
            'Update an existing pet.': ['Category','Pet','Tag', 'Error'], 
            'Add a new pet to the store.': ['Category','Pet','Tag', 'Error'], 
            'Finds Pets by status.': ['Category','Pet','Tag', 'Error'], 
            'Finds Pets by tags.': ['Category','Pet','Tag', 'Error'], 
            'Find pet by ID.': ['Category','Pet','Tag', 'Error'], 
            'Updates a pet in the store with form data.': ['Category','Pet','Tag', 'Error'], 
            'Deletes a pet.': ['Error'], 
            'Uploads an image.': ['ApiResponse', 'Error'], 
            'Returns pet inventories by status.': ['Error'], 
            'Place an order for a pet.': ['Order', 'Error'], 
            'Find purchase order by ID.': ['Order', 'Error'], 
            'Delete purchase order by identifier.': ['Error'], 
            'Create user.': ['User', 'Error'], 
            'Creates list of users with given input array.': ['User', 'Error'], 
            'Logs user into the system.': ['Error'], 
            'Logs out current logged in user session.': ['Error'], 
            'Get user by user name.': ['User', 'Error'], 
            'Update user resource.': ['Error'], 
            'Delete user resource.': ['Error']
            } 
        expected_exits = {
            'Update an existing pet.': {DataMovementType.EXIT : ['Category', 'Pet', 'Tag', 'Error']},             
            'Add a new pet to the store.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Finds Pets by status.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Finds Pets by tags.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Find pet by ID.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']},
            'Updates a pet in the store with form data.': {DataMovementType.EXIT : ['Category','Pet','Tag', 'Error']}, 
            'Create user.': {DataMovementType.EXIT : ['User', 'Error']},
            'Creates list of users with given input array.': {DataMovementType.EXIT : ['User', 'Error']},
            'Delete purchase order by identifier.': {DataMovementType.EXIT : ['Error']},
            'Delete user resource.': {DataMovementType.EXIT : ['Error']},
            'Deletes a pet.': {DataMovementType.EXIT : ['Error']}, 
            'Find purchase order by ID.': {DataMovementType.EXIT : ['Order', 'Error']}, 
            'Get user by user name.': {DataMovementType.EXIT : ['User', 'Error']},
            'Logs out current logged in user session.': {DataMovementType.EXIT : ['Error']},
            'Logs user into the system.': {DataMovementType.EXIT : ['Error']},
            'Place an order for a pet.': {DataMovementType.EXIT : ['Order', 'Error']},
            'Returns pet inventories by status.': {DataMovementType.EXIT : ['Error']},
            'Update user resource.': {DataMovementType.EXIT : ['Error']}, 
            'Uploads an image.': {DataMovementType.EXIT : ['ApiResponse', 'Error']}
            }
        self.assertEqual(Helpers.sort_dict_by_keys(self.mti.identify_exits(self.mti, responses_datagroups)), Helpers.sort_dict_by_keys(expected_exits))

    def test_identify_exits_when_no_schema(self):
        responses_datagroups = {
            'Update an existing pet.': ['Pet', 'Error'], 
            'Add a new pet to the store.': ['Pet', 'Error'], 
            'Finds Pets by status.': ['Pet', 'Error'], 
            'Finds Pets by tags.': ['Pet', 'Error'], 
            'Find pet by ID.': ['Pet', 'Error'], 
            'Updates a pet in the store with form data.': ['Pet', 'Error'], 
            'Deletes a pet.': ['Error'], 
            'Uploads an image.': ['ApiResponse', 'Error'], 
            'Returns pet inventories by status.': ['Error'], 
            'Place an order for a pet.': ['Order', 'Error'], 
            'Find purchase order by ID.': ['Order', 'Error'], 
            'Delete purchase order by identifier.': ['Error'], 
            'Create user.': ['User', 'Error'], 
            'Creates list of users with given input array.': ['User', 'Error'], 
            'Logs user into the system.': ['Error'], 
            'Logs out current logged in user session.': ['Error'], 
            'Get user by user name.': ['User', 'Error'], 
            'Update user resource.': ['Error'], 
            'Delete user resource.': ['Error']
            }
        expected_exits = {'Update an existing pet.': {DataMovementType.EXIT : ['Pet', 'Error']}, 'Add a new pet to the store.': {DataMovementType.EXIT : ['Pet', 'Error']}, 'Finds Pets by status.': {DataMovementType.EXIT : ['Pet', 'Error']}, 'Finds Pets by tags.': {DataMovementType.EXIT : ['Pet', 'Error']}, 'Find pet by ID.': {DataMovementType.EXIT : ['Pet', 'Error']}, 'Updates a pet in the store with form data.': {DataMovementType.EXIT : ['Pet', 'Error']}, 'Deletes a pet.': {DataMovementType.EXIT : ['Error']}, 'Uploads an image.': {DataMovementType.EXIT : ['ApiResponse', 'Error']}, 'Returns pet inventories by status.': {DataMovementType.EXIT : ['Error']}, 'Place an order for a pet.': {DataMovementType.EXIT : ['Order', 'Error']}, 'Find purchase order by ID.': {DataMovementType.EXIT : ['Order', 'Error']}, 'Delete purchase order by identifier.': {DataMovementType.EXIT : ['Error']}, 'Create user.': {DataMovementType.EXIT : ['User', 'Error']}, 'Creates list of users with given input array.': {DataMovementType.EXIT : ['User', 'Error']}, 'Logs user into the system.': {DataMovementType.EXIT : ['Error']}, 'Logs out current logged in user session.': {DataMovementType.EXIT : ['Error']}, 'Get user by user name.': {DataMovementType.EXIT : ['User', 'Error']}, 'Update user resource.': {DataMovementType.EXIT : ['Error']}, 'Delete user resource.': {DataMovementType.EXIT : ['Error']}}
        
        self.assertEqual(self.mti.identify_exits(self.mti, responses_datagroups), expected_exits)
    
    def test_transform_entries_to_reads(self):
        entries = {
            'Add a new pet to the store.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Create user.': {DataMovementType.ENTRY : ['User']},
            'Creates list of users with given input array.': {DataMovementType.ENTRY : ['User']},
            'Delete purchase order by identifier.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Delete user resource.': {DataMovementType.ENTRY : ['User']},
            'Deletes a pet.': {DataMovementType.ENTRY : ['Order']}, 
            'Find pet by ID.': {DataMovementType.ENTRY : ['Order']},
            'Find purchase order by ID.': {DataMovementType.ENTRY : ['UNKNOWN']}, 
            'Finds Pets by status.': {DataMovementType.ENTRY : ['Order','Pet']},
            'Finds Pets by tags.': {DataMovementType.ENTRY : ['Pet']},
            'Get user by user name.': {DataMovementType.ENTRY : ['User']},
            'Logs out current logged in user session.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Logs user into the system.': {DataMovementType.ENTRY : ['User']},
            'Place an order for a pet.': {DataMovementType.ENTRY : ['Order']},
            'Returns pet inventories by status.': {DataMovementType.ENTRY : ['UNKNOWN']},
            'Update an existing pet.': {DataMovementType.ENTRY : ['Category','Pet','Tag']}, 
            'Update user resource.': {DataMovementType.ENTRY : ['User']}, 
            'Updates a pet in the store with form data.': {DataMovementType.ENTRY : ['Category','Order','Pet','Tag']}, 
            'Uploads an image.': {DataMovementType.ENTRY : ['Order', 'UNKNOWN']}
            }
        expected_reads = {
            'Add a new pet to the store.': {DataMovementType.READ : ['Category','Pet','Tag']}, 
            'Create user.': {DataMovementType.READ : ['User']},
            'Creates list of users with given input array.': {DataMovementType.READ : ['User']},
            'Delete purchase order by identifier.': {DataMovementType.READ : ['UNKNOWN']},
            'Delete user resource.': {DataMovementType.READ : ['User']},
            'Deletes a pet.': {DataMovementType.READ : ['Order']}, 
            'Find pet by ID.': {DataMovementType.READ : ['Order']},
            'Find purchase order by ID.': {DataMovementType.READ : ['UNKNOWN']}, 
            'Finds Pets by status.': {DataMovementType.READ : ['Order','Pet']},
            'Finds Pets by tags.': {DataMovementType.READ : ['Pet']},
            'Get user by user name.': {DataMovementType.READ : ['User']},
            'Logs out current logged in user session.': {DataMovementType.READ : ['UNKNOWN']},
            'Logs user into the system.': {DataMovementType.READ : ['User']},
            'Place an order for a pet.': {DataMovementType.READ : ['Order']},
            'Returns pet inventories by status.': {DataMovementType.READ : ['UNKNOWN']},
            'Update an existing pet.': {DataMovementType.READ : ['Category','Pet','Tag']}, 
            'Update user resource.': {DataMovementType.READ : ['User']}, 
            'Updates a pet in the store with form data.': {DataMovementType.READ : ['Category','Order','Pet','Tag']}, 
            'Uploads an image.': {DataMovementType.ENTRY : ['Order', 'UNKNOWN']}
            }
        self.assertEqual(self.mti.transform_entries_to_reads(entries), expected_reads)
