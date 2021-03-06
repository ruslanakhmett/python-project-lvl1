import random
from operator import mul, sub, add


task = 'What is the result of the expression?'

OPERATORS = ((add, '+'), (sub, '-'), (mul, '*'))


def new_round():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    operation, sym = random.choice(OPERATORS)
    question = '{} {} {}'.format(num1, sym, num2)
    answer = str(operation(num1, num2))
    return question, answer







'''
def calculate():
    counter = 0
    while counter != 3:
        the_number1 = random.randrange(99)
        the_number2 = random.randrange(99)
        operator = random.choices(['+', '-', '*'])
        result = int(eval(str(the_number1) + ''.join(operator) + str(the_number2)))
        print('Question:', the_number1, ''.join(operator), the_number2 )
        user_answer = int(prompt.string('Your answer: '))
        
        if result != user_answer:
            break
        else:
            print('Correct!')
            counter += 1
    return counter, user_answer, result'''


