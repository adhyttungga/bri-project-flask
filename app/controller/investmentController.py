from app.model.investment import Investment

from app import response, app, db
from flask import request, jsonify
import math

# create function create for /article POST method
def create():
  try:
    application = request.form.get('application')
    mandatory_business = request.form.get('mandatory_business')
    investment_value = request.form.get('investment_value')
    return_on_investment = request.form.get('return_on_investment')
    input = [{
      "application": application,
      "mandatory_business": mandatory_business,
      "investment_value": investment_value,
      "return_on_investment": return_on_investment,
    }]
    investment = Investment(
      application = application,
      mandatory_business = mandatory_business,
      investment_value = investment_value,
      return_on_investment = return_on_investment,
    )
    db.session.add(investment)
    db.session.commit()
    return response.success(input, 'Successfully added new investment')
  except AssertionError as e:
    return response.badRequest([], "{}".format(e))

# import all from investment database
def index():
  try: 
    investment = Investment.query.all()
    data = formatArray(investment)
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
    "application": data.application,
    "mandatory_business": data.mandatory_business,
    "investment_value": data.investment_value,
    "return_on_investment": data.return_on_investment,    
  }
  return data

# import pagination from investment database
def paginate(limit, offset):
  try:
    limit = int(limit)
    offset = int(offset)
    return jsonify(paginateList(limit, offset))
  except Exception as e:
    print(e)

def paginateList(limit, offset):
  investment = Investment.query.all()
  data = formatArray(investment)
  count = len(data)
  
  obj = {}
  
  if (count < offset):
    obj["success"] = False
    obj["message"] = "The selected page (offset) exceeds the total data limit!"
    return obj
  
  else:
    # make response
    obj['success'] = True
    obj['start_page'] = offset
    obj['per_page'] = limit
    obj['total_data'] = count
    obj['total_page'] = math.ceil(count / limit)
    obj['results'] = data[(offset - 1):(offset - 1 + limit)]
    # obj['all_results'] = data
    return obj
  return obj