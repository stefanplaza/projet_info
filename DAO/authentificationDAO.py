from dao.db_connection import DBConnection


class AuthentificationDAO:
    def verification(self, id_user, mdp) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    "  FROM projet.utilisateur                      "
                    " WHERE id_utilisateur=%(id)s AND mdp=%(mdp)s   ",
                    {"id": self.id_user,
                     "mdp": self.mdp},
                 )
                res = cursor.fetchone()
        if res is None:
            return False
        else:
            return True
