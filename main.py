from flask import Flask
from flask import request
import json

@app.route("/") #Default - Show Data
def test:
    return "Hello world"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
