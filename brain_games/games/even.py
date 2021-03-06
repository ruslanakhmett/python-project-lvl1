import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'

def question_even(a):
    if a % 2 == 0:
        return 'YES'
    else:
        return "NO"

def new_round():
    question = random.randint(1, 50)
    answer = question_even(question)
    return question, answer













'''import prompt
import random


def even_not_even():
    counter = 0
    while counter != 3:
        the_number = random.randrange(99)
        print('Question:', the_number)
        user_answer = prompt.string('Your answer: ')
        
        if the_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
            counter += 1
            
        elif the_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            counter += 1
        else:
            if user_answer == 'yes':
                true_answer = 'no'
            else:
                true_answer = 'yes'
            break
    return counter, user_answer, true_answer'''
        
