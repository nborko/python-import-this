"""Python module with functions to assist playing a game of hangman."""

import random
import string
import sys

# read the wordlist from a stock dictionary file
wordlist = [w.strip() for w in file('words').readlines()]

def random_word(length):
    """Pick a random word from the wordlist.

    length: The number of letters for the word

    """
    word = ""
    # keep picking until the length of the word matches the target word length
    while len(word) != length:
        word = random.choice(wordlist)
    return word

def word_progress(word, guesses):
    """Return the word string with the correctly guessed letters or a blank.

    word: The word being guessed
    guesses: A list of letters that have already been guessed

    """
    return ''.join([
        ' %s ' % (letter if letter in guesses else '_')
        for letter in word
    ])

def guess_letter(word, letter):
    """Check to see if the letter is in the word.  Returns the number of
    occurrances of the letter in the word.

    word: The word being guessed
    letter: The letter to check

    """
    return string.count(word, letter)

if __name__ == '__main__':
    # initialize game variables
    word = random_word(random.randint(5, 8)) # the word to guess, 5-8 letters
    guesses = [] # a list of letters the player already guessed
    correct = 0 # the number of correctly guessed letters
    incorrect = 0 # the number of incorrectly guessed letters

    # allow the player to keep guessing until 8 incorrect guesses
    while incorrect < 8:

        print(word_progress(word, guesses))
        print('You have %s guesses left' % (8 - incorrect))

        # get the next guess
        letter = raw_input()

        # if the letter had already been guessed, then lose the game
        assert letter not in guesses, \
            'The letter %s was already guessed' % letter

        # track the guessed letter
        guesses.append(letter)

        # check to see if the letter is in the word
        result = guess_letter(word, letter)
        if result > 0:
            # the letter was in the word, so add the number of occurrances
            # of the letter in the word to the number of correct guesses
            correct += result
            print('You made a correct guess!')
        else:
            # bad guess, add to the number of incorrect guesses
            incorrect += 1
            print('You made an incorrect guess')

        # check to see if the game has been won
        if len(word) == correct:
            break

        print('You have made %s guesses' % len(guesses))

    # the game is over, determine the outcome
    if incorrect < 8:
        print('You won!')
    else:
        print('You lose!')
    print('The word was: %s' % word)

__all__ = ['random_word', 'word_progress', 'guess_letter']

# This example is part of "import this"
# "import this" (c) 2013 by Nicholas Borko
#
# This presentation and accompanying code is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see http://creativecommons.org/licenses/by-nc-sa/3.0/.

