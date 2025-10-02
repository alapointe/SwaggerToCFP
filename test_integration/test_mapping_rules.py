from os import error
import unittest
from src.basic_definitions import params
from src.basic_definitions import data
import src.mappingRules as mr

class TestMappingRules(unittest.TestCase):
    mappingRules = mr.MappingRules()

    @unittest.skip("Not implemented")
    def test_apply_fp_to_datagroups_mapping(self):
        datagroups = {
            "Recupérer les projets COMPTE_EPARGNE_ET_RETRAITE et EPARGNE_PAR_VERSEMENT_BONIFIE d'un membre-client": ["Membre-client (PDO)", "Projet", "Message d'erreur"], 
            'Créer un projet COMPTE_EPARGNE_ET_RETRAITE': ["Membre-client (PDO)", "Projet", "Projet Entente", "Message d'erreur"],
            'Mettre à jour un projet COMPTE_EPARGNE_ET_RETRAITE': ["Membre-client (PDO)", "Projet", "Message d'erreur"], 
            'Recuperer un projet COMPTE_EPARGNE_ET_RETRAITE précis par son identifiant': ["Membre-client (PDO)", "Projet", "Message d'erreur"], 
            'Supprimer un projet COMPTE_EPARGNE_ET_RETRAITE': ["Projet", "Message d'erreur"], 
            }
        expected_movement_types = {
            "Recupérer les projets COMPTE_EPARGNE_ET_RETRAITE et EPARGNE_PAR_VERSEMENT_BONIFIE d'un membre-client" : {data.DataMovementType.ENTRY : [ "Membre-Client Particulier (PDO)", "Projet"], data.DataMovementType.READ : ["Projet", "Projet Entente"], data.DataMovementType.WRITE : [], data.DataMovementType.EXIT : ["Projet", "Message d'erreur"]},
            "Créer un projet COMPTE_EPARGNE_ET_RETRAITE" : {data.DataMovementType.ENTRY : [ "Membre-Client Particulier (PDO)", "Projet"], data.DataMovementType.READ : ["Membre-Client Particulier (PDO)"], data.DataMovementType.WRITE : [], data.DataMovementType.EXIT : ["Message d'erreur"]},
            "Mettre à jour un projet COMPTE_EPARGNE_ET_RETRAITE" : {data.DataMovementType.ENTRY : [ "Membre-Client Particulier (PDO)", "Projet"], data.DataMovementType.READ : ["Membre-Client Particulier (PDO)", "Projet"], data.DataMovementType.WRITE : ["Membre-Client Particulier (PDO)", "Projet"], data.DataMovementType.EXIT : ["Message d'erreur", "Membre-Client Particulier (PDO)"]},
            'Recuperer un projet COMPTE_EPARGNE_ET_RETRAITE précis par son identifiant' : {data.DataMovementType.ENTRY : [ "Membre-Client Particulier (PDO)", "Projet"], data.DataMovementType.READ : ["Projet", "Projet Entente"], data.DataMovementType.WRITE : [], data.DataMovementType.EXIT : ["Projet", "Message d'erreur"]}, 
            "Supprimer un projet COMPTE_EPARGNE_ET_RETRAITE" : {data.DataMovementType.ENTRY : ["Projet"], data.DataMovementType.READ : ["Projet"], data.DataMovementType.WRITE : ["Projet"], data.DataMovementType.EXIT : ["Message d'erreur"]}     
            }
        self.assertEqual(expected_movement_types, self.mappingRules.apply_fp_to_datagroups_mapping(datagroups))

    # def test_http_verb_to_CRUD_mapping(self):
    #     httpVerb = "GET"
    #     self.assertEqual(({"prob1" : {data.CRUD.READ : 100}}), self.mappingRules.apply_http_verb_to_crud_mapping(httpVerb))
    #     httpVerb = "DELETE"
    #     self.assertEqual(({"prob1" : {data.CRUD.DELETE : 100}}), self.mappingRules.apply_http_verb_to_crud_mapping(httpVerb))
    #     httpVerb = "PUT"
    #     self.assertEqual(({"prob1" : {data.CRUD.UPDATE : 93}, "prob2" : {data.CRUD.READ : 7}}), self.mappingRules.apply_http_verb_to_crud_mapping(httpVerb))
    #     httpVerb = "PATCH"
    #     self.assertEqual(({"prob1" : {data.CRUD.UPDATE : 69}, "prob2" : {data.CRUD.READ : 15}, "prob3" : {data.CRUD.CREATE : 8}}), self.mappingRules.apply_http_verb_to_crud_mapping(httpVerb))
    #     httpVerb = "POST"
    #     self.assertEqual(({"prob1" : {data.CRUD.READ : 48}, "prob2" : {data.CRUD.CREATE : 44}, "prob3" : {data.CRUD.DELETE : 8}, "prob4" : {data.CRUD.UPDATE : 5}}), self.mappingRules.apply_http_verb_to_crud_mapping(httpVerb))
    #     httpVerb = "HEAD"
    #     with self.assertRaises(ValueError) as error:
    #         self.mappingRules.apply_http_verb_to_crud_mapping(httpVerb)
    #         self.assertEqual(str(error.exception), f"Invalid HTTP verb: '{httpVerb}'. Supported verbs are: {', '.join(params.supported_http_verbs)}")

    def test_http_verb_to_CRUD_mapping(self):
        http_verb = "GET"
        self.assertEqual(data.CRUD.READ, self.mappingRules.apply_http_verb_to_crud_mapping(http_verb))
        http_verb = "DELETE"
        self.assertEqual(data.CRUD.DELETE, self.mappingRules.apply_http_verb_to_crud_mapping(http_verb))
        http_verb = "PUT"
        self.assertEqual(data.CRUD.UPDATE, self.mappingRules.apply_http_verb_to_crud_mapping(http_verb))
        http_verb = "PATCH"
        self.assertEqual(data.CRUD.UPDATE, self.mappingRules.apply_http_verb_to_crud_mapping(http_verb))
        http_verb = "POST"
        self.assertEqual(data.CRUD.CREATE, self.mappingRules.apply_http_verb_to_crud_mapping(http_verb))
        http_verb = "HEAD"
        with self.assertRaises(ValueError) as error:
            self.mappingRules.apply_http_verb_to_crud_mapping(http_verb)
        self.assertEqual(str(error.exception), f"Invalid HTTP verb: '{http_verb}'. Supported verbs are: {', '.join(params.supported_http_verbs)}")

    def test_get_best_crud_per_fp(self):
        fpid = "Recupérer les projets COMPTE_EPARGNE_ET_RETRAITE et EPARGNE_PAR_VERSEMENT_BONIFIE d'un membre-client"
        data_dict = {"prob1" : {data.CRUD.READ : 48}, "prob2" : {data.CRUD.CREATE : 44}, "prob3" : {data.CRUD.DELETE : 8}, "prob4" : {data.CRUD.UPDATE : 5}}
        expected_crud = data.CRUD.READ
        self.assertEqual(self.mappingRules.get_best_crud_per_fp(data_dict, fpid), expected_crud)

    def test_description_to_CRUD_mapping(self):
        description_list =  [
            "Recupérer les projets COMPTE_EPARGNE_ET_RETRAITE et EPARGNE_PAR_VERSEMENT_BONIFIE d'un membre-client",
            "Créer un projet COMPTE_EPARGNE_ET_RETRAITE",
            "Mettre à jour un projet COMPTE_EPARGNE_ET_RETRAITE",
            "Recuperer un projet COMPTE_EPARGNE_ET_RETRAITE précis par son identifiant",
            "Supprimer un projet COMPTE_EPARGNE_ET_RETRAITE"
        ]
        expected_mapping_dict = {
            "Recupérer les projets COMPTE_EPARGNE_ET_RETRAITE et EPARGNE_PAR_VERSEMENT_BONIFIE d'un membre-client": data.CRUD.READ,
            "Créer un projet COMPTE_EPARGNE_ET_RETRAITE": data.CRUD.CREATE,
            "Mettre à jour un projet COMPTE_EPARGNE_ET_RETRAITE": data.CRUD.UPDATE,
            "Recuperer un projet COMPTE_EPARGNE_ET_RETRAITE précis par son identifiant": data.CRUD.READ,
            "Supprimer un projet COMPTE_EPARGNE_ET_RETRAITE": data.CRUD.DELETE
        }
        self.assertEqual(sorted(expected_mapping_dict), sorted(self.mappingRules.apply_description_to_crud_mapping(description_list)))

    @unittest.skip("Not implemented yet")
    def test_extract_verbs(self):
        # From NLPStrategy.parse_sentence but in reality it should be the following, there seem to b e an issue with NLTK french
        # pos_tags = [('recupérer', 'VERB'), ('les', 'DET'), ('projets', 'NOUN'), ('compte-epargne-et-retraite', 'ADJ'), ('et', 'CONJ'), ('epargne-par-versement-bonifie', 'ADJ'), ("d'", 'ADP'), ('un', 'DET'), ('membre-client', 'NOUN')]
        pos_tags = [('recupérer', 'VERB'), ('les', 'DET'), ('projets', 'NOUN'), ('compte-epargne-et-retraite', 'ADJ'), ('et', 'CONJ'), ('epargne-par-versement-bonifie', 'VERB'), ("d'", 'ADP'), ('un', 'DET'), ('membre-client', 'ADJ')]
        expected_verbs = ['recupérer']
        self.assertEqual(expected_verbs, self.mappingRules.extract_verbs(pos_tags))

    @unittest.skip("Not implemented yet")
    def test_extract_nouns(self):
        # From NLPStrategy.parse_sentence but in reality it should be the following, there seem to b e an issue with NLTK french
        # pos_tags = [('recupérer', 'VERB'), ('les', 'DET'), ('projets', 'NOUN'), ('compte-epargne-et-retraite', 'ADJ'), ('et', 'CONJ'), ('epargne-par-versement-bonifie', 'ADJ'), ("d'", 'ADP'), ('un', 'DET'), ('membre-client', 'NOUN')]
        pos_tags = [('recupérer', 'VERB'), ('les', 'DET'), ('projets', 'NOUN'), ('compte-epargne-et-retraite', 'ADJ'), ('et', 'CONJ'), ('epargne-par-versement-bonifie', 'VERB'), ("d'", 'ADP'), ('un', 'DET'), ('membre-client', 'ADJ')]
        expected_nouns = ['projets', 'membre-client']
        self.assertEqual(expected_nouns, self.mappingRules.extract_nouns(pos_tags))

