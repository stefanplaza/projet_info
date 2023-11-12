from projet_info.DAO import authentificationDAO


class Authentification:
    def __init__(self, id_user, mdp):
        self.id_user = id_user
        self.mdp = mdp

    detecte = 0
    while not detecte:
        verify = authentificationDAO().verification(self.id_user, self.mdp)
        if (verify is None):
            detecte = 1
            print("-----------------------------------")
            print("Le mot de passe rentré ne correspond pas à l'identifiant choisi.\n")
            print("Veuillez réessayer")   
        else:
            print("-----------------------------------")
            print("Connexion réussite.")
