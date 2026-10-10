import random

def _parse_file(file_path):
    words = []

    with open(file_path, "r") as fh:
        for line in fh:
            words.append(line.strip().upper())

    return words

_words = {
    3: _parse_file("./words/length-three.txt"),
    4: _parse_file("./words/length-four.txt"),
    5: _parse_file("./words/length-five.txt"),
}

def get_random_words():
    bag = []

    for i in range(3, 6):
        popul = _words[i]
        bag += random.sample(popul, 7)
        # bag += popul[:7]

    random.shuffle(bag)
    return bag