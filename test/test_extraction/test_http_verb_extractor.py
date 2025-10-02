import src.extraction.HTTPVerbExtractor as hve
import src.extraction.Extractor as extractor
from test.helpers.CalculationSpecificationFileTest import CalculationSpecificationFileTest

class Test_DataGroupExtractor(CalculationSpecificationFileTest):

    def setUp(self) -> None:
        self.extractor = extractor.Extractor('./test/testdata/swagger_pet_store.yml')
        self.hve = hve.HTTPVerbExtractor()
        return super().setUp()
    
    def test_get_http_verbs(self):
        expected_dict = {
            'Update an existing pet.putpet': {'Update an existing pet.': 'put'}, 
            'Add a new pet to the store.postpet': {'Add a new pet to the store.': 'post'}, 
            'Finds Pets by status.getfindByStatus': {'Finds Pets by status.': 'get'}, 
            'Finds Pets by tags.getfindByTags': {'Finds Pets by tags.': 'get'}, 
            'Find pet by ID.get{petId}': {'Find pet by ID.': 'get'}, 
            'Updates a pet in the store with form data.post{petId}': {'Updates a pet in the store with form data.': 'post'}, 
            'Deletes a pet.delete{petId}': {'Deletes a pet.': 'delete'}, 
            'Uploads an image.postuploadImage': {'Uploads an image.': 'post'}, 
            'Returns pet inventories by status.getinventory': {'Returns pet inventories by status.': 'get'}, 
            'Place an order for a pet.postorder': {'Place an order for a pet.': 'post'}, 
            'Find purchase order by ID.get{orderId}': {'Find purchase order by ID.': 'get'}, 
            'Delete purchase order by identifier.delete{orderId}': {'Delete purchase order by identifier.': 'delete'}, 
            'Create user.postuser': {'Create user.': 'post'}, 
            'Creates list of users with given input array.postcreateWithList': {'Creates list of users with given input array.': 'post'}, 
            'Logs user into the system.getlogin': {'Logs user into the system.': 'get'}, 
            'Logs out current logged in user session.getlogout': {'Logs out current logged in user session.': 'get'}, 
            'Get user by user name.get{username}': {'Get user by user name.': 'get'}, 
            'Update user resource.put{username}': {'Update user resource.': 'put'}, 
            'Delete user resource.delete{username}': {'Delete user resource.': 'delete'}
            }
        # print(self.hve.get_http_verbs(self.extractor))
        self.assertEqual(sorted(self.hve.get_http_verbs(self.extractor)), sorted(expected_dict))