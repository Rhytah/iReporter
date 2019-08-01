import psycopg2 
from flask import current_app as app
from config import app_configuration
from psycopg2.extras import RealDictCursor
from .relations_commands import sqlcommands
import os

class DatabaseConnect:

    def __init__(self):
        
        self.credentials = dict(
                dbname ='',
                user = 'postgres',
                password='mine',
                host='localhost',
                port = 5432
            )
        self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        

        if app.config.get('ENV') == 'development':
            dbname = app_configuration['development'].DATABASE_URI
            self.credentials['dbname'] = dbname

            
        if app.config.get('ENV') == 'testing':
            dbname = app_configuration['testing'].DATABASE_URI
            self.credentials['dbname'] = dbname
    
        if app.config.get('ENV') == 'production':
 
            self.credentials_heroku ="""
            dbname='dfktg48dd4p22l' user= 'kuzegimbnbuwlw' host='ec2-50-16-197-244.compute-1.amazonaws.com' port =5432 password = '858f7dd5363a48d534a4184fbe9c3ee5daeadfaf88b73c3267b2aceb92f915b0' 
            """
            self.credentials =self.credentials_heroku
        
        try:
            self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print(self.credentials)
        except:
            print("failed to connect")
    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)

