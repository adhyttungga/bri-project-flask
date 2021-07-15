from app import db
from datetime import datetime
from sqlalchemy.orm import validates

class Investment(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  application = db.Column(db.String(200))
  mandatory_business = db.Column(db.BigInteger)
  investment_value = db.Column(db.BigInteger)
  return_on_investment = db.Column(db.BigInteger)
  created_date = db.Column(db.DateTime, default=datetime.utcnow)
  updated_date = db.Column(db.DateTime, default=datetime.utcnow)
  
  def __repr__(self):
    return '<Investment {}>'.format(self.name)
  
  @validates("application")
  def validate_application(self, key, application):
    if not application: 
      raise AssertionError("Application is required")
    return application
  
  @validates("mandatory_business")
  def validate_mandatory_business(self, key, mandatory_business):
    if not mandatory_business: 
      raise AssertionError("Mandatory Business is required")
    return mandatory_business
  
  @validates("investment_value")
  def validate_investment_value(self, key, investment_value):
    if not investment_value: 
      raise AssertionError("Investment Value is required")
    return investment_value
  
  @validates("return_on_investment")
  def validate_retrun_investment(self, key, return_investment):
    if not return_investment: 
      raise AssertionError("Return on Investment is required")
    return return_investment
