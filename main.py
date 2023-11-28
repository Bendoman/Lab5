from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS
import json

def create_app():
  app = Flask(__name__)

  @app.route("/")
  def hello_world():
     return "Hello world"

  return app
  
app = create_app()

if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=8080)