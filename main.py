import os
import sys
from utils import clear_screen
import startup
import menu

def main():
    args = sys.argv[1:]
    if len(args) > 0 and "skip" in args:
        startup.print_fast()
    else:
        startup.print_animation()

    # rudimentary page system
    # each page function runs its own logic, then returns the next page function to switch pages
    # returning no page clears the screen before closing the program
    page = menu.enter
    while page != None:
        page = page()

    clear_screen()

main()
