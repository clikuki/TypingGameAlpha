import os
import sys
import time
import startup
import game
import leaderboard
import words
import options
from utils import clear_screen, flush_terminal

def _print_menu(do_slow):
    win_x,_ = os.get_terminal_size()
    win_x = min(win_x, 90)
    print("[1] " + "  Start Game  ".center(win_x, "─"))
    if do_slow: time.sleep(0.02)
    print("[2] " + "  View Leaderboard  ".center(win_x, "─"))
    if do_slow: time.sleep(0.02)
    print("[3] " + "  Options  ".center(win_x, "─"))
    if do_slow: time.sleep(0.02)
    print("[0] " + "  Exit  ".center(win_x, "─"))
    if do_slow: time.sleep(0.02)

# dunno if globally storing options and word data is allowed, so im passing them around
def _open_menu(options_data):
    word_set = words.parse_word_set()

    last_input = None
    while True:
        flush_terminal()
        clear_screen()
        startup.print_fast()
        _print_menu(last_input == None)
        
        if last_input != None:
            print("\nInvalid option \"" + str(last_input) + "\".")
            last_input = None
        else:
            print("")

        choice = input("What would you like to do? ")

        if choice == "0":
            return
        elif choice == "1":
            if game.start(word_set):
                leaderboard.view()
        elif choice == "2":
            leaderboard.view()
        elif choice == "3":
            options.view_and_edit(options_data)
        else:
            # Invalid option, redraw screen
            last_input = choice

def main():
    args = sys.argv[1:]
    
    options_data = options.get_options()
    if len(args) > 0 and "skip" in args or "skipLogo" in options_data:
        startup.print_fast()
    else:
        startup.print_animation()

    _open_menu(options_data)
    clear_screen()

main()
