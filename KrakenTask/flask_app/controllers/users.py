from flask_app import app
from flask import Flask, render_template, request, redirect 
from flask_app.models.user import User
from flask_app.models.task import Task

@app.route('/')
def index():
    return redirect('/login')