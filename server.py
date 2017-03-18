from flask import Flask
from flask import request
from tictactoe import *
from surfit import *

app = Flask(__name__)

game = None

@app.route("/")
def root():
    if game != None:
        return str(game.someone_won)
    return -1

@app.route("/start", methods=['POST'])
def start():
    x = request.get_json(silent=True)['g']
    if x == 0:
        game = TicTacToe()
    if x == 1:
        game = SurfIt()

@app.route("/key", methods=['POST'])
def key():
    game.getKey(request.get_json(silent=True)['k'])
    return "Reçu"

if __name__ == "__main__":
    app.run()
