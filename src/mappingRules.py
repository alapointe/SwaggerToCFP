#!/usr/bin/env python3

from src.basic_definitions import params
from src.basic_definitions import data

class MappingRules():

    def __init__(self) -> None:
        pass

    def get_best_crud_per_fp(self, data_dict, fpid) -> data.CRUD:
        max_prob = 0
        result_data = None
        for key, value in data_dict.items():
            if isinstance(value, dict):
                for data, prob in value.items():
                    if prob > max_prob:
                        max_prob = prob
                        result_data = data
        return result_data

    def apply_http_verb_to_crud_mapping_with_probabilities(self, HTTPVerb) -> dict:
        """
            Probabilities
            HTTP Verb mapping

            Requires:
                - HTTP verb

            Returns
                - A dictionnary of possible CRUD operation associated with its probability
        """
        HTTPVerb = HTTPVerb.lower()
        if HTTPVerb not in params.supported_http_verbs:
            raise ValueError(f"Invalid HTTP verb: '{HTTPVerb}'. Supported verbs are: {', '.join(params.supported_http_verbs)}")
        # @MR1 
        if (HTTPVerb == "delete"):
            return {"prob1" : {data.CRUD.DELETE : 100}}
        # @MR2 
        if (HTTPVerb == "get"):
            return {"prob1" : {data.CRUD.READ : 100}}
        # @MR3
        if (HTTPVerb == "put"):
            return {"prob1" : {data.CRUD.UPDATE : 93}, "prob2" : {data.CRUD.READ : 7}}
        # @MR4
        if (HTTPVerb == "patch"):
            return {"prob1" : {data.CRUD.UPDATE : 69}, "prob2" : {data.CRUD.READ : 15}, "prob3" : {data.CRUD.CREATE : 8}}
        # @MR5
        if (HTTPVerb == "post"):
            return {"prob1" : {data.CRUD.READ : 48}, "prob2" : {data.CRUD.CREATE : 44}, "prob3" : {data.CRUD.DELETE : 8}, "prob4" : {data.CRUD.UPDATE : 5}}

    def apply_http_verb_to_crud_mapping(self, HTTPVerb) -> dict:
        """
            Basic approach
            HTTP Verb mapping

            Requires:
                - HTTP verb

            Returns
                - A dictionnary of fpid associated to his CRUD
        """
        HTTPVerb = HTTPVerb.lower()
        if HTTPVerb not in params.supported_http_verbs:
            raise ValueError(f"Invalid HTTP verb: '{HTTPVerb}'. Supported verbs are: {', '.join(params.supported_http_verbs)}")
        # @MR1 
        if (HTTPVerb == "delete"):
            return data.CRUD.DELETE
        # @MR2 
        if (HTTPVerb == "get"):
            return data.CRUD.READ
        # @MR3
        if (HTTPVerb == "put"):
            return data.CRUD.UPDATE
        # @MR4
        if (HTTPVerb == "patch"):
            return data.CRUD.UPDATE
        # @MR5
        if (HTTPVerb == "post"):
            return data.CRUD.CREATE
    
    def extract_verbs(self, tagged_words):
        verbs = []
        for word, tag in tagged_words:
            if tag == 'VERB':
                verbs.append(word)
        return verbs

    def identify_verb_category(self, verb, verb_categories):
        """Identifies the category of a verb based on a given dictionary.

        Args:
            verb: The verb to classify.
            verb_categories: A dictionary mapping verbs to their categories.

        Returns:
            The category of the verb (read, create, update, delete), or None if not found.
        """

        if verb in verb_categories:
            return verb_categories[verb][0]  # Assuming only one category per verb
        else:
            return data.CRUD.UNKNOWN

    def extract_nouns(self, tagged_words):
        nouns = []
        for word, tag in tagged_words:
            if tag == 'NOUN':
                nouns.append(word)
        return nouns
    
    def apply_fp_to_datagroups_mapping(self, datagroups):
        """
            Simplist approach: only returns np.nouns as possible datagroups

            Example: tree.pretty_print()
                                                ROOT
                                                    |
                                                SENT
                                                    |
                                                COORD
                ___________________________________|____________________________________
                |            NP                     |                      |             |
                |       _____|___________           |                      |             |
                |      |     |           AP         VN                   MWADV           AP
                |      |     |           |          |           ___________|____         |
            VERB   DET   NOUN        ADJ        CONJ       VERB        ADP  DET      ADJ
                |      |     |           |          |          |           |    |        |
            recupérer les projets    externes      et         internes     d'  une  organisation


            Here it would identify "projets" as the only datagroup. (In fact, "organisation" is also a datagroup)
        """
        datagroup_mapping = {}
        for fpids in datagroups:
            it = NLPStrategy.parse_sentence(nlps, fpids.lower())
            for tree in it:
                pos_tags = NLPStrategy.pos_tag(self, tree)
            nouns = self.extract_nouns(pos_tags)
            # Compare extracted nouns with datagroups
            for noun in nouns:
                # TODO
                pass
                # print("Noun: ")
                # print(noun)
        return {}
# Mapping Rules Template

# Define input file format
# input_format = {
#     "fields": [
#         {"name": "field1", "type": "string"},
#         {"name": "field2", "type": "integer"},
#         # Add more fields as needed
#     ],
#     # Additional information about the input format, such as delimiter, encoding, etc.
#     "delimiter": ",",
#     "encoding": "utf-8",
# }

# # Define output file format
# output_format = {
#     "fields": [
#         {"name": "output_field1", "type": "string"},
#         {"name": "output_field2", "type": "float"},
#         # Add more fields as needed
#     ],
#     # Additional information about the output format, such as delimiter, encoding, etc.
#     "delimiter": "\t",
#     "encoding": "utf-8",
# }

# # Define mapping rules
# mapping_rules = [
#     {"input_field": "field1", "output_field": "output_field1", "transformation": lambda x: x.upper()},
#     {"input_field": "field2", "output_field": "output_field2", "transformation": lambda x: float(x) * 2},
#     # Add more mapping rules as needed
# ]

# # Function to apply mapping rules to convert input data to output data
# def apply_mapping_rules(input_data):
#     output_data = []
#     for record in input_data:
#         output_record = {}
#         for rule in mapping_rules:
#             input_value = record.get(rule["input_field"])
#             transformed_value = rule["transformation"](input_value)
#             output_record[rule["output_field"]] = transformed_value
#         output_data.append(output_record)
#     return output_data

# # Example usage
# input_data = [
#     {"field1": "value1", "field2": 5},
#     {"field1": "value2", "field2": 10},
#     # Add more input records as needed
# ]

# output_data = apply_mapping_rules(input_data)
# print(output_data)
