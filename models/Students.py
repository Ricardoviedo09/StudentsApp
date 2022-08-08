from config.connection import db


# Student Class/Model
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


# Create table if it doesn't exist
db.create_all()
