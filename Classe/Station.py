class Station:
    def __init__(
        self,
        id_station,
        longitude,
        latitude,
        ville,
        adresse,
        services, 
        type_carburant,
        prix_carburant, 
        coordonnees,
    ):
        self.id_station = id_station
        self.longitude = longitude
        self.latitude = latitude
        self.ville = ville
        self.adresse = adresse
        self.services = services 
        self.type_carburant = type_carburant, 
        self.prix_carburant = prix_carburant, 
        self.coordonnees = coordonnees

    def rechercher_par_preference(self):
        pass