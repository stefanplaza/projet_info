class Station:
    def __init__(
        self,
        id_station,
        longitude,
        latitude,
        ville,
        adresse,
        type_carburant,
        prix_carburant,
        coordonnees,
    ):
        self.id_station = id_station
        self.longitude = longitude
        self.latitude = latitude
        self.ville = ville
        self.adresse = adresse
        self.type_carburant = type_carburant
        self.prix_carburant = prix_carburant
        self.coordonnees = coordonnees
        self.services = []

    def ajouter_service(self, nom_service):
        self.services.append(nom_service)

    def service_disponible(self, nom_service: str) -> bool:
        return nom_service in self.services

    def rechercher_par_preference(self):
        pass