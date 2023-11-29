import os
from flask import Flask, jsonify, Response, render_template, request 
from flask_cors import CORS
import os, re, datetime
import db
from models import Student

# def create_app():
app = Flask(__name__)
CORS(app)
# Error 404 handler
@app.errorhandler(404)
def resource_not_found(e):
  return jsonify(error=str(e)), 404
# Error 405 handler
@app.errorhandler(405)
def resource_not_found(e):
  return jsonify(error=str(e)), 405
# Error 401 handler
@app.errorhandler(401)
def custom_401(error):
  return Response("API Key required.", 401)

if not os.path.isfile('students.db'):
  db.connect()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/read', methods=['GET'])
def getRequest():
    content_type = request.headers.get('Content-Type')
    sts = [s.serialize() for s in db.view()]
    print('students in lib: ', sts)
    
    return jsonify({
                # 'error': '',
                'res': sts,
                'status': '200',
                'msg': 'Success getting all students in library!',
                'no_of_students': len(sts)
            })

@app.route("/write", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    course = req_data['course']
    name = req_data['name']
    year = req_data['year']

    st = Student(db.getNewId(), name, course, year)
    print('new student: ', st.serialize())
    db.insert(st)
    new_sts = [s.serialize() for s in db.view()]
    print('students in lib: ', new_sts)
    
    return jsonify({
                # 'error': '',
                'res': st.serialize(),
                'status': '200',
                'msg': 'Success creating a new student!'
            })

  # return app
  
# app = create_app()

if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=8080)




