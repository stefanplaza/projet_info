from InquirerPy import inquirer
from view.abstract_view import AbstractView
from view.session_view import Session
from projet_info.DAO.inscriptionDAO import DAO.inscriptionDAO
from ListesFavoritesView import ListesFavoritesView  # Assurez-vous de corriger le chemin d'importation

class MenuView(AbstractView):
    def __init__(self):
        # ... Vos autres méthodes d'initialisation restent inchangées

    def make_choice(self):
        while True:
            answers = inquirer.prompt(self.__questions)
            choice = answers["choice"]

            if choice == "Effectuer une recherche":
                # Ajoutez le code pour l'option "Effectuer une recherche"
                pass
            elif choice == "Consulter mes stations favorites":
                # Ajoutez le code pour l'option "Consulter mes stations favorites"
                pass
            elif choice == "Modifier/Supprimer mes stations favorites":
                # Ajoutez le code pour l'option "Modifier/Supprimer mes stations favorites"
                pass
            elif choice == "Créer une nouvelle liste de stations favorites":
                listes_favorites_view = ListesFavoritesView()
                listes_favorites_view.display_info()
                listes_favorites_view.make_choice()
            elif choice == "Déconnexion":
                Session().clear_session()
                from view.connexion_view import ConnexionView
                return ConnexionView()
