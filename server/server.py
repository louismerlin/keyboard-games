from flask import Flask
from flask import request
from yo import *
import time

app = Flask(__name__)

game = TicTacToe()

@app.route("/")
def hello():
    return str(time.time())

@app.route("/key", methods=['POST'])
def key():
    print(request.get_json(silent=True))
    return incYo()

if __name__ == "__main__":
    app.run()
