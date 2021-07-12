import requests
import jsons
import json
import time
from game import Game
from player import Player


def initialize_player():
    player_name = input(f"Welcome to the Game, Enter a player name:")
    player = Player(player_name)
    return player

def get_user_move():
    insert_position_user = int(input(f"It's your turn {player}, Please enter a column (1 - 9):"))
    insert_position_np = insert_position_user - 1
    return insert_position_np

def request_new_game(player):
    print("Starting Game, Requesting server")
    start_game_url = 'http://localhost:5000/start-game/'
    PARAMS_START_GAME = {'player_name': player.player_name}

    r = requests.post(url=start_game_url, params=PARAMS_START_GAME)
    resp_obj_original = json.loads(r.content.decode('utf-8'))
    resp_obj = resp_obj_original['payload']['game_state']
    print(resp_obj)

    if resp_obj['Player1'] == player:
        opponent = 'Player2'
    else:
        opponent = 'Player1'

    gameId = resp_obj['GameID']

    print(f"GameId received is {gameId}")
    PARAMS_START_GAME['game_id'] = gameId
    game = Game(gameId, resp_obj[opponent], resp_obj['Board'], resp_obj['Current_Turn_Player'], resp_obj['Winner'])
    return game


def make_move(game,move):
    PARAMS_MAKE_MOVE = {'move_col': ''}
    PARAMS_MAKE_MOVE['game_id'] = game.gameid
    make_move_url = 'http://localhost:5000/next-move/'
    PARAMS_MAKE_MOVE['move_col'] = move
    r = requests.post(url=make_move_url, params=PARAMS_MAKE_MOVE)
    resp_obj = json.loads(r.content.decode('utf-8'))
    return resp_obj

def update_game_move(game,move):
    move_response = make_move(game, move)
    game.update_game(move_response['game_state']['Board'], move_response['game_state']['Current_Turn_Player'],
                     move_response['game_state']['Winner'])

def check_current_player(gameid):
    get_current_player = 'http://localhost:5000/get-player/'
    PARAMS_MAKE_MOVE = {'game_id': gameid}
    r = requests.post(url=get_current_player, params=PARAMS_MAKE_MOVE)
    resp_obj = json.loads(r.content.decode('utf-8'))
    return resp_obj

if __name__ == '__main__':
    player = initialize_player()
    game = request_new_game(player)

    print(f"Your opponent is {game.opponent}")
    print(f"The current board position is ")
    game.display_board()
    print(f"The next turn is yours - {game.next_move_player}")

    while game.no_winner_yet():
        if game.next_move_player == player.player_name:
            game.display_board()
            next_move = get_user_move()
            update_game_move(game, next_move)
            game.display_board()
        else:
            current_player = check_current_player(game.gameid)
            if current_player['game_state']['Current_Turn_Player'] == player.player_name:
                game.update_game(current_player['game_state']['Board'], current_player['game_state']['Current_Turn_Player'], current_player['game_state']['Winner'])
                game.display_board()


        time.sleep(3)

    print("GAME OVER, WINNER IS")
    print(game.get_winner())