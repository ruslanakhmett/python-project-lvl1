#!/usr/bin/env python
from brain_games import games, engine


def calc_main():
    engine.start(games.calc)


if __name__ == '__main__':
    calc_main()














'''#import sys
import prompt
#sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games/games')
from brain_games.games import *

def main():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    a, b, c = games.calc_fun()
    if a == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\
 Let's try again, {}!".format(b, c, name))

if __name__ == '__main__':
    main()'''