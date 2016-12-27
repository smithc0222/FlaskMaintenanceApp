from app import db
from models import Unit

#create db and tables
db.create_all()

#insert
db.session.add(Unit("P113", "Saltwater Pump"))
db.session.add(Unit("P856", "Stripper Bottoms Pump"))
#commit changes
db.session.commit()
