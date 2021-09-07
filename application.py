from flask import Flask, request, Response
from flask import render_template
import json
import helper

application = app = Flask(__name__)

@app.route("/", methods=["POST", "Get"])
def Calculate():
    return render_template('page.html')

@app.route("/add", methods=["POST", "GET"])
def addtion():
    value1 = str(request.form.get("value1"))
    value2 = str(request.form.get("value2"))
    Result = helper.add(int(value1), int(value2))
    returnResult = str(value1) + " + " + str(value2) + " is equal to: " + str(Result)
    return render_template('page.html', returnResult = returnResult)

