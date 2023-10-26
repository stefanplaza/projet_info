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