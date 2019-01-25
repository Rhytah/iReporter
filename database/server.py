import psycopg2 
from flask import current_app as app
from config import app_configuration
from psycopg2.extras import RealDictCursor
from .relations_commands import sqlcommands
import os

class DatabaseConnect:

    def __init__(self):
        
        # self.credentials = dict(
        #         dbname ='',
        #         user = 'postgres',
        #         password='mine',
        #         host='localhost',
        #         port = 5432
        #     )
        self.credentials= dict(dbname='degbph26bv6m4i',
         user= 'wkmnrsrpffhfpr',
          host='ec2-54-227-246-152.compute-1.amazonaws.com',
         port =5432 ,
         password = 'dde675f7f5af4dc53de4bbac1c7109921fa99454935ce281b3e94798c98eb125' )
        self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        

        if app.config.get('ENV') == 'development':
            dbname = app_configuration['development'].DATABASE
            self.credentials['dbname'] = dbname

            
        if app.config.get('ENV') == 'testing':
            dbname = app_configuration['testing'].DATABASE
            self.credentials['dbname'] = dbname
    
        # if app.config.get('ENV') == 'production':
 
        #     # self.credentials_heroku ="""
        #     # dbname='degbph26bv6m4i' user= 'wkmnrsrpffhfpr' host='ec2-54-227-246-152.compute-1.amazonaws.com' port =5432 password = 'dde675f7f5af4dc53de4bbac1c7109921fa99454935ce281b3e94798c98eb125' 
        #     # # """
        #     # self.credentials_heroku= dict(dbname='degbph26bv6m4i',
        #     #  user= 'wkmnrsrpffhfpr',
        #     #   host='ec2-54-227-246-152.compute-1.amazonaws.com',
        #     #  port =5432 ,
        #     #  password = 'dde675f7f5af4dc53de4bbac1c7109921fa99454935ce281b3e94798c98eb125' )
        #     # self.credentials =self.credentials_heroku
        #     herokudb= app_configuration['production'].DATABASE_URI
        #     self.credentials['user'] = app_configuration['production'].USER
        #     self.credentials['password'] = app_configuration['production'].PASSWORD
        #     self.credentials['host'] = app_configuration['production'].HOST
        #     self.credentials['port'] = app_configuration['production'].PORT
        #     self.credentials['dbname'] = dbname
        #     # self.credentials = herokudb
            
        try:
            self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print(self.credentials['dbname'])
        except:
            print("failed to connect")
        
    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)