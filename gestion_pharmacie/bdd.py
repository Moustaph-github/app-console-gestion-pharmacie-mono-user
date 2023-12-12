""" la classe base de données """
# Importer le module sqlite3
import sqlite3
from sqlite3 import Error

class bdd:


    #def __init__()
    """ Ces méthodes ont été fournies dans la documentation officiel de sqlite de python http://www.sqlitetutorial.net/sqlite-python/ """

    """ la méthode Connection """

    def create_connection(db_file):     

        """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
 
        return None
        
    """ la méthode création de table """

    def create_table(conn, create_table_sql):
        
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            conn.commit()
        except Error as e:
            print(e)

    """ la méthode d'insertion de données dans la base """

    def insert_data_table(conn,sql,data):
        
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    """ Extraction des données dans la base """

    def select_all_data_table(conn,requete_sql):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        #cur.execute("SELECT * FROM personnes")
        cur.execute(requete_sql)
        conn.commit()
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)

    """ Suppresion d'une entrée dans une table """
    def delete_data_table(conn,sql,id):
        """
        Delete a task by task id
        :param conn:  Connection to the SQLite database
        :param id: id of the task
        :return:
        """
        
        cur = conn.cursor()
        cur.execute(sql, (id,))

    """ Suppression de toutes les entrées de la table """
    def delete_all_data_table(conn,sql):
        """
        Delete all rows in the tasks table
        :param conn: Connection to the SQLite database
        :return:
        """
        
        cur = conn.cursor()
        cur.execute(sql)

    """ Mise à jour d'un produit de la table produit """
    def update_data_table(conn,sql,data_table):
        """
        update priority, begin_date, and end date of a task
        :param conn:
        :param task:
        :return: project id
        """
        
        cur = conn.cursor()
        cur.execute(sql,data_table)
        conn.commit()
        

        

    """ Recherche d'une entrée dans une table """
    def search_data_table(conn,sql,id):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()

        rows = cur.fetchall()
 
        for row in rows:
            print(row)
