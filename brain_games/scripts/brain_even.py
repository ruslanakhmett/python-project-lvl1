#!/usr/bin/env python
from brain_games import games, engine


def questions_main():
    engine.start(games.even)


if __name__ == '__main__':
    questions_main()
















'''

import sys
sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games')
sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games/games')
import random
import sys
import prompt
sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games/games')
from even_not import even_not_even

def main():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    a, b, c = even_not_even()
    if a == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'. \
Let's try again, {}!".format(b, c, name))

if __name__ == '__main__':
    main()
'''