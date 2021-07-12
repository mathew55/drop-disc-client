from app.model.player import Player
from app.model.game import Game


def initialize_player():
    player_name = input(f"Welcome to the Game, Enter a player name:")
    token = input(f"Please choose a disc shape for your username (Disc names can be numbers between 1 - 9):")
    player = Player(player_name, token)
    return player

def initialize_game(gameId, opponent, board, current_turn_player, winner):
    game = Game(gameId, opponent, board, current_turn_player, winner)
    return game

def get_user_move(player):
    insert_position_user = int(input(f"It's your turn {player.player_name}, Please enter a column (1 - 9):"))
    insert_position_np = insert_position_user - 1
    return insert_position_np

