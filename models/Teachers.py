from config.connection import db


# Teachers Class/Model
class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    course = db.Column(db.String(25), nullable=False)

    def __init__(self, name, lastname, course):
        self.name = name
        self.lastname = lastname
        self.course = course


# Create table if it doesn't exist
db.create_all()
