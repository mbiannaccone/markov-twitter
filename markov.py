"""Generate markov text from text files."""


from random import choice
import sys

n = int(raw_input("What size would you like your n-grams to be? "))


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    f = open(file_path)

    text = f.read()

    f.close()

    return text


def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - (n - 1)):

        key = tuple(words[i:i + n])

        if key not in chains:
            chains[key] = []

        try:
            chains[key].append(words[i+n])
        except:
            chains[key].append(None)

    return chains


def make_text(chains, n):
    """Returns text from chains."""

    words = []

    # CAPITALIZATION
    upper_chains = []

    for key in chains.keys():
        if key[0][0].isupper():
            upper_chains.append(key)

    # PUNCTUATION: not functional yet ???
    # ends_with_punct = []

    # for key in chains.keys():
    #     if key[-1][-1] == ".":
    #         ends_with_punct.append(key)

    current_key = choice(upper_chains)
    words.extend(current_key)

    while True:
        new_link = choice(chains[current_key])
        words.append(new_link)
        current_key = tuple(words[-n:])
        if None in chains[current_key]:
            break

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text
