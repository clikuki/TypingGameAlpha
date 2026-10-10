import os
import sys
import time
from utils import clear_screen, flush_terminal
import startup
import game
import leaderboard
import words

def _print_menu(do_slow):
    win_x,_ = os.get_terminal_size()
    win_x = min(win_x, 90)
    print("[1] " + "  Start Game  ".center(win_x, "-"))
    if do_slow: time.sleep(0.02)
    print("[2] " + "  View Leaderboard  ".center(win_x, "-"))
    if do_slow: time.sleep(0.02)
    print("[0] " + "  Exit  ".center(win_x, "-"))
    if do_slow: time.sleep(0.02)

def _open_menu():
    word_set = words.parse_word_set()

    last_input = None
    while True:
        clear_screen()
        startup.print_fast()
        _print_menu(last_input == None)
        
        if last_input != None:
            print("\nInvalid option \"" + str(last_input) + "\".")
            last_input = None
        else:
            print("")

        flush_terminal()
        choice = input("What would you like to do? ")

        if choice == "0":
            return
        if choice == "1":
            if game.start(word_set):
                leaderboard.view()
            continue
        if choice == "2":
            leaderboard.view()
            continue

        # Invalid option, redraw screen
        last_input = choice

def main():
    args = sys.argv[1:]
    if len(args) > 0 and "skip" in args:
        startup.print_fast()
    else:
        startup.print_animation()

    _open_menu()
    clear_screen()

main()
