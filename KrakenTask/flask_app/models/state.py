from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import User
from flask_app.controllers import Task

class State:
    def __init__(self, data):
        self.id = data['id']
        self.name_status = data ['name_status']
        self.description = data ['description']