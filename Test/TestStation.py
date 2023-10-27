import unittest
from Classe.Station import Station

class TestStation(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets Station pour les tests
        self.station = Station(
            id_station=1,
            longitude=12.9716,
            latitude=77.5946,
            ville="Rennes",
            adresse="Breizh street"
        )
        self.station.ajouter_service("Restauration")
        self.station.ajouter_service("Sanitaire")

    def test_service_disponible(self):
        # Teste si le service ajouté est disponible dans la station
        self.assertTrue(self.station.service_disponible("Restauration"))
        self.assertTrue(self.station.service_disponible("Sanitaire"))
        self.assertFalse(self.station.service_disponible("Lavage_voiture"))

if __name__ == '__main__':
    unittest.main()