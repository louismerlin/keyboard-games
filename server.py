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
    return str(-1)

@app.route("/start", methods=['POST'])
def start():
    x = request.get_json(silent=True)['g']
    global game
    if x == 0:
        game = TicTacToe()
    if x == 1:
        game = SurfIt()
    return "All good"

@app.route("/key", methods=['POST'])
def key():
    if game != None:
        game.getKey(request.get_json(silent=True)['k'])
    return "Reçu"

if __name__ == "__main__":
    app.run()
