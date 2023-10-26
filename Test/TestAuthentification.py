from Classe.Authentification import Authentification
import unittest

class TestAuthentification(unittest.TestCase):
    def setUp(self):
        # Crée une instance de Authentification pour les tests
        self.auth = Authentification("utilisateur1", "123")

    def test_compare_identifiants_valides(self):
        resultat = self.auth.compare("utilisateur1", "123")
        self.assertTrue(resultat)

    def test_compare_identifiants_invalides(self):
        resultat = self.auth.compare("utilisateur2", "123")
        self.assertFalse(resultat)

    def test_compare_mauvais_mot_de_passe(self):
        resultat = self.auth.compare("utilisateur2", "456")
        self.assertFalse(resultat)

if __name__ == '__main__':
    unittest.main()