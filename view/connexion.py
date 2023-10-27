import database from

class connexion:
def login():
    print("entrez votre identifiant")
    x=input()
    print("entrez votre mot de passe")
    y=input()
    if x in accounts and accounts[x] == y:
        print("Connexion réussie.")
    else:
        print("Identifiants invalides.")

while True:
    print("1. Créer un compte")
    print("2. Se connecter")
    choice = input("Choisissez une option (1/2) : ")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    else:
        print("Option invalide. Veuillez réessayer.")
