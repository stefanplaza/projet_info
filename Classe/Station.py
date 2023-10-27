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
<<<<<<< HEAD
        self.services = services 
        self.type_carburant = type_carburant, 
        self.prix_carburant = prix_carburant, 
        self.coordonnees = coordonnees
=======
        self.services = []

    def ajouter_service(self, nom_service):
        self.service.append(nom_service)

    def service_disponible(self, nom_service: str) -> bool:
        service = True

        if nom_service not in self.service:
            service = False
            return service

        return service
>>>>>>> 6cb2fd884b62c3fbe18e662164b556def7e1fda3

    def rechercher_par_preference(self):
        pass