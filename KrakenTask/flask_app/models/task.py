from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import User

class Task:
    def __init__(self, data):
        self.id = data ['id']
        self.name = data ['name']
        self.description = data ['description']
        self.expiry_date = data ['expiry_date']
        self.user_id = []
        self.priority_id = []
        self.state_id = []