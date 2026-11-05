import time
import leaderboard
import os
from utils import row_update_print, clear_screen, flush_terminal

def _load_options_data():
    options_path = "options.dat"
    if not os.path.exists(options_path):
        return set()

    data = set()
    with open(options_path, "r") as fh:
        for line in fh:
            data.add(line.strip())

    return data

def _save_options_data(data):
    options_path = "options.dat"

    with open(options_path, "w") as fh:
        for var in data:
            fh.write(var)
            fh.write("\n")

def draw_options(options_data, do_fast):
    strings = [
        " " + " OPTIONS ".center(45, "─") + " ",
    ]

    option_rows = [
        "[1]  Clear leaderboard",
        "[2]  Skip logo animation -> "+ str("skipLogo" in options_data).upper(),
        "[3]  Skip game countdown -> "+ str("noCountDown" in options_data).upper(),
        "[4]  Remove menu animations -> "+ str("noAnim" in options_data).upper(),
        "[0]  Return to main menu",
    ]
    option_rows = ["║  " + s.ljust(43) + "║" for s in option_rows]

    # first draw: box edges
    new_rows = [
        # Top and bottom
        (1, "╓─────────────────────────────────────────────╖"),
        (2, "╙─────────────────────────────────────────────╜"),
        # Push bottom down with middle rows
    ] + [(2, "║                                             ║")] * len(option_rows)
    
    row_update_print(strings, new_rows, False, do_fast)
    if not do_fast: time.sleep(0.3)

    new_rows = [(i+2, s, 0.05) for (i, s) in enumerate(option_rows)]
    row_update_print(strings, new_rows, True, do_fast)
    if not do_fast: time.sleep(0.3)

def toggle_elem_in_set(s, e):
    if e in s:
        s.remove(e)
    else:
        s.add(e)

def get_options():
    return _load_options_data()

def view_and_edit(options_data):
    has_ran = "noAnim" in options_data
    res_text = None
    while True:
        flush_terminal()
        clear_screen()
        draw_options(options_data, has_ran)
        has_ran = True
        
        if res_text != None:
            print(res_text)
            res_text = None
        else:
            print("")

        choice = input("What would you like to do? ")

        if choice == "0":
            break
        elif choice == "1":
            if input("Are you sure? (y/N) ").upper() == "Y":
                leaderboard.clear()
                res_text = "Leaderboard successfully cleared."
            else:
                res_text = "Clear operation cancelled."
        elif choice == "2":
            toggle_elem_in_set(options_data, "skipLogo")
        elif choice == "3":
            toggle_elem_in_set(options_data, "noCountDown")
        elif choice == "4":
            toggle_elem_in_set(options_data, "noAnim")
        else:
            # Invalid option, redraw screen
            res_text = "\nInvalid option \"" + str(choice) + "\"."

    _save_options_data(options_data)