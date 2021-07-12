from app.services.user_interactions import initialize_player
from app.services.user_interactions import initialize_game
from app.services.user_interactions import get_user_move
from app.services.request_manager import request_new_game

import time
import logging.handlers
import os

log = logging.getLogger("drop-disc-client")
handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", "drop-disc-client.log"))
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)


if __name__ == '__main__':
    log.info("Starting the application")
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
            print("Current Status of the board")
            game.display_board()
            next_move = get_user_move(player)
            game.make_next_move(next_move)
            game.display_board()
        else:
            game.check_current_player(player)

        time.sleep(1)

    print(f"GAME OVER, WINNER IS {game.get_winner()}")
    log.info("Game finished with a winner")