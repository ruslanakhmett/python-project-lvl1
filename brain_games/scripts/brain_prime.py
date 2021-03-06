from brain_games import games, engine


def prime_main():
    engine.start(games.prime)


if __name__ == '__main__':
    prime_main()










'''
import sys
import prompt
sys.path.append('/home/ruslan/Desktop/python-project-lvl1/brain_games/games')
from brain_prime_funk import prime_not_prime

def main():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    a, b, c = prime_not_prime()
    if a == 3:
        print('Congratulations, {}!'.format(name))
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'. \
Let's try again, {}!".format(b, c, name))

if __name__ == '__main__':
    main()'''
