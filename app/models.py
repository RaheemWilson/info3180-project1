from . import db

class Property(db.Model):

    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    rooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price= db.Column(db.String(80))
    location = db.Column(db.String(255))
    type = db.Column(db.String(16))
    file_name = db.Column(db.String(80))


    def __init__(self, title, description, rooms, bathrooms, price, location, type, file_name):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.location = location
        self.type = type
        self.file_name = file_name

