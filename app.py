from flask import Flask, request
from flask_restful import Api, Resource
from flask_migrate import Migrate
from config import Config
from algorithms import sorting_algorithms
from models import User
from databse import db  # Import the db instance
import os

app = Flask(__name__)  # Create a Flask instance
app.config.from_object(Config)  # Load configuration
db.init_app(app)  # Initialize the database with the app
migrate = Migrate(app, db)  # Initialize Flask-Migrate

api = Api(app)  # Initialize API

class SortResource(Resource):
    def post(self, algorithm):
        data = request.json.get('data')
        
        if algorithm in sorting_algorithms:
            steps = sorting_algorithms[algorithm](data)
            return {'steps': steps}, 200
        else:
            return {'error': 'Invalid sorting algorithm'}, 400

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {'id': user.id, 'username': user.username}, 200
        return {'error': 'User not found'}, 404

    def post(self):
        data = request.json
        new_user = User(username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'id': new_user.id}, 201

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}, 200
        return {'error': 'User not found'}, 404

# Add user resource routes
api.add_resource(UserResource, '/api/user', '/api/user/<int:user_id>')
api.add_resource(SortResource, '/api/sort/<string:algorithm>')

if __name__ == '__main__': 
    app.run(debug=True)