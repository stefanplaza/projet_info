from Classe.Station import Station

class Services:
    def __init__(self, id_service, nom_service):
        """
        Initialise une instance de la classe Services avec un identifiant de service et un nom de service.

        Args:
            id_service (int): L'identifiant du service associé à l'instance.
            nom_service (str): Le nom du service, une description de ce que le service représente.

        Exemple:
            Pour représenter un service de station-service, id_service pourrait être un identifiant unique,
            comme un code, et nom_service pourrait être une chaîne de caractères décrivant le service,
            par exemple "Lavage de voiture" ou "Cafétéria".
        """
        self.id_service = id_service
        self.nom_service = nom_service
