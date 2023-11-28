import os
from flask import Flask, jsonify, Response, render_template, request 
import os, re, datetime
import db
from models import Student

def create_app():
  app = Flask(__name__)
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

  @app.route('/request', methods=['GET'])
  def getRequest():
      content_type = request.headers.get('Content-Type')
      sts = [s.serialize() for s in db.view()]
      if (content_type == 'application/json'):
          json = request.json
          for s in sts:
              if s['id'] == int(json['id']):
                  return jsonify({
                      # 'error': '',
                      'res': b,
                      'status': '200',
                      'msg': 'Success getting all students in the database'
                  })
          return jsonify({
              'error': f"Error! Student with id '{json['id']}' not found!",
              'res': '',
              'status': '404'
          })
      else:
          return jsonify({
                      # 'error': '',
                      'res': sts,
                      'status': '200',
                      'msg': 'Success getting all students in library!',
                      'no_of_students': len(sts)
                  })

  return app
  
app = create_app()

if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=8080)




