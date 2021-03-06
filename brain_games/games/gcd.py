import random

task = 'Find the greatest common divisor of given numbers.'


def check_gcd(x, y):
    w = [x, y]
    w.sort()
    a, b = w
    if b % a == 0:
        return a
    i = a
    while   i >= 1:
        if b % i == 0 and a % i == 0:
            return i
        i -= 1

def new_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    question = '{} {}'.format(num1, num2)
    answer = str(check_gcd(num1, num2))
    return question, answer










'''import random
import prompt

def gcd_nod():
    counter = 0
    while counter != 3:
        the_number1 = random.randrange(99)
        the_number2 = random.randrange(99)
        s = []
        print('Question:', the_number1, the_number2 )
        user_answer = int(prompt.string('Your answer: '))
        
        for i in range(1, 100):
            if the_number1 % i == 0 and the_number2 % i == 0:
                s.append(i)
                result = max(s)
        if user_answer == int(result):
            print('Correct!')
            counter += 1
        else:
            break
    return counter, user_answer, result   '''
