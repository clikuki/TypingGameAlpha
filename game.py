import time
from utils import asciify, stringify_float_with_zeros, clear_screen, flush_terminal
from words import get_random_words
import leaderboard

def _get_score(word):
    length = len(word)
    if length == 3: return 2
    if length == 4: return 5
    if length == 5: return 7
    return 0

def _print_from_ascii_rows(pretext, word):
    ascii_rows = asciify(word)

    print(pretext + ascii_rows[0])
    pretext_len = len(pretext)
    for row in ascii_rows[1:]:
        print(" " * pretext_len + row)

def _run_game(word_set):
    word_list = get_random_words(word_set)
    start_time = time.time()
    score = 0
    incorrects = []

    for word in word_list:
        clear_screen()
        _print_from_ascii_rows("Your word is ", word)
        typed_word = input("Typing: ").upper()

        if typed_word == word:
            score += _get_score(word)
        else:
            incorrects.append((word, typed_word))

    clear_screen()
    
    duration = time.time() - start_time

    return (score, duration, incorrects)

def _print_count_up(goal, pretext, posttext, round_by):
    for t in range(101):
        t /= 100
        i = (1-t) ** 0.5 - 1 # ease-in
        progress = i * i
        value = round(goal * progress, round_by)

        if type(value) is float:
            value = stringify_float_with_zeros(value, 2)
        else:
            value = str(value)

        print("\r" + pretext + value + posttext, end="", flush=True)
        time.sleep(0.01)
    time.sleep(0.4)
    print("")

def _display_results(score, duration, incorrects):
    _print_count_up(score   , "You got a score of ", " points.", None)
    _print_count_up(duration, "You took "          , " s."     , 2   )

    mistakes = len(incorrects)
    if mistakes == 0:
        print("You made no mistakes.")
    else:
        _print_count_up(mistakes, "You made ", " mistakes.", None)

        print("\n" + "═" * 24)
        print("ACTUAL".center(12) + "RECIEVED".center(12))
        print("─" * 24)
        for word, typed_word in incorrects:
            time.sleep(0.01)
            print(word.center(10), "->", (typed_word or "<EMPTY>").center(10))
        print("═" * 24)

    time.sleep(0.6)

def start(word_set):
    clear_screen()
    print(
        "\nInstructions:"
        "\n You will be presented with 7 3-letter words, 7 4-letter words, and 7 5-letter words, in random order."
        "\n Type them as they come, and press enter to confirm your word. Longer words give more points."
    )
    
    # Return to menu if canceled
    choice = input("\nStart game? (Y/n) ")
    if choice.upper() == "N":
        return False

    third = 1/3
    for i in range(3):
        for j in range(1, 4):
            clear_screen()
            print("Starting in", 3-i, ("."*j).ljust(3), " ")
            time.sleep(third)

    flush_terminal()

    score, duration, incorrects = _run_game(word_set)
    _display_results(score, duration, incorrects)

    flush_terminal()
    input("\nPress ENTER to continue to leaderboard.") # block until user enters
    leaderboard.try_add_new_entry(score, duration)
    return True