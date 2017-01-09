from app import db
from models import *

db.drop_all()
#create db and tables
db.create_all()

#insert
db.session.add(Unit("P113", "Saltwater Pump"))
db.session.add(Unit("P856", "Stripper Bottoms Pump"))
b=db.session.query(Unit).first()
db.session.add(Parts("Pump, Richter, Wet End RI9427-13-8104", "Pump, Richter, RMA-B, 1.5 X 1 - 8, WET END, STANDARD TORQUE, 6.750\" IMPELLER TRIM, P/N: 9427-13-8104", 3, unit_id=b))
db.session.add(Parts("Pump, Richter, Impeller Assembly, RI 9427-13-8328", "RICHTER, RMA-B, 1.5 X 1 - 8, COMPLETE IMPELLER ASSEMBLY, STANDARD TORQUE P/N: 9427-13-8328 (KIT C)BOM INCLUDES:* 6.750\" IMPELLER* DISTANCE RING* FRONT THRUST RING* BEARINGS* ANTI-TORSION INSERT* INNER MAGNET* CIRCLIP", 2, unit_id=b))

#commit changes
db.session.commit()
