"""Generate Markov text from text files."""

# from random import choice
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    content = open(file_path).read()

    return content


# print(open_and_read_file('green-eggs.txt')


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # How is this file coming in here

    # split file text
    words = text_string.split()
    words.append(None)

    # Initiate empty dictionary
    chains = {}

    for i in range(len(words) - 2):
        # our key
        key = (words[i], words[i + 1])
        # our value
        value = words[i + 2]

        #chains[key] = value
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]

    return chains

# return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # print(chains)
    # your code goes here
    # words.append(chains.keys())
    random_key = random.choice(list(chains.keys()))
    random_value = random.choice(list(chains.values()))
    # print(words)
    # print(words)
    # return ' '.join(words)

    while True:
        words.append(random_key)
        words.append(random_value)

    print(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
