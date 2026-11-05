import time
import leaderboard
from utils import row_update_print, clear_screen, flush_terminal

def draw_options(skip):
    strings = [
        " " + " OPTIONS ".center(45, "─") + " ",
    ]

    # first draw: box edges
    new_rows = [
        # Top and bottom
        (1, "╓─────────────────────────────────────────────╖"),
        (2, "╙─────────────────────────────────────────────╜"),
        # Push bottom down with middle rows
    ] + [(2, "║                                             ║")] * 2
    
    row_update_print(strings, new_rows, False, skip)
    if not skip: time.sleep(0.3)

    new_rows = [
      # (2, "║                                             ║", 0.05),
        (2, "║  [1]  Clear leaderboard                     ║", 0.05),
        (3, "║  [0]  Return to main menu                   ║", 0.05),
    ]

    row_update_print(strings, new_rows, True, skip)
    if not skip: time.sleep(0.3)

def view():
    has_ran = False
    res_text = None
    while True:
        flush_terminal()
        clear_screen()
        draw_options(has_ran)
        has_ran = True
        
        if res_text != None:
            print(res_text)
            res_text = None
        else:
            print("")

        choice = input("What would you like to do? ")

        if choice == "0":
            return
        elif choice == "1":
            if input("Are you sure? (y/N) ").upper() == "Y":
                leaderboard.clear()
                res_text = "Leaderboard successfully cleared."
        else:
            # Invalid option, redraw screen
            res_text = "\nInvalid option \"" + str(choice) + "\"."