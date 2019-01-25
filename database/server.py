import psycopg2 
from flask import current_app as app,abort
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

        self.credentials['dbname']=app_configuration['production'].DB
        self.credentials['user']=app_configuration['production'].USER
        self.credentials['password']=app_configuration['production'].PASSWORD
        self.credentials['host']=app_configuration['production'].HOST
        self.credentials['port']=app_configuration['production'].PORT
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
 
            self.credentials
        
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

