import os
from time import sleep
from utils import clear_screen
import game
import leaderboard
import startup

def _print_menu(do_slow):
    win_x,_ = os.get_terminal_size()
    win_x = min(win_x, 90)
    print("[1] " + "  Start Game  ".center(win_x, "-"))
    if do_slow: sleep(0.02)
    print("[2] " + "  View Leaderboard  ".center(win_x, "-"))
    if do_slow: sleep(0.02)
    print("[0] " + "  Exit  ".center(win_x, "-"))
    if do_slow: sleep(0.02)

def enter():
    last_input = None
    while True:
        _print_menu(last_input == None)
        
        if last_input != None:
                print("\nInvalid option \"", last_input, "\".")
        else:
                print("")
        choice = input("What would you like to do? ")

        if choice == "1":
                return game.start
        if choice == "2":
                return leaderboard.view
        if choice == "0":
                return

        # Invalid option, redraw screen
        last_input = choice
        clear_screen()
        startup.print_fast()