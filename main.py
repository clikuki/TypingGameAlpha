import os
import sys
from time import sleep
from utils import clear_screen
import startup
    
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
                return

        # Invalid option, redraw screen
        last_input = choice
        clear_screen()
        startup.print_fast()

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
    return view_leaderboard

def view_leaderboard():
    print("view leaderboard")

def main():
    args = sys.argv[1:]
    if len(args) > 0 and "skip" in args:
        startup.print_fast()
    else:
        startup.print_animation()

    # rudimentary page system
    # each page function runs its own logic, then returns the next page function to switch pages
    # returning no page clears the screen before closing the program
    page = enter_menu
    while page != None:
        page = page()

    clear_screen()

main()
