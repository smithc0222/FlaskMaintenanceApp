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
