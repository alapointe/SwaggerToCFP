import unittest   # The test framework
from src.basic_definitions import data
from src.basic_definitions.api_context import APIContext
from src.basic_definitions.data import DataMovementType, CRUD
from src.extraction import DataGroupExtractor as dge
from src.aggregator import Aggregator
from src.function_points_processing.MovementTypeIdentifier import MovementTypeIdentifier
import src.function_points_processing.FunctionPointsCalculator as fpc
import src.extraction.Extractor as ext # type: ignore
from src.CRUDIdentifier import CRUDIdentifier
from src.functionalProcess import FunctionalProcess as fp
from src.DatagroupIdentifier import DataGroupIdentifier
import src.extraction.HTTPVerbExtractor as hve

from test.helpers.FakeExtractor import FakeExtractor
from test.helpers.FakeFunctionPointCalculator import FakeFunctionPointsCalculator


from src.report_generation.ReportGenerator import ReportGenerator
from src.extraction.DataGroupExtractor import DataGroupExtractor
from test.helpers import FakeAggregator


class Test_Aggregator(unittest.TestCase):
    pf_rows = []
    spec_path = './test/testdata/swagger_pet_store.yml'
    ags = []
    api_counter = 0
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

    def setUp(self) -> None:
        self.extractor = ext.Extractor(self.spec_path)
        schema = self.extractor.get_schema()
        self.dge = dge.DataGroupExtractor(self.extractor)
        data_model = self.dge.get_data_model()
        response_data_model = self.dge.get_responses_data_model()
        parameters = self.dge.get_parameters()
        request_body = self.dge.get_request_body(data_model)
        http_status_codes = self.dge.get_http_status_codes()
        content_objects_per_fp = self.dge.get_content_objects_per_fp()
        responses = self.dge.get_responses()
        dgi = DataGroupIdentifier()
        request_body_datagroups = dgi.get_request_body_datagroups(request_body)
        parameters_datagroups = dgi.get_parameters_datagroups(data_model, parameters, request_body)
        http_status_datagroups = dgi.get_http_status_datagroups(http_status_codes)
        responses_datagroups = dgi.get_responses_datagroups(responses, data_model, response_data_model)
        datagroups_per_pf = dgi.identify_datagroups_per_fp(data_model) # À vérifier, louche
        self.mti = MovementTypeIdentifier()
        self.hve = hve.HTTPVerbExtractor()
        http_verbs = self.hve.get_http_verbs(self.extractor)
        self.entries = self.mti.identify_entries(request_body_datagroups, parameters_datagroups, data_model)
        self.reads = self.mti.identify_reads(parameters_datagroups)
        self.writes = self.mti.identify_writes(parameters_datagroups)
        self.exits = self.mti.identify_exits(self.mti, responses_datagroups)

        movement_types = self.mti.get_movement_types(self.entries, self.reads, self.writes, self.exits)

        self.co = CRUDIdentifier()
        crud_operations = self.co.identify_crud_operations(http_verbs)
        self.rg = ReportGenerator()
        self.fpc = fpc.FunctionPointsCalculator(movement_types)
        self.api_context = APIContext(self.fpc, crud_operations, self.entries, self.reads, self.writes, self.exits, self.rg)
        
        # Besoins aggregator = fpid, fpc, entries, reads, writes, exits, 
        self.ag = Aggregator(self.api_context)

        return super().setUp()

    def test_instantiate_aggregator(self):
        fe = FakeExtractor('./test/testdata/swagger_pet_store.yml')
        ffpc = FakeFunctionPointsCalculator()
        dge = DataGroupExtractor(fe)
        data_model = dge.get_data_model()
        response_data_model = dge.get_responses_data_model()
        parameters = dge.get_parameters()
        request_body = dge.get_request_body(data_model)
        dgi = DataGroupIdentifier()
        request_body_datagroups = dgi.get_request_body_datagroups(request_body)
        parameters_datagroups = dgi.get_parameters_datagroups(data_model, parameters, request_body)
        http_status_datagroups = dgi.get_http_status_datagroups(dge.get_http_status_codes())
        responses_datagroups = dgi.get_responses_datagroups(dge.get_responses(), data_model, response_data_model)
        datagroups_per_pf = dgi.identify_datagroups_per_fp(data_model)
        hvee = hve.HTTPVerbExtractor
        http_verbs = hvee.get_http_verbs(hvee, fe)
        mti = MovementTypeIdentifier()
        entries = mti.identify_entries(request_body_datagroups, parameters_datagroups, data_model)
        reads = mti.identify_reads(parameters_datagroups)
        writes = mti.identify_writes(parameters_datagroups)
        exits = mti.identify_exits(self.mti, responses_datagroups)
        movement_types = mti.get_movement_types(entries, reads, writes, exits)
        ci = CRUDIdentifier
        crud_operations = ci.identify_crud_operations(ci, http_verbs)
        rg = ReportGenerator()

        api_context = APIContext(ffpc, crud_operations, entries, reads, writes, exits, rg)
        self.ag.aggregate_new_specification()

    def test_aggregate_fp_description_aggregator(self):
        fe = FakeExtractor('./test/testdata/swagger_pet_store.yml')
        ffpc = FakeFunctionPointsCalculator()
        dge = DataGroupExtractor(fe)
        data_model = dge.get_data_model()
        response_data_model = dge.get_responses_data_model()
        parameters = dge.get_parameters()
        request_body = dge.get_request_body(data_model)
        dgi = DataGroupIdentifier
        request_body_datagroups = dgi.get_request_body_datagroups(dgi, request_body)
        parameters_datagroups = dgi.get_parameters_datagroups(dgi, data_model, parameters, request_body)
        http_status_datagroups = dgi.get_http_status_datagroups(dgi, dge.get_http_status_codes())
        responses_datagroups = dgi.get_responses_datagroups(dgi, dge.get_responses(), data_model, response_data_model)
        mti = MovementTypeIdentifier()
        hvee = hve.HTTPVerbExtractor
        http_verbs = hvee.get_http_verbs(hvee, fe)
        entries = mti.identify_entries(request_body_datagroups, parameters_datagroups, data_model)
        reads = mti.identify_reads(parameters_datagroups)
        writes = mti.identify_writes(parameters_datagroups)
        exits = mti.identify_exits(mti, responses_datagroups)
        ci = CRUDIdentifier
        crud_operations = ci.identify_crud_operations(ci, http_verbs)
        rg = ReportGenerator()
        api_context = APIContext(ffpc, crud_operations, entries, reads, writes, exits, rg)
        self.ag.aggregate_new_specification()
        self.ag.aggregate_fp_description()

    def test_basic_report_generatior_aggregator(self):
        fe = FakeExtractor('./test/testdata/swagger_pet_store.yml')
        ffpc = FakeFunctionPointsCalculator()
        dge = DataGroupExtractor(fe)
        dgi = DataGroupIdentifier
        request_body = dge.get_request_body(dge.get_data_model())
        mti = MovementTypeIdentifier()
        hvee = hve.HTTPVerbExtractor
        http_verbs = hvee.get_http_verbs(hvee, fe)
        ci = CRUDIdentifier
        entries = mti.identify_entries(dgi.get_request_body_datagroups(dgi, request_body), dgi.get_parameters_datagroups(dgi, dge.get_data_model(), dge.get_parameters(), dge.get_data_model()), dge.get_data_model())
        reads = mti.identify_reads(dgi.get_parameters_datagroups(dgi, dge.get_data_model(), dge.get_parameters(), dge.get_data_model()))
        writes = mti.identify_writes(dgi.get_http_status_datagroups(dgi, dgi.get_parameters_datagroups(dgi, dge.get_data_model(), dge.get_parameters(), request_body)))
        exits = mti.identify_exits(mti, dgi.get_responses_datagroups(dgi, dge.get_responses(), dge.get_data_model(), dge.get_responses_data_model()))
        crud_operations = ci.identify_crud_operations(ci, http_verbs)
        rg = ReportGenerator()
        api_context = APIContext(ffpc, crud_operations, entries, reads, writes, exits, rg)
        self.ag.aggregate_new_specification()
        self.ag.aggregate_fp_description()

    def test_get_functional_process_description(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual("Update an existing pet.putpet" , self.ag.get_functional_process_description(fpid))

    def test_get_entry_count(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(3 ,self.ag.get_entry_count(self.fpc, fpid))

    def test_get_entry_datagroups(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(['Category', 'Pet', 'Tag'] , self.ag.get_entry_datagroups(self.entries, fpid))

    def test_get_read_count(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(0 , self.ag.get_read_count(self.fpc, fpid))

    def test_get_read_datagroups(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual([] , self.ag.get_read_datagroups(self.reads, fpid))

    def test_get_write_count(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(0 , self.ag.get_write_count(self.fpc, fpid))

    def test_get_write_datagroups(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual([] , self.ag.get_write_datagroups(self.writes, fpid))

    def test_get_exit_count(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(4 , self.ag.get_exit_count(self.fpc, fpid))

    def test_get_exit_datagroups(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(['Category', 'Error', 'Pet', 'Tag'] , self.ag.get_exit_datagroups(self.exits, fpid))

    def test_get_total_count(self):
        fpid = "Update an existing pet.putpet"
        self.assertEqual(7 , self.ag.get_total_count(self.fpc, fpid))

    def test_get_crud_type(self):
        fpid = "Update an existing pet.putpet"
        crud_operations = {
            "Update an existing pet.putpet" : data.CRUD.UPDATE, 
            "Add a new pet to the store.postpet" : data.CRUD.CREATE, 
            "Finds Pets by status.getfindByStatus" : data.CRUD.READ, 
            "Finds Pets by tags.getfindByTags" : data.CRUD.READ, 
            "Finds Pets by ID.get{petId}" : data.CRUD.READ, 
            "Updates a pet in the store with form data.post{petId}" : data.CRUD.CREATE, 
            "Deletes a pet.delete{petId}" : data.CRUD.DELETE, 
            "Uploads an image.postuploadImage" : data.CRUD.CREATE,
            "Create user.postuser" : data.CRUD.CREATE,
            'Creates list of users with given input array.postcreateWithList': data.CRUD.CREATE,
            'Delete purchase order by identifier.delete{petId}': data.CRUD.DELETE, 
            'Delete user resource.delete{username}': data.CRUD.DELETE, 
            'Find purchase order by ID.get{orderId}': data.CRUD.READ, 
            'Get user by user name.get{username}': data.CRUD.READ,
            'Logs out current logged in user session.getlogout': data.CRUD.READ,
            'Logs user into the system.getlogin': data.CRUD.READ,
            'Place an order for a pet.postorder': data.CRUD.CREATE,
            'Returns pet inventories by status.getinventory': data.CRUD.READ,
            'Update user resource.put{username}': data.CRUD.UPDATE
            }   
        self.assertEqual(CRUD.UPDATE, self.ag.get_crud_type(crud_operations, fpid))
        
    @unittest.skip('Needs refacto')
    def test_get_new_api_number(self): 
        self.assertEqual(self.ag.get_new_api_number(), 'API1')
        self.assertEqual(self.ag.get_new_api_number(), 'API2')
        self.assertEqual(self.ag.get_new_api_number(), 'API3')