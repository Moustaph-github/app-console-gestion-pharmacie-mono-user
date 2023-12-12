""" La classe Produit """
# On importe les modules os et sys
from os import *
from sys import *
#Importation du module bdd
#from bdd import *
import bdd



class Produit:

    

    

    def __init__(self):
        
        self.nom = ""
        self.prix = 0.0
        #self.prisEncharge de type NUMERIC
        self.prisEncharge = 0
        self.type_prod = ""

    
    
    def saisie(self):
        self.nom = input("Entrez le nom du produit : ")
        self.prix = float(input("Entrer le prix du produit : "))
        #self.prisEncharge = bool(input("Entrez True or False : "))
        self.prisEncharge = int(input("Entrez 0 ou 1 : "))
        self.type_prod = input("Donnez type produit(medicament ou parapharma) : ")


    """ les getters """
    def getNom(self):
        return self.nom
    def getPrix(self):
        return self.prix
    def getPrisEnCharge(self):
        return self.prisEncharge
    def getTypeProd(self):
        return self.type_prod     

    """ Saisie de chaque entrée """
    def saisieNom(self):
        self.nom = input("Entrez le nom du produit : ")
        return self.nom
    def saisiePrix(self):
        self.prix = float(input("Entrer le prix du produit : "))
        return self.prix
    def saisiePrisEnCharge(self):
        self.prisEncharge = bool(input("Entrez True or False : "))
        return self.prisEncharge
    def saisieTypeProd(self):
        self.type_prod = input("Donnez type produit(m ou pp) : ")
        return self.type_prod
    
    def recupererSaisie(self):

        data = (self.nom,self.prix,self.prisEncharge,self.type_prod)
        return data

    def recupererSaisieModif(self):
        
        id = int(input("Veuillez donner l'identifiant du produit Pour la mise à jour du produit: "))
        data = (id,self.nom,self.prix,self.prisEncharge,self.type_prod)
        return data   
        
    """ Les Opérations aplliquées dans les produits """
    #Enregistrement de produits
    #Lister les produits
    #Suppression

    #Méthode création table
    def table(self):

        database = "gestionpharmacie"

        sql_create_produit_table = "create table produit(identifiant integer primary key autoincrement unique, nom text, prix float, prise_en_charge numeric, type_prod text)"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        if conn is not None:   
            #create produit tables
            bdd.bdd.create_table(conn, sql_create_produit_table)
        else:
            print("Error! cannot create the database connection.")
        
    #Enregistrement de produits

    def enregistrement(self):

        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #baseDonnees = bdd()
        sql = ''' INSERT INTO
              produit(nom,prix,prise_en_charge,type_prod)
              VALUES(?,?,?,?)
          '''
        #data = recupererSaisie()
        #p.table()
        Produit.table(self)

        nbproduit = int(input("Saisir le nombre de produit à enregistrer : "))
        i = 1
        
        while i <= nbproduit:
                   
            # Insertion de données
            with conn:          
                
                
                
                Produit.saisie(self)
                data = Produit.recupererSaisie(self)
                bdd.bdd.insert_data_table(conn,sql,data)
                print("Enregistrement validé !")
                
            i +=1    

    # Affichage des Produits    
    def affichageProduit(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        requete = ''' SELECT * FROM produit '''

        #Affichage des données de la table produit
        with conn:
            print("------------- Les produits du Stock -------------")
            bdd.bdd.select_all_data_table(conn,requete)

    
            
    # Suppression d'une entrée de la table produit
    def suppressionProduit(self):

        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Requete de suppression
        sql = 'DELETE FROM produit WHERE identifiant=?'
        #p.table()
        Produit.table(self)

        id = int(input("Veuillez donner l'identifiant du produit : "))

        with conn:
            bdd.bdd.delete_data_table(conn,sql,id)
            print("Produit Supprimé avec succés")
        

    
    
    # Recherche d'une entrée dans la table produit
    def rechercheProduit(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Requete de recherche
        requete = ''' SELECT * FROM produit WHERE identifiant=? '''
        #p.table()
        Produit.table(self)

        id = int(input("Veuillez donner l'identifiant du produit à recherché : "))

        with conn:
            bdd.bdd.search_data_table(conn,requete,id)
            print("Produit trouvé avec succés")
      
    #Méthode Mise à jour du produit
    def miseAJourProduit(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Curseur
        curseur=conn.cursor()
        
        #Choix de la modification à effectuer
        choixModif = int(input(" Que voulez vous modifié Tapez 1 : nom produit 2 : prix du produit 3 : type du produit : "))

        if choixModif in range(1,4):
            
            

            #Modification du nom du produit
            if choixModif == 1:
                
                identifiant = int(input("Donnez l'identifiant du produit : "))
                nom = Produit.saisieNom(self)
                data=[(nom, identifiant)]
                for enreg in data:
                    curseur.execute("update produit set nom = ? where identifiant = ?  ", enreg) 
                    conn.commit()
                    print(" Le nom du produit a été Modifié avec succes")


            #Modification du prix du produit
            if choixModif == 2:
                
               

               identifiant = int(input("Donnez l'identifiant du produit : "))
               prix = Produit.saisiePrix(self)
               data = [(prix, identifiant)]
               for enreg in data:
                           
                   curseur.execute("update produit set prix = ? where identifiant = ?  ", enreg) 
                   conn.commit()
                   print(" Le prix du produit a été Modifié avec succes")


            #Modification du type de produit
            if choixModif == 3:

               identifiant = int(input("Donnez l'identifiant du client : "))
               type_prod = Produit.saisieTypeProd(self)
               data=[(type_prod, identifiant)]
               for enreg in data:
                   
                   curseur.execute("update produit set type_prod = ? where identifiant = ?  ", enreg) 
                   conn.commit()
                   print(" Le type du produit a été Modifié avec succes") 


            

            

#if __name__ == "__main__":


    
    

    #p = Produit()
    #p.saisie()
    
    
    

            

    
    
        

    
    
    
    
    
