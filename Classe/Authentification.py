import unittest

class Authentification:
    def __init__(
        self,
        id_utilisateur,
        mot_de_passe,
    ):
        self._id_utilisateur = id_utilisateur
        self._mot_de_passe = mot_de_passe

    def compare(self, id_utilisateur, mot_de_passe):
        """
        Compare les noms d'utilisateur et les mots de passe.
        
        Args:
            id_utilisateur (str): Nom d'utilisateur à vérifier.
            mot_de_passe (str): Mot de passe à vérifier.
        
        Returns:
            bool: True si les identifiants sont valides, False sinon.
        """
        if self._id_utilisateur == id_utilisateur and self._mot_de_passe == mot_de_passe:
            return True
        else:
            return False
        
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