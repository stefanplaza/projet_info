from dao.db_connection import DBConnection


class CreerlisteDAO:
    def taille_table(self, id_user) -> int: # La fonction taille_table est importante 
        with DBConnection().connection as connection: # pour affecter à chaque nouveau
            with connection.cursor() as cursor: # objet un "id" différent
                cursor.execute(
                    "SELECT COUNT(*)       "
                    "FROM projet.listes             "
                    "WHERE id_utilisateur = %(id_user)s ",
                )
                {
                    "id_user": id_user
                }
                res = cursor.fetchone()          
            if res is not None:
                return int(res["count"])
            else:
                return 0  # Si aucune ligne n'est trouvée, retournez 0

    def add_liste(self, id_user, nom_liste) -> bool:
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
