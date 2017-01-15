from app import db

class Schedule(db.Model):

    __tablename__="schedule"
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.DateTime)

    schedule_line=db.relationship('schedule_line', backref=db.backref('line', lazy='dynamic'))

    def __init__(self, date):
        self.date=date

    def __repr__(self):
        return '{Schedule: }'.format(self.date)

schedule_line = db.Table('schedule_line',
    db.Column('schedule_id', db.Integer, db.ForeignKey('schedule.id')),
    db.Column('workorder_id', db.Integer, db.ForeignKey('workorder.id')),
)

class User(db.Model):

    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True)
    first_name=db.Column(db.String(20), nullable=False)
    last_name=db.Column(db.String(20), nullable=False)
    position=db.Column(db.String(50), nullable=False)


    def __init__(self, username, first_name, last_name, position):
        self.username=username
        self.first_name=first_name
        self.last_name=last_name
        self.position=position

    def __repr__(self):
        return '{}'.format(self.username)

user_lockout = db.Table('user_lockout',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('lockout_id', db.Integer, db.ForeignKey('lockout.id'))
)
user_workorder = db.Table('user_workorder',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('workorder_id', db.Integer, db.ForeignKey('workorder.id'))
)

class Workorder(db.Model):

    __tablename__="workorder"
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(250), nullable=False)
    notes=db.Column(db.String(1000), nullable=False)

    #One to Many Relationship between User and Workorder as workorder_author
    author_id=db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    workorder_author=db.relationship('User', backref=db.backref('workorder_author', lazy='dynamic'))

    #Many to Many Relationship between Workorder and user_workorder Table to name technicians to workorders
    workorder_technician=db.relationship('User', secondary=user_workorder, backref=db.backref('workorder_technician', lazy='dynamic'))

    def __init__(self, description, notes, author_id):
        self.description=description
        self.notes=notes
        self.author_id=author_id

    def __repr__(self):
        return '{}'.format(self.description)

class Lockout(db.Model):

    __tablename__="lockout"
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(200), nullable=False)
    lockout_author = db.relationship('User', secondary=user_lockout, backref=db.backref('lockout_author', lazy='dynamic'))

    def __init__(self, description):
        self.description=description

    def __repr__(self):
        return '{}'.format(self.description)

class Warehouse(db.Model):

    __tablename__="warehouse"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    bin=db.Column(db.String(10), nullable=False, unique=True)


    def __init__(self, name, bin):
        self.name=name
        self.bin=bin

    def __repr__(self):
        return '{}'.format(self.bin)

warehouse_part = db.Table('warehouse_part',
    db.Column('warehouse_id', db.Integer, db.ForeignKey('warehouse.id')),
    db.Column('part_id', db.Integer, db.ForeignKey('part.id'))
)

class Unit(db.Model):

    __tablename__="unit"
    id=db.Column(db.Integer, primary_key=True)
    unit_name=db.Column(db.String(200), unique=True)
    description=db.Column(db.String(1000), nullable=True)

    def __init__(self, unit_name, description):
        self.unit_name=unit_name
        self.description=description

    def __repr__(self):
        return '{}'.format(self.unit_name)

unit_part = db.Table('unit_part',
    db.Column('unit_id', db.Integer, db.ForeignKey('unit.id')),
    db.Column('part_id', db.Integer, db.ForeignKey('part.id'))
)

class Part(db.Model):

    __tablename__="part"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    description=db.Column(db.String(1000), nullable=False)
    quantity_on_hand=db.Column(db.Integer, nullable=True)

    units=db.relationship('Unit', secondary='unit_part', backref=db.backref('spares', lazy='dynamic'))

    warehouses=db.relationship('Warehouse', secondary='warehouse_part', backref=db.backref('location', lazy='dynamic'))

    def __init__(self, name, description,quantity_on_hand):
        self.name=name
        self.description=description
        self.quantity_on_hand=quantity_on_hand

    def __repr__(self):
        return '{}'.format(self.name)
