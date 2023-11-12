from projet_info.DAO import authentificationDAO


class Authentification:
    def verifier(self, id_user, mdp) -> bool:
        detecte = 0
        while not detecte:
            verify = authentificationDAO().verification(id_user, mdp)
            if (verify):
                detecte = 1
                print("-----------------------------------")
                print("Le mot de passe rentré ne correspond pas à l'identifiant choisi.\n")
                print("Veuillez réessayer")   
            else:
                print("-----------------------------------")
                print("Connexion réussite.")
