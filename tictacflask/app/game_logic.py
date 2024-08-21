import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Create an empty board
        self.current_winner = None

    def print_board(self):
        # Prints the current board
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Returns a list of available moves
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        # Make a move on the board
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check for winner
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def play(self, user_move):
        # Make the user move
        if self.make_move(user_move, 'X'):
            if self.current_winner:
                return {'status': 'win', 'board': self.board}

            # Make computer move
            comp_move = random.choice(self.available_moves())
            self.make_move(comp_move, 'O')
            if self.current_winner:
                return {'status': 'loss', 'board': self.board}
            return {'status': 'continue', 'board': self.board}
        return {'status': 'invalid', 'board': self.board}
