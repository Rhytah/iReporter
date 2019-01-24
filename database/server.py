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
        # self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
        # self.conn.autocommit = True
        # self.cursor = self.conn.cursor()
        

        if app.config.get('ENV') == 'development':
            dbname = app_configuration['development'].DATABASE
            self.credentials['dbname'] = dbname

            
        if app.config.get('ENV') == 'testing':
            dbname = app_configuration['testing'].DATABASE
            self.credentials['dbname'] = dbname

        if app.config.get('ENV') == 'production':
            dbname = app_configuration['production'].DATABASE
            self.credentials['host'] = app_configuration['production'].HOST
            self.credentials['user'] = app_configuration['production'].USER
            self.credentials['password'] = app_configuration['production'].PASSWORD
            self.credentials['dbname'] = dbname

        try:
            self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
        except Exception as error:
            print(f"error: {error}")

    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)