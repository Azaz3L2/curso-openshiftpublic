import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
  return "Bienvenido v3!!!"
  
@app.route('/como estas')
def hola():
  return 'Estoy super bien, gracias'
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
