from app.services.conf import Config
import requests
import json

config = Config()

def request_manager(request_api_endpoint, request_parameters):
    response = requests.post(url=request_api_endpoint, params=request_parameters)
    response_json = json.loads(response.content.decode('utf-8'))
    response_game_state = response_json['payload']['Game_State']
    return response_game_state

def request_new_game(player):
    print("Starting Game, Requesting server")
    serverhttpEndpoint = config.get_config_value("endpoint", "serverhttpEndpoint")
    baseEndpoint = config.get_config_value("endpoint", "base")
    start_game_url = f'{serverhttpEndpoint}/{baseEndpoint}/startgame/'
    PARAMS_START_GAME = {'player_name': player.player_name, 'player_token': player.token}
    game_state = request_manager(start_game_url, PARAMS_START_GAME)
    gameId = game_state['GameID']

    if game_state['Player1'] == player:
        opponent = 'Player2'
    else:
        opponent = 'Player1'

    print(f"GameId received is {gameId}")
    PARAMS_START_GAME['game_id'] = gameId
    return gameId, game_state[opponent], game_state['Board'], game_state['Current_Turn_Player'], game_state['Winner']



