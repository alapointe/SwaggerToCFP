import src.mappingRules as mr
from src.basic_definitions import data

class CRUDIdentifier():

    mr = mr.MappingRules()
    """
        Version avec probabilités
    """
    def identify_crud_operations(self, http_verbs) -> dict:
        """ 
            Basic approach
            Identify which operation from CRUD (Create, read, update, delete) is associated with the functional process

            Requires:
            - Http verbs

            Returns:
            - CRUD operations related to http verbs
        """
        crud_operations = {}
        for fpid, values in http_verbs.items():
            for description, http_verb in values.items():   
                crud_operations.update({fpid : self.mr.apply_http_verb_to_crud_mapping(http_verb)})
        return crud_operations
    
    def identify_crud_operation_per_fp(self, http_verbs, fpid):
        """ 
            Identify which operation from CRUD (Create, read, update, delete) is associated with the functional process

            Requires:
            - Http verbs
            - Fpid

            Returns
            - CRUD operation for a given fpid
        """
        crud_operation = data.CRUD.UNDEFINED
        for key, values in http_verbs.items():
            if isinstance(values, dict):
                for description, http_verb in values.items():
                    if description == fpid:
                        return self.mr.get_best_crud_per_fp(self.mr.apply_http_verb_to_crud_mapping_with_probabilities(http_verb), fpid)
        return crud_operation
    

    def get_crud_probability_based_on_httpVerb(self, httpVerb, fpId = 1):
        """ 
            Obtain the probability associated which a CRUD operation (Create, read, update, delete) is associated with the functional process

            Requires:
            - Verbe HTTP, fp id
            - Mapping Rules
            Returns
            - CRUD operation, probability, fp id
        """
        return self.mappingRules.applyHTTPVerbToCRUDMapping(httpVerb)

    def get_crud_probability_based_on_fp_description(self, description, fpId = 1):
        """ 
            Obtain the probability associated which a CRUD operation (Create, read, update, delete) is associated with the functional process

            Requires:
            - Description du processus fonctionnel, fp id
            - Mapping Rules
            Returns
            - CRUD operation, probability, fp id
        """
        return self.mappingRules.applyDescriptionToCRUDMapping(description)