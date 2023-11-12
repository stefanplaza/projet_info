DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;

--------------------------------------------------------------
-- Les stations
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.stations CASCADE ;
CREATE TABLE projet.stations (
    id_station text PRIMARY KEY,
    longitude text NOT NULL,
    latitude text NOT NULL,
    adresse text NOT NULL,
    ville text NOT NULL,
    services text,
    type_carburant text,
    prix_carburant text, 
    coordonnees text NOT NULL
);


--------------------------------------------------------------
-- Les services
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.utilisateur;

CREATE TABLE projet.utilisateur (
    id_utilisateur text PRIMARY KEY,
    nom_utilisateur text NOT NULL,
    mdp text NOT NULL
);

--------------------------------------------------------------
-- Les listes des stations
--------------------------------------------------------------

DROP TABLE IF EXISTS projet.listes;

CREATE TABLE projet.listes (
    id_liste text PRIMARY KEY,
    id_utilisateur text REFERENCES projet.utilisateur(id_utilisateur),
    nom_liste text UNIQUE NOT NULL
);

--------------------------------------------------------------
-- Le contenu des listes des stations
--------------------------------------------------------------


DROP TABLE IF EXISTS projet.contenu_liste;

CREATE TABLE projet.contenu_liste (
    id_liste text REFERENCES projet.listes(id_liste),
    id_stations text 
);