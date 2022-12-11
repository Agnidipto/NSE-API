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

if __name__ == "__main__":
  app.run()