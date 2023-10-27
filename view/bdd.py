# Créer une base de données vide (dictionnaire)
"""class Database:"""
database = {}

print("Choisissez nom d'utilisateur")
nom_utilisateur = input()
print("Choisissez un mot de passe")
mot_de_passe = input()

def ajouter_utilisateur(nom_utilisateur, mot_de_passe):
    """Ajouter un utilisateur à la base de données."""
    database[nom_utilisateur] = mot_de_passe
    print(f"Utilisateur {nom_utilisateur} ajouté avec succès.")

"""# Exemple d'utilisation
ajouter_utilisateur("utilisateur1", "motdepasse1")
ajouter_utilisateur("utilisateur2", "motdepasse2")

# Afficher la base de données
print("Base de données actuelle :", database)"""