from app import app
from flask import request

# import controller
from app.controller import investmentController
from app.controller import chart_dummyController

@app.route('/')
def index():
  return 'Hello Flask'

@app.route('/dashboard/investment', methods=["GET", "POST"])
def dashboard():
    if request.method == "GET":
        return investmentController.index()
    elif request.method == "POST":
        return investmentController.create()
  
@app.route('/dashboard/investment/<limit>/<offset>', methods=["GET"])
def paginations(limit, offset):
    return investmentController.paginate(limit, offset)
  
@app.route('/dashboard/chart-dummy', methods=["GET", "POST"])
def chartDummy():
    if request.method == "GET":
        return chart_dummyController.index()
    elif request.method == "POST":
        return chart_dummyController.create()