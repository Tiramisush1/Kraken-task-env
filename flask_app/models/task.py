from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import User

class Task:
    def __init__(data, self):
        self.id = data ['id']
        self.name = data['name']
        self.text = data['text']
        self.users = []
        
    @classmethod
    def create(cls, data):
        query = "INSERT INTO tasks (name, text) VALUES(%(name)s %(text)s)"
        result = connectToMySQL('kraken').query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tasks;"
        result = connectToMySQL('kraken').query_db(query)
        tasks = []
        for row in results:
            tasks.append(cls(row))
        return tasks
