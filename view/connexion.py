# Base de données factice pour stocker les comptes (utilisation de dictionnaires)
accounts = {}

def create_account():
    username = input("Entrez un nom d'utilisateur : ")
    password = input("Entrez un mot de passe : ")
    accounts[username] = password
    print("Compte créé avec succès.")

def login():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    if username in accounts and accounts[username] == password:
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
