import sys
from random import randrange

FILENAME = "wordlists/500words/wordlist.txt"

OUTPUT_FILE = "wordlists//output.txt"

SAVING = False

MONOVOV = False

N = 100

DEBUG = True


def add_occurence(letter_freq: dict, previous_letter, letter, ):
    """
increases the count of letter "letter" folling the letter "previous_letter" in letter_freq
    :param letter_freq: the letter-frequency table
    :param previous_letter: the letter before "letter"
    :param letter: the letter following "previous_letter"
    """
    letter_freq.setdefault(previous_letter, {}).setdefault(letter, 0)
    letter_freq[previous_letter][letter] += 1


def next_letter(previous_letter, letter_freq: dict) -> str:
    """
Randomly chooses the next letter. Chances are based on the previous letter and the given frequencies in letter_freq
    :param previous_letter: the letter before the one being generated
    :param letter_freq: the table of letter-frequencies
    :return: the next letter following the previous one
    """
    possibility_space = 0
    # building sum of all frequencies
    for key in letter_freq[previous_letter]:
        possibility_space += letter_freq[previous_letter][key]
    choice = randrange(possibility_space)
    entropy = 0
    # collapsing space-time until a letter emerges
    for key in letter_freq[previous_letter]:
        if entropy + letter_freq[previous_letter][key] > choice:
            return key
        else:
            entropy += letter_freq[previous_letter][key]


def is_vovel(letter: str) -> bool:
    if len(letter) == 1:
        for v in ["a", "e", "i", "o", "u"]:
            if letter.count(v) == 1:
                return True
        return False


def format_word(word: str) -> str:
    """
formats a word by removing linebreaks changing it to lowercase
    :param word: the word to format
    :return: the formatted word
    """
    word = word.lower()
    lbi = word.find("\n")
    if lbi > 0:
        word = word[:lbi]
    return word


def analyze_words(words: list) -> dict:
    letter_freq: dict = {}
    for word in words:
        for i, l in enumerate(word.lower()):
            if i == 0:
                add_occurence(letter_freq, "0", l)
            else:
                add_occurence(letter_freq, word[i - 1], l)
        add_occurence(letter_freq, word[len(word) - 1], "1")
    return letter_freq


def invent_words(letter_freq: dict, n:int = 10, blacklist: list = [], monovov: bool = False) -> list:
    """
invents words based on the given word-frequency table.
    :param letter_freq: the letter-frequency table
    :param n: the number of words to invent
    :param blacklist: a blacklist of words (to avoid inventing existing words)
    :param monovov: should the generated words use only a single vovel
    :return: a list of invented words
    """
    #TODO: implement blacklist and duplication detection
    new_words: list = []
    for i in range(n):
        new_word = ""
        word_finished = False
        vovel_mode = ""
        while not word_finished:
            if len(new_word) == 0:
                new_word += next_letter("0", letter_freq)
            else:
                last_letter = new_word[len(new_word) - 1]
                letter = next_letter(last_letter, letter_freq)

                if monovov and is_vovel(letter):
                    if vovel_mode == "":
                        vovel_mode = letter
                    else:
                        letter = vovel_mode

                if letter == "1":
                    if 2 < len(new_word) < 10:
                        word_finished = True
                    else:
                        new_word = ""
                else:
                    new_word += letter

        new_words.append(new_word)
    return new_words


def open_wordlist(filename: str) -> list:
    """
opens a file containing a list of words, seperated by linebreaks
    :param filename: the filename to open
    :return: the list of words
    """
    with open(filename) as f:
        words = [format_word(word) for word in f.readlines()]
    return words


def run(input_filename: str, output_filename: str = "output.txt", n: int = 10, saving: bool = False, monovov: bool = False):
    words = open_wordlist(input_filename)
    letter_freq = analyze_words(words)

    print("using: " + str(sys.getsizeof(letter_freq)) + " bytes for letter_freq")
    print("found: " + str(len(letter_freq)) + " letters")
    print(letter_freq)

    new_words = invent_words(letter_freq, n, words, monovov)
    print(new_words)
    if saving:
        with open(output_filename, "w") as f:
            f.writelines((word + "\n" for word in new_words))


if __name__ == "__main__":
    run(FILENAME, OUTPUT_FILE, N, SAVING, MONOVOV)
