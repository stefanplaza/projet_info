
import requests
import zipfile
import io
import xml.etree.ElementTree as ET

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
                cp=[]


                # Parcourez tous les éléments <pdv> dans le XML
                for pdv_element in root.findall(".//pdv"):
                    pdv_id = pdv_element.get("id")
                    pdv_latitude = pdv_element.get("latitude")
                    pdv_longitude = pdv_element.get("longitude")
                    pdv_cp = pdv_element.get("cp")
                    ids.append(pdv_id)
                    latitude.append(pdv_latitude)
                    longitude.append(pdv_longitude)
                    cp.append(pdv_cp)

                print(ids)
                #print(latitude)
                #print(longitude)
                #print(cp)
               
            else:
                print(f"Le fichier {xml_file_name} n'existe pas dans le fichier zip.")

    else:
        print("La requête a échoué avec le code de statut :", response.status_code)

except requests.exceptions.RequestException as e:
    print("Erreur de requête :", e)
except ET.ParseError:
    print("Le contenu extrait n'est pas un fichier XML valide.")