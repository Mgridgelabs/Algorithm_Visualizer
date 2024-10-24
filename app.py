from flask import Flask, request
from flask_restx import Api, Resource, fields
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

api = Api(app, version='1.0', title='algo visualizer', description='API for sorting Algorithms ')  # Initialize API
sort_model = api.model('sortData', {
    'data': fields.List(fields.Integer, required=True, description='List of integer to sort')
})
#sorting Resource
@api.route('/sort/<string:algorithm>')
@api.doc(params={'algorithm':'name of the sorting algorithm'})
class SortResource(Resource):
    @api.expect(sort_model)
    @api.response(200, 'succes', sort_model)
    @api.response(400, 'Invalid sorting algorithm')
    @api.doc(description='Apply a sorting algorithm to the list of integers')
    def post(self, algorithm):
        """ 
        sort a list of integers using a specified algorithm.
        Available algorithms:
        -buble
        - selection
        - insertion
        - merge
        - quick
        - heap
        - shell
        example input:
        {
            "data": [5, 3, 8, 2, 1, 9, 4, 7, 6]
        }
        """
        data = request.json.get('data')
        
        if algorithm in sorting_algorithms:
            steps = sorting_algorithms[algorithm](data)
            return {'steps': steps}, 200
        else:
            return {'error': 'Invalid sorting algorithm'}, 400

#user rescource 
@api.route('/user/<int:user_id>', '/user')

class UserResource(Resource):
    @api.response(200, 'success')
    @api.response(404, 'User not found')
    @api.doc(description='Get a user by ID or create a new user')  
    def get(self, user_id):
        """
        Retrieve a user's details by their ID.

        Returns the user's ID and username.
        """
        user = User.query.get(user_id)
        if user:
            return {'id': user.id, 'username': user.username}, 200
        return {'error': 'User not found'}, 404


    @api.expect(api.model('NewUser', {
        'username': fields.String(required=True, description='The username of the new user')
    }))
    @api.response(201, 'User created')
    @api.doc(description="Create a new user.")
    def post(self):
        """
        Create a new user with the provided username.
        
        Example input:
        ```
        {
            "username": "john_doe"
        }
        ```
        """
        data = request.json
        new_user = User(username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'id': new_user.id}, 201

    @api.response(200, 'User deleted')
    @api.response(404, 'User not found')
    @api.doc(description="Delete a user by their ID.")
    def delete(self, user_id):
        """
        Delete a user by their ID.
        
        Example:
        `/user/1` will delete the user with ID 1.
        """
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted'}, 200
        return {'error': 'User not found'}, 404

# Add  resource enpoints to api 
api.add_resource(UserResource, '/api/user', '/api/user/<int:user_id>')
api.add_resource(SortResource, '/api/sort/<string:algorithm>')

if __name__ == '__main__': 
    app.run(debug=True)