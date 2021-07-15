from app import db
from datetime import datetime

class ChartDummy(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  status = db.Column(db.String(200))
  value = db.Column(db.BigInteger)
  created_date = db.Column(db.DateTime, default=datetime.utcnow)
  updated_date = db.Column(db.DateTime, default=datetime.utcnow)
  
  def __repr__(self):
    return '<ChartDummy {}>'.format(self.name)
