import json
import os
import src.specification as sp
from test.helpers.DummySpecificationFileTest import DummySpecificationFileTest
import utils.jsonDataHandler as jdh


class Test_specification(DummySpecificationFileTest):   

    def parcourir_dictionnaire(self, dico):
        for cle, valeur in dico.items():
            # Affichage de la clé
            print(f"Clé : {cle}")

            # Si la valeur est un dictionnaire, on l'explore récursivement
            if isinstance(valeur, dict):
                self.parcourir_dictionnaire(valeur)

            # Sinon, on affiche la valeur
            else:
                print(f"Valeur : {valeur}")

    def test_get_specification(self):
        self.assertIsInstance(sp.get_specification('./test/testdata/swagger_pet_store.yml'), dict)