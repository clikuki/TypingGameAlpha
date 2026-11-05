import os
import time
from utils import row_update_print, stringify_float_with_zeros, clear_screen, flush_terminal

def _load_leaderboard_data():
    leaderboard_path = "leaderboard.dat"
    if not os.path.exists(leaderboard_path):
        return []

    data = []
    entry = []
    cnt = 0
    with open(leaderboard_path, "r") as fh:
        for line in fh:
            entry.append(line.strip())
            cnt += 1
            if cnt >= 3:
                data.append({
                    "name": entry[0],
                    "time": entry[1],
                    "score": entry[2],
                })

                cnt = 0
                entry.clear()

    return data

def _save_leaderboard_data(data):
    leaderboard_path = "leaderboard.dat"

    if len(data) > 10:
        data = data[:10]

    with open(leaderboard_path, "w") as fh:
        for entry in data:
            g_name = entry["name"]
            g_time = entry["time"]
            g_score = entry["score"]

            fh.write(g_name)
            fh.write("\n")
            fh.write(g_time)
            fh.write("\n")
            fh.write(g_score)
            fh.write("\n")

def _print_leader_board(data, no_anim):
    strings = [
        " " + " LEADERBOARD ".center(45, "─") + " ",
    ]

    # first draw: empty box expanding downwards
    new_rows = [
        # Top and bottom
        (1, "╓─────────────────────────────────────────────╖"),
        (2, "╙─────────────────────────────────────────────╜"),
        # Push bottom down with middle rows
        (2, "║                                             ║"),
        (3, "╟─────────────────────────────────────────────╢"),
    ]

    row_cnt = len(data) or 2
    for i in range(row_cnt):
        new_rows.append((i+4, new_rows[2][1]))

    row_update_print(strings, new_rows, False, no_anim)
    if not no_anim: time.sleep(0.3)

    # second draw: line-by-line entries
    # same index on header to overwrite row
    new_rows = [
        (2, "║ RANK                                        ║", 0.05),
        (2, "║ RANK    NAME                                ║", 0.05),
        (2, "║ RANK    NAME          TIME                  ║", 0.05),
        (2, "║ RANK    NAME          TIME            SCORE ║", 0.05),
    ]

    if data:
        for i,entry in enumerate(data):
            g_name = entry["name"]
            g_score = entry["score"]

            g_time = stringify_float_with_zeros(float(entry["time"]), 2).rjust(6)
            
            # Same idea above, but with entry data
            row = ("[" + str(i+1) + "]").rjust(4) + " "
            new_rows.append((i+4, "║ " + row.ljust(43) + " ║", 0.03))

            row += "   " + (g_name + " ").ljust(12)
            new_rows.append((i+4, "║ " + row.ljust(43) + " ║", 0.03))

            row += (" "+g_time+"  ").ljust(19)
            new_rows.append((i+4, "║ " + row.ljust(43) + " ║", 0.03))

            row += str(g_score).rjust(3) + " "
            new_rows.append((i+4, "║ " + row + " ║", 0.03))
    else:
        # Show empty msg all at once if no past games
        new_rows.extend([
            (4, "║             No past games found.            ║", 0.1),
            (5, "║    Play a couple games to fill this out!    ║", 0),
        ])

    row_update_print(strings, new_rows, True, no_anim)

def _get_name():
    err = ""
    while True:
        clear_screen()
        print("New entry on the leaderboard!")

        if err:
            print(err)

        name = input("\nEnter your initials: ")
        n_len = len(name)

        if n_len < 1 or n_len > 8:
            err = "Name must be from 1 to 8 characters long."
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

def clear():
    _save_leaderboard_data([])

def view(options_data):
    no_anim = "noAnim" in options_data

    clear_screen()

    data = _load_leaderboard_data()
    _print_leader_board(data, no_anim)

    if not no_anim:
        time.sleep(0.2)
        flush_terminal()
        
    input("\nPress ENTER to continue.")