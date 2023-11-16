from projet_info.DAO.authentificationDAO import AuthentificationDAO


class Authentification:
    def verifier(self):
        detecte = 0
        while not detecte:
            id_user = input("Votre id: ")
            mdp = input("Votre mdp: ")        
            verify = AuthentificationDAO().verification(id_user, mdp)
            if (not verify):
                print("-----------------------------------")
                print("Le mot de passe rentré ne correspond pas à l'identifiant choisi.")
                print("Veuillez réessayer.")
                print("-----------------------------------")
            else:
                detecte = 1                
                print("-----------------------------------")
                print("Connexion réussite.")
                print("-----------------------------------")
                pass


if __name__ == "__main__":

    Authentification().verifier()
