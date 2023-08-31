from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import Task

class User:
    def __init__(self, data):
        self.id = data  ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.password = data ['password'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.task = []

    @classmethod
    def create_user(cls, data):
        query =  "INSERT INTO users (first_name, last_name, email, password, craeated_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"  
        result = connectToMySQL('kraken').query_db(query, data)
        return result