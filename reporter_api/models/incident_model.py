import datetime
from database.server import DatabaseConnect
from flask import jsonify

db=DatabaseConnect()
class Redflag:

    def get_redflags(self):
        cmd = "SELECT * FROM redflags;"
        db.cursor.execute(cmd)
        all_users = db.cursor.fetchall()
        return all_users

    def create_redflag (self, created_by,created_on,status, location, image, video, comment):
        add_cmd ="INSERT INTO redflags(created_by,created_on,status, location, image, video, comment)\
        VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(created_by,created_on, status, location, image, video, comment)
        db.cursor.execute(add_cmd)

    def get_redflag(self, redflag_id):
        cmd = "SELECT * FROM redflags WHERE redflag_id='{}';".format(redflag_id)
        db.cursor.execute(cmd)
        result = db.cursor.fetchone()
        return result

    def delete_redflag(self,redflag_id):
        del_cmd="DELETE FROM redflags WHERE redflag_id={}".format(redflag_id)
        deleted=db.cursor.rowcount
        db.cursor.execute(del_cmd)
        return deleted

    def modify_location(self,location,redflag_id):
        sql = "UPDATE redflags SET location = '{}' WHERE redflag_id = '{}';".format(location,redflag_id)
        updated_rows = 0    
        db.cursor.execute(sql)
        updated_rows = db.cursor.rowcount
        return updated_rows
    def modify_comment(self,comment,redflag_id):
        sql = "UPDATE redflags SET comment = '{}' WHERE redflag_id = '{}';".format(comment,redflag_id)
        updated_rows = 0    
        db.cursor.execute(sql)
        updated_rows = db.cursor.rowcount
        return updated_rows
    def modify_status(self,status,redflag_id):
        sql = "UPDATE redflags SET status = '{}' WHERE redflag_id = '{}';".format(status,redflag_id)
        updated_rows = 0    
        db.cursor.execute(sql)
        updated_rows = db.cursor.rowcount
        return updated_rows

class Intervention:
    
    def get_interventions(self):
        cmd = "SELECT * FROM interventions;"
        db.cursor.execute(cmd)
        all_users = db.cursor.fetchall()
        return all_users

    def create_intervention(self,created_by,created_on,status, location, image, video, comment):
        add_intervention_cmd = "INSERT INTO interventions(created_by,created_on,status, location, image, video, comment)\
        VALUES ('{}','{}','{}','{}','{}','{}','{}');".format(created_by,created_on,status, location, image, video, comment)
        db.cursor.execute(add_intervention_cmd)
    def get_intervention(self, intervention_id):
        cmd = "SELECT * FROM interventions WHERE intervention_id='{}'".format(intervention_id)
        db.cursor.execute(cmd)
        result = db.cursor.fetchone()

        return result

    def delete_intervention(self,intervention_id):
        del_cmd="DELETE FROM interventions WHERE intervention_id={}".format(intervention_id)
        deleted=db.cursor.rowcount
        db.cursor.execute(del_cmd)
        return deleted

    def modify_interventionlocation(self,location,intervention_id):
        sql = "UPDATE redflags SET location = '{}' WHERE intervention_id = '{}';".format(location,intervention_id)
        updated_rows = 0    
        db.cursor.execute(sql)
        updated_rows = db.cursor.rowcount
        return updated_rows

    def modify_interventioncomment(self,comment,intervention_id):
        sql = "UPDATE redflags SET comment = '{}' WHERE intervention_id = '{}';".format(comment,intervention_id)
        updated_rows = 0    
        db.cursor.execute(sql)
        updated_rows = db.cursor.rowcount
        return updated_rows