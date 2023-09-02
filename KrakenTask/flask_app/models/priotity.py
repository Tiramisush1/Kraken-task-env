from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import User
from flask_app.controllers import Task
from flask_app.controllers import State
from flask_app.controllers import Rol

class Priority:
    def __init__(self, data):
        self.id = data ['id']
        self.name_priority = data['name_priority']
        self.description = data ['description']