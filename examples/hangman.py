"""This Python module contains classes for playing a game of Hangman."""

import random
import string

class AlreadyGuessedError(Exception):
    """Raised when a letter has already been guessed for a HangmanGame."""

    def __init__(self, letter):
        self._letter = letter

    def __str__(self):
        return 'The letter %s was already guessed' % self._letter


class HangmanGame(object):
    """Class for managing a game of Hangman."""

    def __init__(self, wordlist=None, length=None, word=None):
        """"Constructor for the HangmanGame.

        wordlist: a list of words from which to choose a random word
        length: the length of the word to choose from the wordlist.  Defaults
            to a random number between 5 and 8 letters.
        word: if specified, the word to guess, wordlist and length are ignored

        """
        # internal game tracking variables
        self._guesses = [] # the list of letters the player already guessed
        self._correct = 0 # the number of correctly guessed letters
        self._incorrect = 0 # the number of incorrectly guessed letters

        # if the word wasn't specified, then try to pick one
        if word is None:
            word = ""
            
            # if length wasn't specified, pick a random length from 5-8 letters
            if length is None:
                length = random.randint(5, 8)
            
            # keep picking a word from the wordlist until the length
            # of the word matches the target word length
            while len(word) != length:
                word = random.choice(wordlist)

        # track the word and the word length
        self._word = word
        self._length = len(word)

    def get_word(self):
        """Returns the word being guessed."""
        return self._word

    def guess(self, letter):
        """Guess a letter.  Returns True if the letter is in the word,
        False otherwise.

        letter: The letter to guess

        """
        # if the letter had already been guessed, then raise an exception
        if letter in self._guesses:
            raise AlreadyGuessedError(letter)

        # track the guessed letter
        self._guesses.append(letter)

        # check to see if the letter is in the word
        if letter in self._word:
            # yes, so add the number of occurrances of the letter in the word
            # to the number of correct guesses and return True
            self._correct += string.count(self._word, letter)
            return True
        else:
            # no, so add to the number of incorrect guesses and return False
            self._incorrect += 1
            return False

    def number_guesses(self):
        """Returns the number of guesses that have been made so far."""
        return len(self._guesses)

    def number_incorrect(self):
        """Returns the number of incorrect guesses that have been made."""
        return self._incorrect

    def is_won(self):
        """Returns True if the game has been won (all letters guessed),
        False otherwise.

        """
        return len(self._word) == self._correct

    def __str__(self):
        """Return a string representation of the current state of the game,
        the word with the correctly guessed letters or a blank.

        """
        return ''.join([
            ' %s ' % (letter if letter in self._guesses else '_')
            for letter in self._word
        ])


if __name__ == '__main__':
    # read the wordlist from a stock dictionary file
    wordlist = [w.strip() for w in file('words').readlines()]

    # create a new game
    game = HangmanGame(wordlist)

    # allow the player to keep guessing until 8 incorrect guesses
    while game.number_incorrect() < 8:
        print(game)
        print('You have %s guesses left' % (8 - game.number_incorrect()))

        # send the next guess to the game and check the outcome
        if game.guess(raw_input()):
            print('You made a correct guess!')
        else:
            print('You made an incorrect guess')

        # check to see if the game has been won
        if game.is_won():
            break

        print('You have made %s guesses' % game.number_guesses())

    # the game is over, determine the outcome
    if game.is_won():
        print('You won!')
    else:
        print('You lose!')
    print('The word was: %s' % game.get_word())

__all__ = ['AlreadyGuessedError', 'HangmanGame']

# This example is part of "import this"
# "import this" (c) 2013 by Nicholas Borko
#
# This presentation and accompanying code is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see http://creativecommons.org/licenses/by-nc-sa/3.0/.

