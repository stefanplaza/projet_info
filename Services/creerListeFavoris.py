from projet_info.DAO import creerListeDAO


class Creerliste:
    def ajouter(self, id_utilisateur, nom_liste):
        verify = creerListeDAO().add_liste(id_utilisateur, nom_liste)
        if (verify):
            print("-----------------------------------")
            print("Votre liste {} a été bien ajoutée.\n".format(nom_liste))
        else:
            print("-----------------------------------")
            print("Votre liste n'a pas été ajoutée.")
