import math

class Coordonnees:
    def __init__(self, latitude, longitude):
        """
        Initialise une instance de la classe Coordonnees avec des coordonnées de latitude et de longitude.
    
        Args:
            latitude (float): La latitude en degrés.
            longitude (float): La longitude en degrés.
        """
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"ID utilisateur: {self._id_utilisateur}, mot de passe : {self._mot_de_passe}"

         """
        Retourne une représentation sous forme de chaîne de caractères de l'objet Utilisateur.

        Returns:
            str: Une chaîne de caractères représentant l'ID de l'utilisateur et son mot de passe.
        """     

    def dist(self, autre):
        """
        Calcule la distance entre deux points géographiques en utilisant la formule de la haversine.

        Args:
            autre (Coordonnees): Les coordonnées de l'autre point géographique.

        Returns:
            float: La distance en kilomètres entre les deux points géographiques.
        """
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
