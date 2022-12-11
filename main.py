from flask import Flask, request
import utils
from flask_cors import CORS, cross_origin
app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route("/")
@cross_origin()
def hello():
    args=request.args
    return utils.get_data(args["name"])

@app.route("/price")
@cross_origin()
def price() :
    args=request.args
    return utils.get_price(args["name"])

@app.route("/change")
@cross_origin()
def change() :
    args=request.args
    return utils.get_change(args["name"])

@app.route("/points")
@cross_origin()
def points() :
    args=request.args
    return utils.get_points(args["name"])

@app.route("/up-down")
@cross_origin()
def up_down() :
    args=request.args
    return utils.get_up_down(args["name"])

if __name__ == "__main__":
  app.run()