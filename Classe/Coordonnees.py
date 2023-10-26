import unittest
import math

class Coordonnees:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def dist(self, autre):
        # Convertir les latitudes et longitudes de degrés à radians
        lat1, lon1 = math.radians(self.latitude), math.radians(self.longitude)
        lat2, lon2 = math.radians(autre.latitude), math.radians(autre.longitude)
        
        # Calcul des différences de latitude et de longitude
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        # Appliquer la formule haversine
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        
        # Rayon de la Terre en kilomètres (par défaut)
        R = 6371.0  # En kilomètres
        
        # Calculer la distance
        distance = R * c
        
        return distance


class TestCoordonnees(unittest.TestCase):
    def test_dist_entre_meme_point(self):
        # Teste si la distance entre un point et lui-même est 0
        coord = Coordonnees(12.9716, 77.5946)
        resultat = coord.dist(coord)
        self.assertEqual(resultat, 0)

    def test_dist_entre_deux_points_identiques(self):
        # Teste si la distance entre deux points identiques est 0
        coord1 = Coordonnees(12.9716, 77.5946)
        coord2 = Coordonnees(12.9716, 77.5946)
        resultat = coord1.dist(coord2)
        self.assertEqual(resultat, 0)

    def test_dist_entre_deux_points_differents(self):
        # Teste la distance entre deux points différents
        coord1 = Coordonnees(12.9716, 77.5946)
        coord2 = Coordonnees(28.6139, 77.2090)
        # Calcul de la distance approximative entre ces deux points en km
        distance_attendue = 1739.0
        resultat = round(coord1.dist(coord2))
        self.assertAlmostEqual(resultat, distance_attendue, delta=1)

if __name__ == '__main__':
    unittest.main()



