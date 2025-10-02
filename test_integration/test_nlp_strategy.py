
from nltk.tree import Tree
import unittest
import src.nlp_strategy as nlps


class TestNLPStrategy(unittest.TestCase):
    
    nlps = nlps.NLPStrategy()

    def test_tokenize(self):
        sentence = 'Le renard brun rapide saute par-dessus le chien paresseux.'
        tokenised_sentence = ['Le', 'renard', 'brun', 'rapide', 'saute', 'par-dessus', 'le', 'chien', 'paresseux', '.']
        self.assertEqual(tokenised_sentence, nlps.NLPStrategy.tokenize(nlps, sentence))
        sentence = "Mettre à jour une réservation"
        tokenised_sentence = ['Mettre', 'à', 'jour', 'une', 'réservation']
        self.assertEqual(tokenised_sentence, nlps.NLPStrategy.tokenize(nlps, sentence))

    def test_parse_sentence(self):
        sentence = "Mettre à jour une réservation"
        expected_list = [Tree('ROOT', [Tree('SENT', [Tree('NP', [Tree('VERB', ['Mettre']), Tree('ADP', ['à']), Tree('PP', [Tree('NOUN', ['jour']), Tree('NP', [Tree('DET', ['une']), Tree('NOUN', ['réservation'])])])])])])]
        self.assertEqual(expected_list, list(nlps.NLPStrategy.parse_sentence(nlps, sentence)))

    def test_pos_tag(self):
        tree = "Recupérer les livres SCIENCE-FICTION et AVENTURE d'un client"
        tree = Tree('SENT', [Tree('COORD', [Tree('VERB', ['recupérer']), Tree('NP', [Tree('DET', ['les']), Tree('NOUN', ['livres']), Tree('AP', [Tree('ADJ', ['science-fiction'])])]), Tree('VN', [Tree('CONJ', ['et'])]), Tree('MWADV', [Tree('VERB', ['aventure']), Tree('ADP', ["d'"]), Tree('DET', ['un'])]), Tree('AP', [Tree('ADJ', ['client'])])])])
        expected_list = [('recupérer', 'VERB'), ('les', 'DET'), ('livres', 'NOUN'), ('science-fiction', 'ADJ'), ('et', 'CONJ'), ('aventure', 'VERB'), ("d'", 'ADP'), ('un', 'DET'), ('client', 'ADJ')]
        self.assertEqual(expected_list, list(nlps.NLPStrategy.pos_tag(nlps, tree)))

