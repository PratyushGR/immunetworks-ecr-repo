from flask import Blueprint, request, jsonify
from .game_logic import TicTacToe

bp = Blueprint('main', __name__)

@bp.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_move = data.get('move')
    game = TicTacToe()
    response = game.play(user_move)
    return jsonify(response)
