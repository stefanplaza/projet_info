class Horaires:
    def __init__(self, ouverture, fermeture):
        """
        Initialise une instance de la classe Horaires avec des horaires d'ouverture et de fermeture.

        Args:
            ouverture (str): L'heure d'ouverture au format HH:MM (par exemple, "08:00").
            fermeture (str): L'heure de fermeture au format HH:MM (par exemple, "18:00").
        """
        self.ouverture = ouverture
        self.fermeture = fermeture
