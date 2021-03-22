-- Destruction des tables


DROP TABLE IF EXISTS Adresse;
DROP TABLE IF EXISTS Ville;
DROP TABLE IF EXISTS Logement;
DROP TABLE IF EXISTS Piece;
DROP TABLE IF EXISTS Type_Capteur;
DROP TABLE IF EXISTS Capteur;
DROP TABLE IF EXISTS Mesure;
DROP TABLE IF EXISTS Facture;


-- Création des tables

CREATE TABLE Ville (Code INTEGER PRIMARY KEY, Nom TEXT NOT NULL);
-- Ville avec son code postale

CREATE TABLE Adresse (id INTEGER PRIMARY KEY AUTOINCREMENT, Numero INTEGER NOT NULL, Voie TEXT NOT NULL, Nom_voie TEXT NOT NULL, Code INTEGER NOT NULL, FOREIGN KEY (Code) REFERENCES Ville(Code));
-- Adresse avec son id, son numéro, son type de voie, son nom de voie et son code postale, en référence à la table ville


CREATE TABLE Logement (id INTEGER PRIMARY KEY AUTOINCREMENT, Numero TEXT NOT NULL, IP TEXT NOT NULL, Date_insert TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, idAd INTEGER NOT NULL, FOREIGN KEY (idAd) REFERENCES Adresse(id));
-- Logement avec son id, son numéro de téléphone, son adresse IP, sa date d'insertion, et son adresse en référence à la table adresse

CREATE TABLE Piece (id INTEGER PRIMARY KEY AUTOINCREMENT, CoordX INTEGER NOT NULL, CoordY INTEGER NOT NULL, CoordZ INTEGER NOT NULL, Nom TEXT NOT NULL, idLog INTEGER NOT NULL, FOREIGN KEY (idLog) REFERENCES Logement(id));
-- Piece avec son id, ses coordonnées, son nom, et l'id du logement auquel il appartient

CREATE TABLE Type_Capteur (id INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT NOT NULL, Unite TEXT NOT NULL, Plage TEXT NOT NULL);
 -- Type de capteur avec son id, le nom du type de grandeur mesuré, l'unite et la plage de valeurs

CREATE TABLE Capteur (id INTEGER PRIMARY KEY AUTOINCREMENT, Reference TEXT NOT NULL, Port TEXT NOT NULL, Date_insert TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, idType INTEGER NOT NULL, idPiece INTEGER NOT NULL, FOREIGN KEY (idType) REFERENCES Type_Capteur(id), FOREIGN KEY (idPiece) REFERENCES Piece(id));
-- Capteur avec son id, sa référence, son port de communication avec le serveur, et sa date d'insertion et l'id de la piece en question

CREATE TABLE Mesure (id INTEGER PRIMARY KEY AUTOINCREMENT, Valeur INTEGER NOT NULL, Date_insert TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, idCap INTEGER NOT NULL, FOREIGN KEY (idCap) REFERENCES Capteur(id));
-- Mesure avec son id, sa valeur, sa date d'insertion, et son capteur associé

CREATE TABLE Facture (id INTEGER PRIMARY KEY AUTOINCREMENT, Type TEXT NOT NULL, Date_facture TIMESTAMP NOT NULL, Montant TEXT NOT NULL, Valeur TEXT NOT NULL, idLog INTEGER NOT NULL, FOREIGN KEY (idLog) REFERENCES Logement(id));
-- Facture avec son id, son type, sa date, son montant, la valeur consomée, et l'id du logement associé


INSERT INTO Ville (Code, Nom) VALUES ("94000", "Creteil");
INSERT INTO Ville (Code, Nom) VALUES ("75005", "Paris 5eme");

INSERT INTO Adresse (Numero, Voie, Nom_voie, Code) VALUES ("3", "Voie", "Felix Eboue", "94000");
INSERT INTO Adresse (Numero, Voie, Nom_voie, Code) VALUES ("5", "Place", "Jussieu", "75005");

