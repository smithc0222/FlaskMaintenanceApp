from app import db
from models import *



#insert
db.session.add(Unit("P114", "Saltwater Pump"))
db.session.add(Unit("P856", "Stripper Bottoms Pump"))

db.session.add(Parts("Pump, Richter, Wet End RI9427-13-8104", "Pump, Richter, RMA-B, 1.5 X 1 - 8, WET END, STANDARD TORQUE, 6.750\" IMPELLER TRIM, P/N: 9427-13-8104"))
db.session.add(Parts("Pump, Richter, Impeller Assembly, RI 9427-13-8328", "RICHTER, RMA-B, 1.5 X 1 - 8, COMPLETE IMPELLER ASSEMBLY, STANDARD TORQUE P/N: 9427-13-8328 (KIT C)BOM INCLUDES:* 6.750\" IMPELLER* DISTANCE RING* FRONT THRUST RING* BEARINGS* ANTI-TORSION INSERT* INNER MAGNET* CIRCLIP"))

#commit changes
db.session.commit()
