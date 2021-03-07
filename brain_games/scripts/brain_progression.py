#!/usr/bin/env python
from brain_games import games, engine


def progression_main():
    engine.start(games.progression)


if __name__ == '__main__':
    progression_main()




























'''import sys
import prompt
sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games/games')
from prog_funk import progression_funk

def main():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    a, b ,c ,d = progression_funk()
    if a == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print('Question: ', *b)
        print('Your answer: ', c)
        print("'{}' is wrong answer ;(. Correct answer was '{}'. \
Let's try again, {}!".format(c, d, name))

if __name__ == '__main__':
    main()'''