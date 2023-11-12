from projet_info.DAO import AccederlisteDAO
from projet_info.Classe import Liste


class AccederListesFavoris:
    def toutes_les_listes(self, id_user) -> list[Liste]:
        resultat = AccederlisteDAO().find_all_listes(id_user)
        if (len(resultat)):
            return resultat
        else:
            print("-----------------------------------")
            print("Aucune liste de favoris trouvée.")
