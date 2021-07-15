from app.model.chart_dummy import ChartDummy

from app import response, app, db
from flask import request, jsonify
import math

# create function create for /article POST method
def create():
  try:
    status = request.form.get('status')
    value = request.form.get('value')
    input = [{
      "status": status,
      "value": value,
    }]
    chart_dummy = ChartDummy(
      status = status,
      value = value,
    )
    db.session.add(chart_dummy)
    db.session.commit()
    return response.success(input, 'Successfully added new Chart Dummy')
  except AssertionError as e:
    return response.badRequest([], "{}".format(e))

# import all from investment database
def index():
  try: 
    chart_dummy = ChartDummy.query.all()
    data = formatArray(chart_dummy)
    return response.success(data, "success")
  except Exception as e:
    print(e)
    
def formatArray(datas):
  array = []  
  for data in datas:
    array.append(singleObject(data))
  return array

def singleObject(data):
  data = {
    "id": data.id,
    "status": data.status,
    "value": data.value,
  }
  return data