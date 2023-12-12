""" La classe AchatClient """
# On importe les modules os et sys
from os import *
from sys import *
#Importation du module bdd
#from bdd import *
import bdd
#Importation module datetime
#from datetime import datetime, date, time
import datetime
#Module time
import time
#Importation de module Produit
import Produit
#Importation du module Client
import Client
# Importer le module sqlite3
import sqlite3
from sqlite3 import Error


class AchatClient:

    def __init__(self):

        #Date achat 
        #self.date_achat = date(1000,1,1)
        self.date_achat = ""
        #Heure achat
        #self.heure_achat = time(0,0,0)
        self.heure_achat = ""
        #Nom produit acheté
        self.nom_produit = ""
        #Prix unitaire du produit acheté
        self.prix_unitaire = 0.0
        #Nombre exemplaire du produit acheté
        self.nbre_exemplaire_pro = 0
        #Prix total du produit acheté self.prix_unitaire * self.nbre_exemplaire_pro
        self.prix_total_prod = 0.0
        #Montant de la facture
        self.montant_facture = 0.0
        #Identifiant du Client correspondant
        self.id_client = 0
        #Identifiant du Produit correspondant
        self.id_produit = 0
        #Type Client
        self.type_client = ""



    """ Méthode de Saisie des Achats """
    def saisieDate(self):  
        #year = int(input("Saisir année : "))
        #month = int(input("Saisir mois : "))
        #day = int(input("Saisir jour : "))       
        #self.date_achat = date(year,month,day)
        self.date_achat = datetime.date.today()
        return self.date_achat

    def saisieHeure(self):
        #hour = int(input("Saisir l'heure de l'achat : "))
        #minute = int(input("Saisir la minute: "))
        #second = int(input("Saisir la seconde : "))
        #self.heure_achat = time(hour,minute,second)
        self.heure_achat = time.strftime("%H:%M:%S")
        
        return self.heure_achat

    def saisieNomProduit(self):
        self.nom_produit = input("Saisissez le nom du produit : ")
        return self.nom_produit

    def saisiePrixUnitaire(self):
        self.prix_unitaire = float(input("Donnez le prix unitaire : "))
        return self.prix_unitaire

    def saisieNbreExemplaire(self):
        self.nbre_exemplaire_pro = int(input("Saisissez le nombre d'exemplaires du produit : "))
        return self.nbre_exemplaire_pro 

    def saisieIdClient(self):
        self.id_client = int(input("Saisissez l'identifiant du client correspondant : "))
        return self.id_client
    
    def saisieIdProduit(self):
        self.id_produit = int(input("Saisissez l'identifiant du produit correspondant : "))
        return self.id_produit
    def saisieTypeClient(self):
        self.type_client = input("Donnez le numéro de police client assure/client non assure/client employe assure/client employe non assure : ")
        return self.type_client
    
    """ Les getters """
    def getDate(self):
        return self.date_achat

    def getHeure(self):
        return self.heure_achat 

    def getNomProduit(self):
        return self.nom_produit

    def getPrixUnitaire(self):
        return self.prix_unitaire

    def getNbreExemplaire(self):
        return self.nbre_exemplaire_pro

    def getIdClient(self):
        return self.id_client

    def getIdProduit(self):
        return self.id_produit
        
        
        
   #Méthode création table
    def table(self):

        database = "gestionpharmacie"

        sql_create_achat_table ='''CREATE TABLE achat(
                                    
                                    id_achat INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                    date_achat DATE,
                                    heure_achat TIME,
                                    nom_produit TEXT NOT NULL,
                                    prix_unitaire FLOAT,
                                    nbre_exemplaire_pro INTEGER,
                                    prix_total_prod FLOAT,
                                    montant_facture FLOAT,
                                    id_client INTEGER,
                                    id_produit INTEGER,
                                    type_client TEXT NOT NULL,
                                    FOREIGN KEY (id_client) REFERENCES client(id_client),
                                    FOREIGN KEY (id_produit) REFERENCES produit(identifiant) )
                                    
                                '''

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        if conn is not None:   
            #create produit tables
            bdd.bdd.create_table(conn, sql_create_achat_table)
        else:
            print("Error! cannot create the database connection.")


    #Enregistrement de achats

    def EnregistrementAchat(self):
        #import datetime
        #self.montant_achat = 0.0
        #self.prix_total_prod = 0.0
        
        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Curseur
        curseur=conn.cursor()

        AchatClient.table(self)

        

        Produit.Produit.affichageProduit(self)
        type_Client = input("Entrer le type de client 'client non assure/client employe assure': ")
        if type_Client == "client non assure":
            
            nbr_produit = int(input("Veuillez entrer  le nombre de produit a achete: "))
            i = 1
            while i <= nbr_produit:               
                #date_achat = datetime.datetime.today()
                self.date_achat = AchatClient.saisieDate(self)
                #heure_achat = datetime.datetime.today()
                self.heure_achat = AchatClient.saisieHeure(self)
                print("Produit",i)
                self.nom_produit = AchatClient.saisieNomProduit(self)
                self.prix_unitaire = AchatClient.saisiePrixUnitaire(self)
                self.nbre_exemplaire_pro = AchatClient.saisieNbreExemplaire(self)
                self.prix_total_prod = self.prix_unitaire*self.nbre_exemplaire_pro            
                self.montant_facture += self.prix_total_prod
                self.id_client = AchatClient.saisieIdClient(self)
                self.id_produit = AchatClient.saisieIdProduit(self)
                #self.type_client = a.saisieTypeClient()
                self.type_client = "client non assure"
                if self.montant_facture >= 50000:
                    self.montant_facture = self.montant_facture-(self.montant_facture*0.1)
                    #self.id_client = a.saisieIdClient()
                    #self.id_prduit = a.saisieIdProduit()  
                #i +=1      
                    data=[(self.date_achat,self.heure_achat,self.nom_produit,self.prix_unitaire,self.nbre_exemplaire_pro,self.prix_total_prod,self.montant_facture,self.id_client,self.id_produit,self.type_client)]
                else:
                    data=[(self.date_achat,self.heure_achat,self.nom_produit,self.prix_unitaire,self.nbre_exemplaire_pro,self.prix_total_prod,self.montant_facture,self.id_client,self.id_produit,self.type_client)]
                print(data)
                """sql = insert into
                        achat(date_achat,heure_achat,nom_produit,prix_unitaire,nbre_exemplaire_pro,prix_total_prod,montant_facture,id_client,id_produit,type_client)
                        values(?,?,?,?,?,?,?,?,?,?)"""
                for enreg in data:
                    curseur.execute("insert into achat(date_achat,heure_achat,nom_produit,prix_unitaire,nbre_exemplaire_pro,prix_total_prod,montant_facture,id_client,id_produit,type_client)values(?,?,?,?,?,?,?,?,?,?)",enreg)
                    conn.commit()
                    print("Achat Ajouté avec succes")
                
                i +=1    
                
        elif type_Client == "client employe assure":
            type_produit = input("Entrer le type de produit 'parapharma': ")
            if type_produit == "parapharma":
                nbr_produit = int(input("Veuillez entrer  le nombre de produit a achete: "))
            i = 1
            while i <= nbr_produit:               
                self.date_achat = AchatClient.saisieDate(self)
                self.heure_achat = AchatClient.saisieHeure(self)
                print("Produit",i)
                self.nom_produit = AchatClient.saisieNomProduit(self)
                self.prix_unitaire = AchatClient.saisiePrixUnitaire(self)
                self.nbre_exemplaire_pro = AchatClient.saisieNbreExemplaire(self)
                self.prix_total_prod = self.prix_unitaire*self.nbre_exemplaire_pro            
                self.montant_facture += self.prix_total_prod
                self.montant_facture = self.montant_facture-(self.montant_facture*0.05)
                self.id_client = AchatClient.saisieIdClient(self)
                self.id_produit = AchatClient.saisieIdProduit(self)
                #self.type_client = a.saisieTypeClient()
                self.type_client = "client employe assure" 
                i +=1      
                data=[(self.date_achat,self.heure_achat,self.nom_produit,self.prix_unitaire,self.nbre_exemplaire_pro,self.prix_total_prod,self.montant_facture,self.id_client,self.id_produit,self.type_client)]
                #print(data)
                """sql = '''insert into
                        achat(date_achat,heure_achat,nom_produit,prix_unitaire,nbre_exemplaire_pro,prix_total_prod,montant_facture,id_client,id_produit)
                        values(?,?,?,?,?,?,?,?,?)'''"""

                for enreg in data:
                    curseur.execute("insert into achat(date_achat,heure_achat,nom_produit,prix_unitaire,nbre_exemplaire_pro,prix_total_prod,montant_facture,id_client,id_produit,type_client)values(?,?,?,?,?,?,?,?,?,?)",enreg)
                    conn.commit()
                    print("Achat Ajouté avec succes")


        else:
            type_produit = input("Entrer le type de produit 'parapharma': ")
            if type_produit == "parapharma":
                nbr_produit = int(input("Veuillez entrer  le nombre de produit a achete: "))
            i = 1
            while i <= nbr_produit:               
                self.date_achat = AchatClient.saisieDate(self)
                self.heure_achat = AchatClient.saisieHeure(self)
                print("Produit",i)
                self.nom_produit = AchatClient.saisieNomProduit(self)
                self.prix_unitaire = AchatClient.saisiePrixUnitaire(self)
                self.nbre_exemplaire_pro = AchatClient.saisieNbreExemplaire(self)
                self.prix_total_prod = self.prix_unitaire*self.nbre_exemplaire_pro            
                self.montant_facture += self.prix_total_prod
                #self.montant_facture = self.montant_facture-(self.montant_facture*0.05)
                self.id_client = AchatClient.saisieIdClient(self)
                self.id_produit = AchatClient.saisieIdProduit(self)
                self.type_client = AchatClient.saisieTypeClient(self)
                i +=1      
                data=[(self.date_achat,self.heure_achat,self.nom_produit,self.prix_unitaire,self.nbre_exemplaire_pro,self.prix_total_prod,self.montant_facture,self.id_client,self.id_produit,self.type_client)]
                #print(data)
                """sql = '''insert into
                        achat(date_achat,heure_achat,nom_produit,prix_unitaire,nbre_exemplaire_pro,prix_total_prod,montant_facture,id_client,id_produit)
                        values(?,?,?,?,?,?,?,?,?)'''"""

                for enreg in data:
                    curseur.execute("insert into achat(date_achat,heure_achat,nom_produit,prix_unitaire,nbre_exemplaire_pro,prix_total_prod,montant_facture,id_client,id_produit,type_client)values(?,?,?,?,?,?,?,?,?,?)",enreg)
                    conn.commit()
                    print("Achat Ajouté avec succes")
                
    
            
                

    #Affichage achats
    def affichageAchat(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        requete = ''' select * from achat'''

        #Affichage des données de la table achat
        with conn:
            print("------------- Les achats effectués avec succés -------------")
            bdd.bdd.select_all_data_table(conn,requete)

    #Achat d'un client donné
    def AfficheClientAchat(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)


        #Curseur
        curseur=conn.cursor()

        curseur.execute(" select prenom, nom from client INNER JOIN achat ON achat.id_client = client.id_client")
        conn.commit()
        for i in curseur:
            print(i)

    #Achat Type Client
    def AfficheTypeClientAchat(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)


        #Curseur
        curseur=conn.cursor()

        curseur.execute(" select prenom, nom from client INNER JOIN achat ON achat.type_client LIKE client.type_client")
        conn.commit()
        for i in curseur:
            print(i)
    
            

    
#if __name__ == "__main__":

    #a = AchatClient()
    
    #produit_achete = []
    
    #data = a.saisieAchat(produit_achete)
    #a.EnregistrementAchat()
    #a.affichageAchat()
    #a.AfficheClientAchat()
    #a.AfficheClientAchat()
    #data = a.recupereAchat()

    #print(data)

    
