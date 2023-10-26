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





