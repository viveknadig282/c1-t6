import requests
import urllib
import json
import psycopg2
from psycopg2 import Error

class DBHandler:
    #following constants should be replaced by production version and moved into settings.py
    user="username"
    password="password"
    host="hostname"
    port="port"
    database="food_db"

    connection = None
    
    def __init__(self):
        try:
            # Connect to an existing database
            self.connection = psycopg2.connect(self.user,
                                               self.password,
                                               self.host,
                                               self.port,
                                               self.database)
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
            
    def __del__(self):
        if connection:
            connection.close()
            

    def getIngredientScores(ingredients):
        names = "', '".join(ingredients)
        cursor = connection.cursor()
        cursor.execute("select name, score from Ingredients where name in ('" + names + "')")
        records = cursor.fetchall()
        cursor.close()
        #returning array of tuples of (name, score)
        return records
