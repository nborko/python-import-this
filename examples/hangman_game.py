#!/usr/bin/env python

# Python script to play a game of hangman

import random
import string
import sys

# initialize game variables
word = "" # the word to guess
length = random.randint(5, 8) # the target length of the word, 5-8 letters
guesses = [] # a list of letters the player already guessed
correct = 0 # the number of correctly guessed letters
incorrect = 0 # the number of incorrectly guessed letters

# read the wordlist from a stock dictionary file
wordlist = [w.strip() for w in file('words').readlines()]

# pick a word from the wordlist
# keep picking until the length of the word matches the target word length
while len(word) != length:
    word = random.choice(wordlist)

# allow the player to keep guessing until 8 incorrect guesses
while incorrect < 8:

    # print the word with the correctly guessed letters or a blank
    print(''.join([
        ' %s ' % (letter if letter in guesses else '_')
        for letter in word
    ]))
    print('You have %s guesses left' % (8 - incorrect))

    # get the next guess
    letter = raw_input()

    # if the letter had already been guessed, then lose the game
    if letter in guesses:
        print('The letter %s was already guessed' % letter)
        incorrect = 8 # set a losing score
        break

    # track the guessed letter
    guesses.append(letter)

    # check to see if the letter is in the word
    if letter in word:
        # yes, so add the number of occurrances of the letter in the word
        # to the number of correct guesses
        correct += string.count(word, letter)
        print('You made a correct guess!')
    else:
        # no, so add to the number of incorrect guesses
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

# This example is part of "import this"
# "import this" (c) 2013 by Nicholas Borko
#
# This presentation and accompanying code is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see http://creativecommons.org/licenses/by-nc-sa/3.0/.

