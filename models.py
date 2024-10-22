
from databse import db




class User(db.Model):
    __tablename__ = 'users'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(50), unique=True, nullable=False)  # Unique username
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp of creation

    def __repr__(self):
        return f"<User {self.username}>"

class Algorithm(db.Model):
    __tablename__ = 'algorithms'  # Name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), unique=True, nullable=False)  # Name of the algorithm
    description = db.Column(db.Text, nullable=True)  # Description of the algorithm

    def __repr__(self):
        return f"<Algorithm {self.name}>"
