from Classe.TypeCarburant import TypeCarburant

class PrixCarburant:
    def __init__(self, id_carburant, prix):
        """
        Initialise une instance de la classe PrixCarburant avec un identifiant de carburant et son prix.

        Args:
            id_carburant (int): L'identifiant du type de carburant associé à l'instance.
            prix (float): Le prix du carburant en unité monétaire (par exemple, en euros par litre).
        """
        self.id_carburant = id_carburant
        self.prix = prix
