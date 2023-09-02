from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import User
from flask_app.controllers import Task
from flask_app.controllers import State

class Rol:
    def __init__(self, data):
        self.id = data ['id']
        self.rolname = data ['rolname']


