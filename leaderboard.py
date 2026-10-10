import os
import time
from utils import clear_screen, flush_terminal


def _load_leaderboard_data():
    leaderboard_path = "leaderboard.dat"
    if not os.path.exists(leaderboard_path):
        return []

    data = []
    with open(leaderboard_path, "r") as fh:
        for line in fh:
            line = line.strip().split(",")
            data.append({
                "name": line[0],
                "time": line[1],
                "score": line[2],
            })

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
            fh.write(",")
            fh.write(g_time)
            fh.write(",")
            fh.write(g_score)
            fh.write("\n")

def _row_update_print(row_strings, transformations, replace):
    for t in transformations:
        idx = t[0]
        new_row = t[1]

        if len(t) > 2:
            sleep_dur = t[2]
        else:
            sleep_dur = 0.01
        
        clear_screen()
        print("\n".join(row_strings))
        if replace:
            row_strings[idx] = new_row
        else:
            row_strings.insert(idx, new_row)

        time.sleep(sleep_dur)
    
    clear_screen()
    print("\n".join(row_strings))

def _print_leader_board(data):
    strings = [
        " " + " LEADERBOARD ".center(45, "─") + " ",
    ]

    # first draw: empty box expanding downwards
    new_rows = [
        (1, "╓─────────────────────────────────────────────╖"),
        (2, "╙─────────────────────────────────────────────╜"),
        (2, "║                                             ║"),
        (3, "╟─────────────────────────────────────────────╢"),
    ]

    row_cnt = len(data) or 2
    for i in range(row_cnt):
        new_rows.append((i+4, new_rows[2][1]))

    _row_update_print(strings, new_rows, False)
    time.sleep(0.3)

    # second draw: line-by-line entries
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

            g_time = float(entry["time"])
            g_time = str(round(g_time, 2)).split(".")
            g_time[1] = g_time[1].ljust(2, "0")
            g_time = ".".join(g_time).rjust(6)
            
            row = ("[" + str(i+1) + "]").rjust(4) + " "
            new_rows.append((i+4, "║ " + row.ljust(43) + " ║", 0.03))

            row += "   " + (g_name + " ").ljust(12)
            new_rows.append((i+4, "║ " + row.ljust(43) + " ║", 0.03))

            row += (" "+g_time+"  ").ljust(19)
            new_rows.append((i+4, "║ " + row.ljust(43) + " ║", 0.03))

            row += str(g_score).rjust(3) + " "
            new_rows.append((i+4, "║ " + row + " ║", 0.03))
    else:
        new_rows.extend([
            (4, "║             No past games found.            ║"),
            (5, "║    Play a couple games to fill this out!    ║"),
        ])

    _row_update_print(strings, new_rows, True)

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

    time.sleep(0.2)

    flush_terminal()
    input("\nPress ENTER to continue.")