from projet_info.DAO.db_connection import DBConnection
from projet_info.Classe import Liste


class AccederlisteDAO:
    def find_all_listes(self, id_user) -> list[Liste]:  # La fonction taille_table est importante 
        with DBConnection().connection as connection:  # pour affecter à chaque nouveau
            with connection.cursor() as cursor:  # objet un "id" différent
                cursor.execute(
                    "SELECT id_liste, nom_liste, id_station                   "
                    "FROM projet.listes pl                                    "
                    "JOIN projet.contenu_liste pc ON pl.id_liste = pc.id_liste"
                    "WHERE id_utilisateur = %(id_user)s                       ",
                )
                {
                    "id_user": id_user
                }
                res = cursor.fetchall()

            listes = []

            if res is not None:
                for row in res:
                    element = Liste[res["id_liste"],res["nom_liste"], res["id_liste"]]
                    listes.append(element)

            return listes

    def acceder(self, id_user, nom_liste) -> bool:
        id_liste = self.taille_table() + 1
        id_utilisateur = self.id_user
        nom_liste = self.nom_liste
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.listes (id_liste, id_utilisateur, nom_liste)"
                    "VALUES                                                         "
                    "(%(id_liste)s, %(id_utilisateur)s, %(nom_liste)s)              "
                    "RETURNING id_liste, id_utilisateur, nom_liste                  ",
                    {
                        "id_liste": id_liste,
                        "id_utilisateur": id_utilisateur,
                        "nom_liste": nom_liste
                    },
                )
                res = cursor.fetchone()
                if res is None:
                    return False
                else:
                    return True
