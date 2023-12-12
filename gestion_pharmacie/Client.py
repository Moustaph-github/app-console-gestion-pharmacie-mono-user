""" La classe Client """
# Importe les modules os et sys
""" La Classe Client """
from os import *
# On importe les modules os et sys
from os import *
from sys import *
#Importation du module bdd
#from bdd import *
import bdd


class Client:
    

    """def __init__(self,nom,prenom,genre,adresse,telephone,email):

        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.adresse = adresse
        self.telephone = telephone
        self.email = email"""

    def __init__(self):

        self.nom = ""
        self.prenom = ""
        self.genre = ""
        self.adresse = ""
        self.telephone = ""
        self.email = ""
        self.type_client = ""

    def saisieClient(self):
        self.nom = input("Nom du Client : ")
        self.prenom = input("Prénom : : ")
        self.genre = input("Genre (M/F) : ")
        self.adresse = input("Donnez son Adresse : ")
        self.telephone = int(input("Entrez son numéro de téléphone : "))
        self.email = input("Donnez son email : ")
        self.type_client = input("Donnez le type de client ---> non assure/client employe assure/client employe non assure : ")
        

    def recupererSaisieClient(self):

        data = (self.nom,self.prenom,self.genre,self.adresse,self.telephone,self.email,self.type_client)
        return data    
    """ Les getters """
    def getNom(self):
        return self.nom
    def getPrenom(self):
        return self.prenom
    def getGenre(self):
        return self.genre
    def getAdresse(self):
        return self.adresse
    def getTelephone(self):
        return self.telephone
    def getEmail(self):
        return self.email
    def getTypeClient(self):
        return self.type_client
    

    

    """ Les Méthodes de saisie """
    def saisieNom(self):
        self.nom = input("Nom du Client : ")
        return self.nom

    def saisiePrenom(self):
        self.prenom = input("Prénom du Client : ")
        return self.prenom

    def saisieGenre(self):
        self.genre = input("Genre (M/F) : ")
        return self.genre

    def saisieAdresse(self):
        self.adresse = input("Donnez son Adresse : ")
        return self.adresse

    def saisieTelephone(self):
        self.telephone = int(input("Entrez son numéro de téléphone : "))
        return self.telephone

    def saisieEmail(self):
        self.email = input("Donnez son email : ")
        return self.email

    """def saisieTypeClient(self):
        self.type_client = input("Donnez le numéro de police client assure/client non assure/client employe assure/client employe non assure : ")
        return self.type_client"""

    def saisieTypeClient(self):
        self.type_client = "client assure"
        return self.type_client
        
        
    
        

    """ Les Opérations aplliquées dans les produits """
    #Enregistrement de produits
    #Lister les produits
    #Suppression

    #Méthode création table
    def table(self):

        #Nom de ma base de données
        database = "gestionpharmacie"

        sql_create_produit_table ="create table client(id_client integer primary key autoincrement unique,nom text,prenom text,genre text,adresse text,telephone integer,email text,type_client text)"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        if conn is not None:   
            #create produit tables
            bdd.bdd.create_table(conn, sql_create_produit_table)
        else:
            print("Error! cannot create the database connection.")

    #Enregistrement de clients

    def enregistrement(self):

        #Nom de ma base de données
        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #baseDonnees = bdd()
        sql = ''' INSERT INTO
              client(nom,prenom,genre,adresse,telephone,email,type_client)
              VALUES(?,?,?,?,?,?,?)
          '''
        
        Client.table(self)

        nbclient = int(input("Saisir le nombre de client à enregistrer : "))
        i = 1

        
        #Nombre de clients à saisir
        while i <= nbclient:
                   
            # Insertion de données
            with conn:          
                
                print(" =====>  Client Numero : ",i)
                
                Client.saisieClient(self)
                
                
                data = Client.recupererSaisieClient(self)
                bdd.bdd.insert_data_table(conn,sql,data)
                print("Enregistrement validé !")
                
            i +=1    


    def affichageClient(self):

        #Nom de ma base de données
        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        requete = ''' SELECT * FROM client '''

        #Affichage des données de la table produit
        with conn:
            print("------------- Les clients enregistrés avec suuces -------------")
            bdd.bdd.select_all_data_table(conn,requete)
            

    # Suppression d'une entrée de la table client
    def suppressionClient(self):

        database = "gestionpharmacie"
        
        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Requete de suppression
        sql = 'DELETE FROM client WHERE id_client=?'
        #c.table()
        Client.table(self)

        id = int(input("Veuillez donner l'identifiant du client : "))

        with conn:
            bdd.bdd.delete_data_table(conn,sql,id)
            print("Client Supprimé avec succés")

    # Recherche d'une entrée dans la table client
    def rechercheClient(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Requete de recherche
        requete = ''' SELECT * FROM client WHERE id_client=? '''
        #c.table()
        Client.table(self)

        id = int(input("Veuillez donner l'identifiant du client à rechercher : "))

        with conn:
            bdd.bdd.search_data_table(conn,requete,id)
            print("Client trouvé avec succés")
        
    """ Les différentes Opérations de la classe Client """

    #Méthode Mise à jour du produit selon le champ voulu
    def miseAJourClient(self):

        database = "gestionpharmacie"

        #create a database connection
        conn = bdd.bdd.create_connection(database)

        #Curseur
        curseur=conn.cursor()
        
        #Choix de la modification à effectuer
        choixModif = int(input(" Que voulez vous modifié Tapez  1->nom/2->prénom/3->genre/4->adresse/5->telephone/6->email/7->type client : "))

        if choixModif in range(1,8):
            
            

            #Modification du nom du client
            if choixModif == 1:
                
                identifiant = int(input("Donnez l'identifiant du client : "))
                nom = Client.saisieNom(self)
                data=[(nom, identifiant)]
                for enreg in data:
                    curseur.execute("update client set nom = ? where id_client = ?  ", enreg) 
                    conn.commit()
                    print(" Le nom du client a été Modifié avec succes")


            #Modification du prénom du client
            if choixModif == 2:
                
               

               identifiant = int(input("Donnez l'identifiant du client : "))
               prenom = Client.saisiePrenom(self)
               data = [(prenom, identifiant)]
               for enreg in data:
                           
                   curseur.execute("update client set prenom = ? where id_client = ?  ", enreg) 
                   conn.commit()
                   print(" Le prénom du client a été Modifié avec succes")


            #Modification du genre du client
            if choixModif == 3:

               identifiant = int(input("Donnez l'identifiant du client : "))
               genre = Client.saisieGenre(self)
               data=[(genre, identifiant)]
               for enreg in data:
                   
                   curseur.execute("update client set genre = ? where id_client = ?  ", enreg) 
                   conn.commit()
                   print(" Le genre du client a été Modifié avec succes") 


            #Modification du adresse du client
            if choixModif == 4:

                identifiant = int(input("Donnez l'identifiant du client : "))
                adresse = Client.saisieAdresse(self)
                data=[(adresse, identifiant)]
                for enreg in data:
                    
                    curseur.execute("update client set adresse = ? where id_client = ?  ", enreg) 
                    conn.commit()
                    print(" L'adresse du client a été Modifié avec succes") 


            #Modification du téléphone du client
            if choixModif == 5:

                 
                 

                identifiant = int(input("Donnez l'identifiant du client : "))
                telephone = Client.saisieTelephone(self)
                data=[(telephone, identifiant)]
                for enreg in data:

                    curseur.execute("update client set telephone = ? where id_client = ?  ", enreg) 
                    conn.commit()
                    print(" Le téléphone du client a été Modifié avec succes")


            #Modification du l'email du client
            if choixModif == 6:

                identifiant = int(input("Donnez l'identifiant du client : "))
                email = Client.saisieEmail(self)
                data=[(email, identifiant)]
                for enreg in data:

                    curseur.execute("update client set email = ? where id_client = ?  ", enreg) 
                    conn.commit()
                    print(" L'email du client a été Modifié avec succes") 
                 
            
            

            #Modification du type de client
            if choixModif == 7:

                identifiant = int(input("Donnez l'identifiant du client : "))
                type_client = Client.saisieTypeClient(self)
                data=[(type_client, identifiant)]
                for enreg in data:

                    curseur.execute("update client set type_client = ? where id_client = ?  ", enreg) 
                    conn.commit()
                    print(" Le type du client a été Modifié avec succes") 
            
        

        

        
    

    

    
#if __name__ == "__main__":

    #c = Client()
    
    #c.enregistrement()
    #c.affichageClient()
    #c.suppressionClient()
    #c.rechercheClient()
    #c.affichageClient()
    
