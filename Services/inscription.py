from projet_info.DAO import inscriptionDAO


class Inscription:
    def inscrire(self, mdp):
        inscrit = inscriptionDAO.add_user(mdp)