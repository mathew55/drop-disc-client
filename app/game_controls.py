# from app.request import request_manager
#
# def make_move(game,move):
#     PARAMS_MAKE_MOVE = {'move_col': ''}
#     PARAMS_MAKE_MOVE['game_id'] = game.gameid
#     make_move_url = 'http://localhost:5000/next-move/'
#     PARAMS_MAKE_MOVE['move_col'] = move
#     game_state_after_move = request_manager(make_move_url, PARAMS_MAKE_MOVE)
#     return game_state_after_move
#
# def update_game_move(game,move):
#     move_response = make_move(game, move)
#     game.update_game(move_response['Board'], move_response['Current_Turn_Player'], move_response['Winner'])
#
# def check_current_player(game, player):
#     get_current_player = 'http://localhost:5000/get-player/'
#     PARAMS_MAKE_MOVE = {'game_id': game.gameid}
#     game_state_check_player_turn = request_manager(get_current_player, PARAMS_MAKE_MOVE)
#     if game_state_check_player_turn['Current_Turn_Player'] == player.player_name:
#         game.update_game(game_state_check_player_turn['Board'], game_state_check_player_turn['Current_Turn_Player'], game_state_check_player_turn['Winner'])