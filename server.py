from flask import Flask
from flask import request
from tictactoe import *

app = Flask(__name__)

game = TicTacToe()

@app.route("/")
def hello():
    return game.someone_won

@app.route("/key", methods=['POST'])
def key():
    print(request.get_json(silent=True))
    return incYo()

if __name__ == "__main__":
    app.run()
