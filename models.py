from app import db

class Unit(db.Model):

    __tablename__="unit"
    id=db.Column(db.Integer, primary_key=True)
    unit_name=db.Column(db.String(200), nullable=True)
    description=db.Column(db.String(1000), nullable=True)



    def __init__(self, unit_name, description):
        self.unit_name=unit_name
        self.description=description

    def __repr__(self):
        return '{}'.format(self.unit_name)


class Parts(db.Model):

    __tablename__="parts"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    description=db.Column(db.String(1000), nullable=False)
    quantity_on_hand=db.Column(db.Integer, nullable=True)

    unit_id=db.Column(db.Integer, db.ForeignKey('unit.id'))
    units = db.relationship('Unit', backref=db.backref('spares', lazy='dynamic'))

    def __init__(self, name, description,quantity_on_hand, unit_id):
        self.name=name
        self.description=description
        self.quantity_on_hand=quantity_on_hand
        self.unit_id=unit_id


    def __repr__(self):
        return '{}'.format(self.name)
