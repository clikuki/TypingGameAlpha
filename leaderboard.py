import os
from utils import clear_screen

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

def _print_leader_board(data):
    print(" " + " LEADERBOARD ".center(45, "─") + " ")
    print("╓─────────────────────────────────────────────╖")
    print("║ RANK    NAME         TIME             SCORE ║")
    print("╟─────────────────────────────────────────────╢")

    if data:
        for i,entry in enumerate(data):
            g_name = entry["name"]
            g_time = entry["time"]
            g_score = entry["score"]
            
            row = ("[" + str(i+1) + "]").rjust(4) + " "
            row += "   " + g_name.ljust(5).ljust(12, "─")
            row += (" "+str(g_time).rjust(5)+" ").ljust(19, "─")
            row += str(g_score).rjust(3) + " "
            print("║ " + row + " ║")
    else:
        print("║             No past games found.            ║")
        print("║    Play a couple games to fill this out!    ║")

    print("╙─────────────────────────────────────────────╜")

def view():
    clear_screen()

    data = _load_leaderboard_data()
    _print_leader_board(data)

    input("\nPress ENTER to continue.")