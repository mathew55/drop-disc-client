import numpy as np

class Game:

    turn = 0
    winner = ''
    game_over = False

    def __init__(self, gameid, opponent, board, next_move_player, winner):
        self.gameid = gameid
        self.opponent = opponent
        self.board = np.array(board)
        self.next_move_player = next_move_player
        self.winner = winner

    def display_board(self):
        print()
        print(np.flip(self.board, 0))
        print()

    def update_game(self, board, next_move_player, winner):
        self.board = np.array(board)
        self.next_move_player = next_move_player
        self.winner = winner

    def update_next_move_player(self, next_move_player):
        self.next_move_player = next_move_player

    def no_winner_yet(self):
        if self.winner == '':
            return True
        else:
            return False

    def get_winner(self):
        return self.winner