INSERT INTO LOGEMENT (NUMERO, IP, idAD) VALUES ("0654321012", "123.123.123.123", "1");

INSERT INTO Piece (CoordX, CoordY, CoordZ, Nom, idLog) VALUES ("0", "0", "3", "Salon", "1");
INSERT INTO Piece (CoordX, CoordY, CoordZ, Nom, idLog) VALUES ("0", "1", "3", "Chambre", "1");
INSERT INTO Piece (CoordX, CoordY, CoordZ, Nom, idLog) VALUES ("1", "0", "3", "Cuisine", "1");
INSERT INTO Piece (CoordX, CoordY, CoordZ, Nom, idLog) VALUES ("1", "1", "3", "Salle de bain", "1");

INSERT INTO Type_Capteur (Nom , Unite, Plage) VALUES ("Temperature", "°C", "-10;+50");
INSERT INTO Type_Capteur (Nom , Unite, Plage) VALUES ("Humidite", "%", "0;100");
INSERT INTO Type_Capteur (Nom , Unite, Plage) VALUES ("Luminosite", "Lux", "0;500");
INSERT INTO Type_Capteur (Nom , Unite, Plage) VALUES ("Son", "dB", "35;130");


INSERT INTO Capteur (Reference, Port, idType, idPiece) VALUES ("d5f4zs1c8e", "8711", "1", "2");
INSERT INTO Capteur (Reference, Port, idType, idPiece) VALUES ("f5e8r7s4g1", "8666", "4", "1");

INSERT INTO Capteur (Reference, Port, idType, idPiece) VALUES ("akfg5u8dk5", "8123", "2", "3");
INSERT INTO Capteur (Reference, Port, idType, idPiece) VALUES ("d5g6d8citm", "8321", "3", "4");
INSERT INTO Capteur (Reference, Port, idType, idPiece) VALUES ("sp8mg93u4v", "8999", "3", "1");

INSERT INTO Mesure (Valeur, idCap) VALUES ("19", "1");
INSERT INTO Mesure (Valeur, idCap) VALUES ("25", "1");
INSERT INTO Mesure (Valeur, idCap) VALUES ("66", "2");
INSERT INTO Mesure (Valeur, idCap) VALUES ("42", "2");

INSERT INTO Mesure (Valeur, idCap) VALUES ("50", "3");
INSERT INTO Mesure (Valeur, idCap) VALUES ("200", "4");
INSERT INTO Mesure (Valeur, idCap) VALUES ("300", "5");
INSERT INTO Mesure (Valeur, idCap) VALUES ("400", "5");


INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/01/2020", "38.25E", "12.75m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/02/2020", "35E", "11.67m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/03/2020", "30E", "10m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/04/2020", "20E", "6.67m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/05/2020", "23E", "7.67m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/06/2020", "22E", "7.33m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/07/2020", "18E", "6m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/08/2020", "12E", "4m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/09/2020", "13E", "4.33m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/10/2020", "11E", "3.67m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/11/2020", "14E", "4.67m3", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Eau", "19/12/2020", "7.2E", "2.4m3", "1");


INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/01/2020", "40E", "266.67kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/02/2020", "38E", "253.33kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/03/2020", "34E", "226.67kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/04/2020", "35E", "233.33kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/05/2020", "33E", "220kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/06/2020", "30E", "200kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/07/2020", "28E", "186.67kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/08/2020", "27E", "180kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/09/2020", "29E", "193.33kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/10/2020", "25E", "166.67kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/11/2020", "26E", "173.33kWh", "1");
INSERT INTO Facture (Type, Date_facture, Montant, Valeur, idLog) VALUES ("Electricite", "19/12/2020", "20E", "133.33kWh", "1");




SELECT * FROM Ville;
SELECT * FROM Adresse;
SELECT * FROM LOGEMENT;
SELECT * FROM Piece;
SELECT * FROM Type_Capteur;
SELECT * FROM Capteur;
SELECT * FROM Mesure;
SELECT * FROM Facture;
