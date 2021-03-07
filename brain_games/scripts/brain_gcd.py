#!/usr/bin/env python
from brain_games import games, engine


def gcd_main():
    engine.start(games.gcd)


if __name__ == '__main__':
    gcd_main()














'''
import sys
import prompt
sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games/games')
from gcd_func import gcd_nod

def main():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    a, b, c = gcd_nod()
    if a == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\
 Let's try again, {}!".format(b, c, name))

if __name__ == '__main__':
    main()'''