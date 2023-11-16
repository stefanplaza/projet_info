from projet_info.DAO.creerListeDAO import CreerlisteDAO
# from projet_info.DAO.ajouterstationDAO import AjouterstationDAO


class Creerliste:
    def ajouter_liste(self, id_utilisateur, nom_liste): 
        """
        Chaque utilisateur a droit de créer une ou plusieurs listes des
        stations mais qu'elles soient de noms différents.
        """
        operation_reussie = False
        while not operation_reussie:
            try:
                liste = CreerlisteDAO().add_liste(id_utilisateur, nom_liste)
            except Exception:
                print("-----------------------------------")
                print("Une liste avec le même nom existe déjà, veuillez réessayer.")
                print("-----------------------------------")
                nom_liste = input("Entrez un nouveau nom: ")
            else:
                if liste is not None:
                    print("-----------------------------------")
                    print("Votre liste '{}' a été créée.".format(liste.nom_liste))
                    print("-----------------------------------")
                    operation_reussie = True


if __name__ == "__main__":
    id = input("Votre id: ")
    nom = input("nom: ")
    Creerliste().ajouter_liste(id, nom)
    # AjouterstationDAO().creer_station("43363365", "Italy", "Versailles")
