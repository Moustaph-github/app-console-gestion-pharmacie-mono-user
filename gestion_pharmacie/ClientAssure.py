""" Module du client assuré . Cette classe hérite de Client """
# Importer les modules os et sys
from os import *
from sys import *
# Importer notre classe bdd gestion de notre base de données gestionpharmacie
import bdd
# Impoter la classe Client
from Client import *
#Importation module datetime
#from datetime import datetime, date, time
import datetime

 
# Importer la classe Client
from Client import *

class ClientAssure(Client):

    def __init__(self):

        Client.__init__(self)
        self.num_police = 0
        self.nom_assureur = ""
        #On initialise les deux dates (debut et fin)
        self.date_debut = datetime.date(2000,1,1)
        self.date_fin = datetime.date(200,1,1)

        

    #Méthode de saisie des données du client assuré
    def saisieClientAssure(self):
        #Client.saisieClient(self)
        Client.saisieNom(self)
        Client.saisiePrenom(self)
        Client.saisieGenre(self)
        Client.saisieAdresse(self)
        Client.saisieTelephone(self)
        Client.saisieEmail(self)
        Client.saisieTypeClient(self)
        self.num_police = int(input("Donnez le numéro de police : "))
        self.nom_assureur = input("Donnez le nom de l'assureur : ")
        print("Donnez la date de début de l'assurance")
        year = int(input("Saisir année : "))
        month = int(input("Saisir mois entre 1 et 12 : "))
        day = int(input("Saisir jour 1 et 30 : "))       
        self.date_debut = datetime.date(year,month,day)
        print("Donnez la date de fin de l'assurance")
        year = int(input("Saisir année : "))
        month = int(input("Saisir mois entre 1 et 12 : "))
        day = int(input("Saisir jour entre 1 et 30 : ")) 
        self.date_fin = datetime.date(year,month,day)

   

    def recupereSaisieClientAssure(self):

        #dataClient = Client.recupererSaisieClient(self)
        nom = Client.getNom(self)
        prenom = Client.getPrenom(self)
        genre = Client.getGenre(self)
        adresse = Client.getAdresse(self)
        telephone = Client.getTelephone(self)
        email = Client.getEmail(self)
        type_client = Client.getTypeClient(self)
        
        #num_police = Client.getNumPolice(self)
        
        data = (nom,prenom,genre,adresse,telephone,email,type_client,self.num_police,self.nom_assureur,self.date_debut,self.date_fin)
        return data

    """ Les différentes de la classe ClientAssure """

    #Méthode création table
    def table(self):

        database = "gestionpharmacie"

        sql_create_client_table ='''CREATE TABLE clientassure(
                                    
                                    nom TEXT NOT NULL,
                                    prenom TEXT NOT NULL,
                                    genre TEXT NOT NULL,
                                    adresse TEXT NOT NULL,
                                    telephone INTEGER,
                                    email TEXT NOT NULL,
                                    type_client TEXT NOT NULL,
                                    num_police INTEGER,
                                    nom_assureur TEXT NOT NULL,
                                    date_debut DATE,
                                    date_fin DATE)
                                '''

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        if conn is not None:   
            #create produit tables
            bdd.bdd.create_table(conn, sql_create_client_table)
        else:
            print("Error! cannot create the database connection.")

    #Enregistrement de produits

    def enregistrementClientAssure(self):

        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #baseDonnees = bdd()
        sql = ''' INSERT INTO
              clientassure(nom,prenom,genre,adresse,telephone,email,type_client,num_police,nom_assureur,date_debut,date_fin)
              VALUES(?,?,?,?,?,?,?,?,?,?,?)
          '''
        #data = recupererSaisie()
        #c.table()
        ClientAssure.table(self)

        nbclientassure = int(input("Saisir le nombre de client assuré à enregistrer : "))
        i = 1
        
        while i <= nbclientassure:
                   
            # Insertion de données
            with conn:          

                ClientAssure.saisieClientAssure(self)
                #data = c.recupereSaisieClientAssure()
                data = ClientAssure.recupereSaisieClientAssure(self)
                bdd.bdd.insert_data_table(conn,sql,data)
                print("Enregistrement validé !")
                
            i +=1    

    """Méthode affichage de l'ensemble des clients assurés """
    def affichageClient(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        requete = ''' SELECT * FROM clientassure '''

        #Affichage des données de la table clientassure
        with conn:
            print("------------- Les clients assurés enregistrés -------------")
            bdd.bdd.select_all_data_table(conn,requete)
            

    # Suppression d'une entrée de la table client
    def suppressionClient(self):

        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Requete de suppression
        sql = 'DELETE FROM clientassure WHERE num_police=?'
        #c.table()
        ClientAssure.table(self)

        id = int(input("Veuillez donner l'identifiant du client assuré à supprimer : "))

        with conn:
            bdd.bdd.delete_data_table(conn,sql,id)
            print("Client Supprimé avec succés")

    # Recherche d'une entrée dans la table clientassure
    def rechercheClientAssure(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Requete de recherche
        requete = ''' SELECT * FROM clientassure WHERE num_police=? '''
        #c.table()
        ClientAssure.table(self)

        num_police = int(input("Veuillez donner le numéro police du client assuré à recherché : "))

        with conn:
            bdd.bdd.search_data_table(conn,requete,num_police)
            print("Client trouvé avec succés")

        

        
    

#if __name__ == "__main__":

    #c = ClientAssure()
    #c.saisieClientAssure()
    #data = c.recupereSaisieClientAssure()
    #print(data)
    
    #c.enregistrementClientAssure()
    #c.affichageClient()
    #c.rechercheClientAssure()
    #c.suppressionClient()
    #c.affichageClient()
