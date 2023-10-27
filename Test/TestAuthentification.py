from Classe.Authentification import Authentification
import unittest

class TestAuthentificationMethods(unittest.TestCase):
    def test_init(self):
        # Vérifie si l'initialisation de l'objet Authentification se déroule correctement
        auth = Authentification("utilisateur123", "motdepasse123")
        self.assertEqual(auth._id_utilisateur, "utilisateur123")
        self.assertEqual(auth._mot_de_passe, "motdepasse123")

    def test_compare(self):
        # Crée un objet Authentification pour les tests
        auth = Authentification("utilisateur123", "motdepasse123")

        # Vérifie si la méthode compare fonctionne correctement pour des identifiants valides
        self.assertTrue(auth.compare("utilisateur123", "motdepasse123"))

        # Vérifie si la méthode compare fonctionne correctement pour des identifiants invalides
        self.assertFalse(auth.compare("utilisateur456", "motdepasse456"))

if __name__ == '__main__':
    unittest.main()