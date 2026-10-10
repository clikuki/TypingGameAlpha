import os
from utils import clear_screen
import menu

_LEADERBOARD_PATH = "leaderboard.dat"

def _load_leaderboard_data():
    if not os.path.exists(_LEADERBOARD_PATH):
        return []

    data = []
    with open(_LEADERBOARD_PATH, "r") as fh:
        for line in fh:
            line = line.strip().split(",")
            data.append({
                "name": line[0],
                "time": line[1],
                "score": line[2],
            })

    return data

def _save_leaderboard_data(data):
    if len(data) > 10:
        data = data[:10]

    with open(_LEADERBOARD_PATH, "w") as fh:
        for entry in data:
            g_name = entry["name"]
            g_time = entry["time"]
            g_score = entry["score"]

            fh.write(g_name)
            fh.write(",")
            fh.write(g_time)
            fh.write(",")
            fh.write(g_score)
            fh.write("\n")

def _print_leader_board(data):
    print(" " + " LEADERBOARD ".center(45, "─") + " ")
    print("╓─────────────────────────────────────────────╖")
    print("║ RANK    NAME          TIME            SCORE ║")
    print("╟─────────────────────────────────────────────╢")

    if data:
        for i,entry in enumerate(data):
            g_name = entry["name"]
            g_score = entry["score"]
            g_time = float(entry["time"])
            g_time = str(round(g_time, 2))
            
            row = ("[" + str(i+1) + "]").rjust(4) + " "
            row += "   " + (g_name + " ").ljust(12, "─")
            row += (" "+str(g_time).rjust(5)+"  ").ljust(19, "─")
            row += str(g_score).rjust(3) + " "
            print("║ " + row + " ║")
    else:
        print("║             No past games found.            ║")
        print("║    Play a couple games to fill this out!    ║")

    print("╙─────────────────────────────────────────────╜")

def _get_name():
    err = ""
    while True:
        clear_screen()
        print("New entry on the leaderboard!")

        if err:
            print(err)

        name = input("\nEnter your initials: ")
        n_len = len(name)

        if n_len < 1:
            err = "Name must be at least 1 character long."
            continue
        if n_len > 8:
            err = "Name must be at most 8 characters long."
            continue

        clear_screen()
        return name.upper()

def try_add_new_entry(score, time):
    data = _load_leaderboard_data()

    for i,entry in enumerate(data):
        g_score = int(entry["score"])
        g_time = float(entry["time"])

        # If scores tie, prioritize shorter time
        # If time still ties, then first one wins
        if score == g_score and time >= g_time:
            continue
        if score >= g_score:
            if i >= 10: # ranking index is too low
                return

            data.insert(i, {
                "name": _get_name(),
                "time": str(time),
                "score": str(score),
            })
            break
    else:
        if len(data) < 10:
            data.append({
                "name": _get_name(),
                "time": str(time),
                "score": str(score),
            })

    _save_leaderboard_data(data)

def view():
    clear_screen()

    data = _load_leaderboard_data()
    _print_leader_board(data)

    input("\nPress ENTER to continue.")
    return menu.enter