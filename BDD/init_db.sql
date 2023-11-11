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
    mdp text NOT NULL
);