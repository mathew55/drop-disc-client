from app.user_interactions import initialize_player
from app.user_interactions import initialize_game
from app.user_interactions import get_user_move
from app.request import request_new_game

import time


if __name__ == '__main__':
    player = initialize_player()
    game = initialize_game(*(request_new_game(player)))

    print(f"Your opponent is {game.opponent}")
    print(f"The current board position is ")
    game.display_board()

    if game.current_turn_player == player:
        print(f"You are granted the privilege of making the first move, Good Luck")
        print(f"It's your turn {player.player_name}, Please enter a column (1 - 9):")

    while game.no_winner_yet():
        if game.current_turn_player == player.player_name:
            game.display_board()
            next_move = get_user_move(player)
            game.make_next_move(next_move)
            game.display_board()
        else:
            game.check_current_player(player)

        time.sleep(3)

    print(f"GAME OVER, WINNER IS {game.get_winner()}")