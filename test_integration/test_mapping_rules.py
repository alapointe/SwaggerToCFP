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
        self.assertEqual(str(error.exception), f"Invalid HTTP verb: '{http_verb.lower()}'. Supported verbs are: {', '.join(params.supported_http_verbs)}")
