from app.services.request_manager import request_manager
from app.services.conf import Config
import numpy as np

config = Config()

class Game:

    turn = 0
    winner = ''
    game_over = False

    def __init__(self, gameid, opponent, board, next_move_player, winner):
        self.gameid = gameid
        self.opponent = opponent
        self.board = np.array(board)
        self.current_turn_player = next_move_player
        self.winner = winner

    def display_board(self):
        print()
        print(np.flip(self.board, 0))
        print()

    def update_game(self, board, next_move_player, winner):
        self.board = np.array(board)
        self.current_turn_player = next_move_player
        self.winner = winner

    def no_winner_yet(self):
        if self.winner == '':
            return True
        else:
            print()
            return False

    def get_winner(self):
        return self.winner

    def make_next_move(self, move):
        PARAMS_MAKE_MOVE = {'move_col': ''}
        PARAMS_MAKE_MOVE['game_id'] = self.gameid
        serverhttpEndpoint = config.get_config_value("endpoint", "serverhttpEndpoint")
        baseEndpoint = config.get_config_value("endpoint", "base")
        make_move_url = f'{serverhttpEndpoint}/{baseEndpoint}/nextmove/'
        PARAMS_MAKE_MOVE['move_col'] = move
        game_state_after_move = request_manager(make_move_url, PARAMS_MAKE_MOVE)
        self.update_game(game_state_after_move['Board'], game_state_after_move['Current_Turn_Player'], game_state_after_move['Winner'])

    def check_current_player(self, player):
        serverhttpEndpoint = config.get_config_value("endpoint", "serverhttpEndpoint")
        baseEndpoint = config.get_config_value("endpoint", "base")
        get_current_player = f'{serverhttpEndpoint}/{baseEndpoint}/getgamestate/'
        PARAMS_MAKE_MOVE = {'game_id': self.gameid}
        game_state_check_player_turn = request_manager(get_current_player, PARAMS_MAKE_MOVE)
        if game_state_check_player_turn['Current_Turn_Player'] == player.player_name:
            self.update_game(game_state_check_player_turn['Board'], game_state_check_player_turn['Current_Turn_Player'],
                             game_state_check_player_turn['Winner'])


