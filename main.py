import os
#import subprocess
from time import sleep

def clear_screen():
    os.system("clear")
    # subprocess.run("clear", shell=True)

def get_logo_strings():
    if os.get_terminal_size()[0] <= 70:
        return (
            r"╓─────────────────────────────────────────────────────────────╖",
            r"║                                                             ║",
            r"║      /████████                  /██                         ║",
            r"║     |__  ██__/                 |__/                         ║",
            r"║        | ██ /██   /██  /██████  /██ /███████   /██████      ║",
            r"║        | ██| ██  | ██ /██__  ██| ██| ██__  ██ /██__  ██     ║",
            r"║        | ██| ██  | ██| ██  \ ██| ██| ██  \ ██| ██  \ ██     ║",
            r"║        | ██| ██  | ██| ██  | ██| ██| ██  | ██| ██  | ██     ║",
            r"║        | ██|  ███████| ███████/| ██| ██  | ██|  ███████     ║",
            r"║        |__/ \____  ██| ██____/ |__/|__/  |__/ \____  ██     ║",
            r"║             /██  | ██| ██                     /██  \ ██     ║",
            r"║            |  ██████/| ██                    |  ██████/     ║",
            r"║             \______/ |__/                     \______/      ║",
            r"║       /██████                                               ║",
            r"║      /██__  ██                                              ║",
            r"║     | ██  \__/  /██████  /██████/████   /██████             ║",
            r"║     | ██ /████ |____  ██| ██_  ██_  ██ /██__  ██            ║",
            r"║     | ██|_  ██  /███████| ██ \ ██ \ ██| ████████            ║",
            r"║     | ██  \ ██ /██__  ██| ██ | ██ | ██| ██_____/            ║",
            r"║     |  ██████/|  ███████| ██ | ██ | ██|  ███████            ║",
            r"║      \______/  \_______/|__/ |__/ |__/ \_______/            ║",
            r"║                                                             ║",
            r"║       /██████  /██           /██                            ║",
            r"║      /██__  ██| ██          | ██                            ║",
            r"║     | ██  \ ██| ██  /██████ | ███████   /██████             ║",
            r"║     | ████████| ██ /██__  ██| ██__  ██ |____  ██            ║",
            r"║     | ██__  ██| ██| ██  \ ██| ██  \ ██  /███████            ║",
            r"║     | ██  | ██| ██| ██  | ██| ██  | ██ /██__  ██            ║",
            r"║     | ██  | ██| ██| ███████/| ██  | ██|  ███████            ║",
            r"║     |__/  |__/|__/| ██____/ |__/  |__/ \_______/            ║",
            r"║                   | ██                                      ║",
            r"║                   | ██                                      ║",
            r"║                   |__/                                      ║",
            r"╙─────────────────────────────────────────────────────────────╜",
        )
    else:
        return (
            r"╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖",
            r"║                                                                                                                                                  ║",
            r"║  /████████                  /██                        /██████  /██           /██                    /██████                                     ║",
            r"║ |__  ██__/                 |__/                       /██__  ██| ██          | ██                   /██__  ██                                    ║",
            r"║    | ██ /██   /██  /██████  /██ /███████   /██████   | ██  \ ██| ██  /██████ | ███████   /██████   | ██  \__/  /██████  /██████/████   /██████   ║",
            r"║    | ██| ██  | ██ /██__  ██| ██| ██__  ██ /██__  ██  | ████████| ██ /██__  ██| ██__  ██ |____  ██  | ██ /████ |____  ██| ██_  ██_  ██ /██__  ██  ║",
            r"║    | ██| ██  | ██| ██  \ ██| ██| ██  \ ██| ██  \ ██  | ██__  ██| ██| ██  \ ██| ██  \ ██  /███████  | ██|_  ██  /███████| ██ \ ██ \ ██| ████████  ║",
            r"║    | ██| ██  | ██| ██  | ██| ██| ██  | ██| ██  | ██  | ██  | ██| ██| ██  | ██| ██  | ██ /██__  ██  | ██  \ ██ /██__  ██| ██ | ██ | ██| ██_____/  ║",
            r"║    | ██|  ███████| ███████/| ██| ██  | ██|  ███████  | ██  | ██| ██| ███████/| ██  | ██|  ███████  |  ██████/|  ███████| ██ | ██ | ██|  ███████  ║",
            r"║    |__/ \____  ██| ██____/ |__/|__/  |__/ \____  ██  |__/  |__/|__/| ██____/ |__/  |__/ \_______/   \______/  \_______/|__/ |__/ |__/ \_______/  ║",
            r"║         /██  | ██| ██                     /██  \ ██                | ██                                                                          ║",
            r"║        |  ██████/| ██                    |  ██████/                | ██                                                                          ║",
            r"║         \______/ |__/                     \______/                 |__/                                                                          ║",
            r"║                                                                                                                                                  ║",
            r"╙──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╜",
        )

def print_logo_startup():
    startup_strings = get_logo_strings()

    size = 0
    for row in startup_strings:
        row_size = len(row)
        if size < row_size:
            size = row_size
            
    for i in range(size + len(startup_strings) * 2):
        clear_screen()

        curr_str = ""
        for j,row in enumerate(startup_strings):
            row_slice_idx = i-j*2

            if row_slice_idx <= 0:
                break
            
            curr_str += row[:row_slice_idx] + "\n"

        print(curr_str)
        sleep(0.01)

    sleep(0.5)

def print_logo_normal():
    startup_strings = get_logo_strings()
    print("\n".join(startup_strings) + "\n")

def print_menu(do_slow):
    print("[1] -----------     Start Game     ----------")
    if do_slow: sleep(0.02)
    print("[2] -----------  View Leaderboard  ----------")
    if do_slow: sleep(0.02)
    print("[0] -----------        Exit        ----------")
    if do_slow: sleep(0.02)

def enter_menu():
    last_input = None
    while True:
        print_menu(last_input == None)
        
        if last_input != None:
                print("\nInvalid option \"", last_input, "\".")
        else:
                print("")
        choice = input("What would you like to do? ")

        if choice == "1":
                return start_game
        if choice == "2":
                return view_leaderboard
        if choice == "0":
                clear_screen()
                return

        # Invalid option, redraw screen
        last_input = choice
        clear_screen()
        print_logo_normal()

def print_separator():
    size_x,_ = os.get_terminal_size()
    print("─" * size_x)

def start_game():
    clear_screen()
    # TODO: replace word list with randomized grab from word bank
    word_list = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
    
    print_separator()
    print(
        "\nInstructions:"
        "\n You will be presented with 7 3-letter words, 7 4-letter words, and 7 5-letter words, in random order."
        "\n Type them as they come, and press enter to confirm your word. Longer words give more points."
    )
    
    # Return to menu if canceled
    choice = input("\nStart? (Y/n) ")
    if choice.upper() == "N":
        return enter_menu
    
    score = 0
    scoring = (0,0,0,2,5,7)
    incorrects = []
    for word in word_list:
        print_separator()
        print("Your word is \"" + str(word) + "\"\n")
        typed_word = input("Typing: ").upper()
        
        if typed_word == word:
            score += scoring[len(word)]
        else:
            incorrects.append((word, typed_word))
    
    print_separator()
    print("Your score is \"", score, "\".")
    print("Incorrect words:")
    for word, typed_word in incorrects:
        print(word, "->", typed_word)

    input("\nPress enter to continue to leaderboard.") # block until user enters

def view_leaderboard():
    print("view leaderboard")

def main():
    #print_logo_startup()

    page = enter_menu
    while page != None:
        page = page()

main()
