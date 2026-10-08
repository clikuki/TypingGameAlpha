import time
from utils import clear_screen, print_separator
import leaderboard
import menu

def _run_game():
    # TODO: replace word list with randomized grab from word bank
    word_list = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]

    start_time = time.time()
    
    score = 0
    scoring = (0,0,0,2,5,7)
    incorrects = []
    for word in word_list:
        clear_screen()
        print_separator()
        print("Your word is \"" + str(word) + "\"\n")
        typed_word = input("Typing: ").upper()
        
        if typed_word == word:
            score += scoring[len(word)]
        else:
            incorrects.append((word, typed_word))

    duration = round(time.time() - start_time, 2)

    return (score, duration, incorrects)

def _handle_results(score, duration, incorrects):
    print_separator()
    print("You got a score of " + str(score) + ", and took " + str(duration) + "s.")

    print("\nIncorrect words:\n")
    for word, typed_word in incorrects:
        print(word, "->", typed_word or "<EMPTY>")

def start():
    clear_screen()
    print_separator()
    print(
        "\nInstructions:"
        "\n You will be presented with 7 3-letter words, 7 4-letter words, and 7 5-letter words, in random order."
        "\n Type them as they come, and press enter to confirm your word. Longer words give more points."
    )
    
    # Return to menu if canceled
    choice = input("\nStart? (Y/n) ")
    if choice.upper() == "N":
        return menu.enter

    score, duration, incorrects = _run_game()
    _handle_results(score, duration, incorrects)

    input("\nPress ENTER to continue to leaderboard.") # block until user enters
    return leaderboard.view