from enum import Enum

class CRUD(Enum):
    CREATE = 'C'
    READ = 'R'
    UPDATE = 'U'
    DELETE = 'D'
    UNKNOWN = 'Unknown'
    UNDEFINED = 'Undefined'

    def __str__(self):
        if self == self.READ:
            return 'Lecture (R)'
        elif self == self.CREATE:
            return 'Écriture (C)'
        elif self == self.UPDATE:
            return 'Mise à jour (U)'
        elif self == self.DELETE:
            return 'Suppression (D)'
        else:
            return 'Indéterminé'

class DataMovementType(Enum):
    TRIGGER = 'T'
    ENTRY = 'E'
    READ = 'L'
    WRITE = 'C'
    EXIT = 'S'
    UNKNOWN = 'Unknown'

class CRUDMapping():
    # CRUD operation mapping based on verb groups (modify this as needed)
    crud_verb_groups = {
        CRUD.READ: ["obtenir","récupérer", "recupérer", "recuperer", "afficher", "lister", "trouver", "chercher", "Rechercher", "rechercher", "Consulter", "consulter", "Valider", "valider", "Retourner", "retourner"],
        CRUD.CREATE: ["Créer", "créer", "creer", "Creer", "Ajouter", "ajouter", "initialiser", "Générer", "Generer", "générer", "generer", "Exécuter", "Effectuer", "Faire", "Ouvrir", "Inscrire", "Enregister", "enregistrer", "Calculer", "Soumettre", "Produire"], 
        CRUD.UPDATE: ["Mettre à jour", "mettre à jour", "Mettre a jour", "modifier", "éditer", "changer", "Réactiver", "reactiver", "Effectuer", "Accepter"],
        CRUD.DELETE: ["Supprimer", "supprimer", "Fermer", "fermer", "Renverser", "renverser", "Annuler", "annuler", "enlever", "effacer", "détruire"],  
        }
    
class ErreurREST():
    error_types = ['BadRequest', 'Unauthorized', 'Forbidden', 'NotFound', 'UnavailableForLegalReasons', 'InternalServer']