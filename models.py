from app import db

class Unit(db.Model):

    __tablename__="units"
    id=db.Column(db.Integer, primary_key=True)
    unit=db.Column(db.String(200), nullable=True)
    description=db.Column(db.String(1000), nullable=True)

    def __init__(self, unit, description):
        self.unit=unit
        self.description=description
    def __repr__(self):
        return '{}'.format(self.unit)

class Parts(db.Model):

    __tablename__="parts"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    description=db.Column(db.String(1000), nullable=False)
    quantity_on_hand=db.Column(db.Integer, nullable=True)

    def __init__(self, name, description,quantity_on_hand):
        self.name=name
        self.description=description
        self.quantity_on_hand=quantity_on_hand
    def __repr__(self):
        return '{}'.format(self.name)
