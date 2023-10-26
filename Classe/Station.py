class Station:
    def __init__(
        self,
        id_station,
        longitude,
        latitude,
        ville,
        adresse
    ):
        self.id_station = id_station
        self.longitude = longitude
        self.latitude = latitude
        self.ville = ville
        self.adresse = adresse
        self.services = []

    def ajouter_service(self, nom_service):
        self.service.append(nom_service)

    def service_disponible(self, nom_service: str) -> bool:
        service = True

        if nom_service not in self.service:
            service = False
            return service

        return service

    def rechercher_par_preference(self):
        pass