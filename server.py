from flask import Flask
from flask import request
from tictactoe import *
from surfit import *

app = Flask(__name__)

#game = TicTacToe()
game = SurfIt()

@app.route("/")
def hello():
    return str(game.someone_won)

@app.route("/key", methods=['POST'])
def key():
    game.getKey(request.get_json(silent=True)['k'])
    return "Reçu"

if __name__ == "__main__":
    app.run()
