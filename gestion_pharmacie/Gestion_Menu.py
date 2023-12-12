# Importer le module sqlite3
import sqlite3
from sqlite3 import Error

""" Les bibliothéques standards os et sys """
from os import *
from sys import *

""" Importation des différents modules du projet """
#Module Client
import Client
#Module Produit
import Produit
#Module ClientAssure
import ClientAssure
#Module AchatClient
import AchatClient
#Module bdd: Gestion de la base de données
import bdd






print("\n\t\t***********************************************")
print("\n\t\t\t\t MENU PRINICIPAL:")
print("\n\t\t***********************************************")
print("\t\t\t 1- Gestion des Clients\n","\t\t\t 2- Gerer Médicament et Produit\n","\t\t\t 3- Gestion achats du client\n","\t\t\t 4- Etat des ventes\n")
print("\t\t***********************************************")
try:
        choix=int(input("Entrez votre choix: "))
        if choix in range(1,4):
            """ Menu Client et Client Assure """    
            if choix==1:
                    print("\n\t\t***********************************************")
                    print("\t\t\t 1- Client \n","\t\t\t 2- Client Assuré\n","\t\t\t 3- Retour Au Menu Principal")
                    print("\t\t***********************************************")
                    gcc=int(input("Entrez votre choix: "))
                        
                    """ Opérations sur Menu Client """
                    if gcc == 1:
                        print("\n\t\t***********************************************")
                        print("\t\t\t MENU CLIENT")
                        print("\t\t\t 1- Ajouter\n","\t\t\t 2- Suppression\n","\t\t\t 3- Recherche\n","\t\t\t 4- Mise à Jour")
                        print("\n\t\t***********************************************")
                        choixClient = int(input("Entrez votre choix: "))
                        if choixClient in range(1,5):
                            if choixClient == 1:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t AJOUTER CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = Client.Client()
                                c.enregistrement()
                                c.affichageClient()
                            if choixClient == 2:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t SUPPRESSION CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = Client.Client()
                                c.affichageClient()
                                c.suppressionClient()
                                c.affichageClient()
                            if choixClient == 3:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t RECHERCHE CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = Client.Client()
                                c.affichageClient()
                                c.rechercheClient()
                            if choixClient == 4:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t MISE A JOUR CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = Client.Client()
                                c.affichageClient()
                                c.miseAJourClient()
                                c.affichageClient()
                                
                                
                                
                                
                                                       
                            
                    """Opération sur Menu Client Asuure """
                    if gcc==2:
                        print("\n\t\t***********************************************")
                        print("\t\t\t MENU CLIENT ASSURE")
                        print("\t\t\t 1- Ajouter\n","\t\t\t 2- Suppression\n","\t\t\t 3- Recherche\n","\t\t\t 4- Mise à Jour")
                        print("\n\t\t***********************************************")
                        choixClient = int(input("Entrez votre choix: "))
                        if choixClient in range(1,5):
                            if choixClient == 1:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t AJOUTER CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = ClientAssure.ClientAssure()
                                c.enregistrementClientAssure()
                                c.affichageClient()
                            if choixClient == 2:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t SUPPRESSION CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = ClientAssure.ClientAssure()
                                c.affichageClient()
                                c.suppressionClient()
                                c.affichageClient()
                            if choixClient == 3:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t RECHERCHE CLIENT")
                                print("\t\t-----------------------------------------------")
                                c = ClientAssure.ClientAssure()
                                c.affichageClient()
                                c.rechercheClientAssure()
                                c.affichageClient()
                            if choixClient == 4:
                                print("\n\t\t-----------------------------------------------")
                                print("\t\t\t\t MISE A CLIENT")
                                print("\t\t-----------------------------------------------")
                        
                        
                        

                                    
                     
                          
            elif choix==2:
                print("\n\t\t***********************************************")
                print("\n\t\t GESTION DES MEDICAMENTS ET DES PRODUITS PARAPHARMACIE:")
                print("\n\t\t***********************************************")
                print("\t\t\t 1- Ajouter produit\n","\t\t\t 2- Supprimer produit\n","\t\t\t 3- Rechercher produit\n","\t\t\t 4- Modifier produit")
                print("\t\t***********************************************")
                gcc=int(input("Entrez votre choix: "))
                """ Ajouter produit """
                if gcc == 1:
                    print("\n\t\t-----------------------------------------------")
                    print("\t\t\t\t AJOUTER UN PRODUIT ")
                    print("\t\t-----------------------------------------------")
                    p = Produit.Produit()
                    p.enregistrement()
                    p.affichageProduit()
                """Supprimer un produit """    
                if gcc == 2:
                    print("\n\t\t-----------------------------------------------")
                    print("\t\t\t\t SUPPRIMER UN PRODUIT")
                    print("\t\t-----------------------------------------------")
                    p = Produit.Produit()
                    p.affichageProduit()
                    p.suppressionProduit()
                    p.affichageProduit()
                """Recherche produit """    
                if gcc == 3:
                    print("\n\t\t-----------------------------------------------")
                    print("\t\t\t\t RECHERCHE PRODUIT")
                    print("\t\t-----------------------------------------------")
                    p = Produit.Produit()
                    p.affichageProduit()
                    p.rechercheProduit()
                """Mise à jour produit """    
                if gcc == 4:
                    print("\n\t\t-----------------------------------------------")
                    print("\t\t\t\t MISE A JOUR D'UN PRODUIT")
                    print("\t\t-----------------------------------------------")
                    p = Produit.Produit()
                    p.affichageProduit()
                    p.miseAJourProduit()
                    p.affichageProduit()
                   
            elif choix==3:
                    
                    print("\n\t\t***********************************************")
                    print("\t\t\t 1- Effectuez Achat\n","\t\t\t 2- Détail Achat\n","\t\t\t 3- Retour Au Menu Principal")
                    print("\t\t***********************************************")
                    gcc=int(input("Entrez votre choix: "))

                    if gcc == 1:
                            
                            print("\n\t\t-----------------------------------------------")
                            print("\t\t\t\t EFFECTUER UN ACHAT")
                            print("\t\t-----------------------------------------------")
                            p = Produit.Produit()
                            p.affichageProduit()
                            a = AchatClient.AchatClient()
                            a.EnregistrementAchat()
                            a.affichageAchat()
                            
                            

                    if gcc == 2:

                            print("\n\t\t-----------------------------------------------")
                            print("\t\t\t\t DETAIL ACHAT")
                            print("\t\t-----------------------------------------------")

                            a = AchatClient.AchatClient()

                            print("\t\t------------- AFFICHAGE DES ACHATS EFFECTUES ET LEURS CLIENTS RESPECTIFS -------------------")
                            a.affichageAchat()
                            a.AfficheClientAchat()
                            
                            
                            
                            
                            
        elif choix==4:

                print("\n\t\t-----------------------------------------------")
                print("\t\t\t\t ETAT DES VENTES")
                print("\t\t-----------------------------------------------")

                a = AchatClient.AchatClient()

                print("\t\t------------- AFFICHAGE DES ACHATS EFFECTUES  -------------------")
                a.affichageAchat()
                print("\t\t------------- LISTE DES CLIENTS (Type Client) QUI ONT EFFECTUES DES ACHATS   -------------------")
                a.AfficheClientAchat()
                print("\t\t-------------------     -------------------------     ------------------------------------")
                a.AfficheTypeClientAchat()
                
                

                

                
                    
                    
            
except ValueError:
    print("La valeur saisie n'est pas bonne")
#return choix
    
#if __name__=="__main__":
    #menu()
    

