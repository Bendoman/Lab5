from flask import Flask
import json

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def base_route():
        return "Hello world"

    return app
  
app = create_app()

if __name__ == "__main__":
  #    app = create_app()
  print(" Starting app...")
  app.run(host="0.0.0.0", port=8080)