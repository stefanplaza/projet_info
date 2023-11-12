from utils.singleton import Singleton
from dao.db_connection import DBConnection


class InscriptionDAO(metaclass=Singleton):
    def taille_table(self) -> int:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT COUNT(*)       "
                    "FROM projet.utilisateur             ",
                )
                res = cursor.fetchone()          
            if res is not None:
                return int(res["count"])
            else:
                return 0  # Si aucune ligne n'est trouvée, retournez 0

    def add_user(self, mdp):
        id_utilisateur = self.taille_table() + 1
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet.utilisateur (id_utilisateur, mdp)       "
                    "VALUES                                                     "
                    "(%(id_utilisateur)s, %(mdp)s)                              "
                    "RETURNING id_utilisateur, mdp                              ",
                    {
                        "id_utilisateur": id_utilisateur,
                        "mdp": mdp,
                    },
                )
                res = cursor.fetchone()
                print("Votre identifiant est: {} et votre mot de passe est: {}.".format(res["id_utilisateur"], res["mdp"]))
