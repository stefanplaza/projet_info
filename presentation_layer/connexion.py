print("Avez vous un compte ?")
x = input()
if x == Oui:
    print("Nom d'utilisateur ?")
    x1 = input()
    if """x1 existe""":
        print("Mot de passe ?")
        x2 = input()
        if x2 == x1.mdp: 
            return """accès à son compte"""
        else:
            print("mot de passe incorrect")
            """retour case départ"""
    else:
        print("Nom d'utilisateur introuvable")
        """retour case départ"""
else:
    """création d'un compte"""
