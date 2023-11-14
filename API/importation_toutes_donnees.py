import requests
import zipfile
import io
import xml.etree.ElementTree as ET
from Classe.Coordonnees import Coordonnees
from helper import trier, selectionner_n_premiers

url = "https://donnees.roulez-eco.fr/opendata/instantane"


#faire plusieurs fonctions selon les cas : si il met pas de filtres, je peux quand même gérer 
#faire deux fonctions (une pour filtrer, une pour rechercher par id)

def trouver_stations_par_filtres (n : int, services_recherches: list, carburants_recherches : list, coor_utilisateur: Coordonnees):
    url = "https://donnees.roulez-eco.fr/opendata/instantane"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            zip_content = response.content

            with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
                xml_file_name = "PrixCarburants_instantane.xml"

                if xml_file_name in zip_file.namelist():
                    xml_content = zip_file.read(xml_file_name).decode("latin-1")
                    root = ET.fromstring(xml_content)

                    # Créez une liste pour stocker les informations
                    ids = []
                    latitude = []
                    longitude = []
                    cp = []
                    # Services à rechercher
                    #services_recherches = ["Station de gonflage"]
                    #carburants_recherches = ["Gazole"]


                    # Parcourez tous les éléments <pdv> dans le XML
                    for pdv_element in root.findall(".//pdv"):
                        # Obtenez la liste des services pour la station
                        services = [service.text for service in pdv_element.findall(".//services/service")]
                        carburants = [carburant_element.get("nom") for carburant_element in pdv_element.findall(".//prix")]


                        # Vérifiez si les services recherchés sont présents dans la liste des services
                        if all(service in services for service in services_recherches):
                            if any(carburant in carburants_recherches for carburant in carburants):
                                pdv_id = pdv_element.get("id")
                                pdv_latitude = pdv_element.get("latitude")
                                pdv_longitude = pdv_element.get("longitude")
                                pdv_cp = pdv_element.get("cp")
                                ids.append(pdv_id)
                                latitude.append(pdv_latitude)
                                longitude.append(pdv_longitude)
                                cp.append(pdv_cp)
               
                    #print(len(longitude))
                    #print(len(ids))
                    #coor_utilisateur = Coordonnees(0,48.6428477,2.7143162)
                    coor_info = [Coordonnees(pdv_id, float(pdv_latitude)/100000, float(pdv_longitude)/100000) for pdv_id, pdv_latitude, pdv_longitude in zip(ids, latitude, longitude)]
                    #print(coor_info)

                    dist=[]
                    for x in coor_info:
                        y= x.dist(coor_utilisateur)
                        dist.append(y)
                    #print(dist)
               
                    print(len(coor_info))
               
                    dist_triee = trier(dist)

                    #print(dist_triee)
        

                    dist_triee_premiers = selectionner_n_premiers(n, dist_triee)
                    print(dist_triee_premiers)

        else:
            print("La requête a échoué avec le code de statut :", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Erreur de requête :", e)
    except ET.ParseError:
        print("Le contenu extrait n'est pas un fichier XML valide.")

trouver_stations_par_filtres(5, ["Station de gonflage"],["Gazole"], Coordonnees(0,48.6428477,2.7143162))