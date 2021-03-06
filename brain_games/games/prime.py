import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def prime_check(num):
    k = 0
    for i in range(2, (num + 1) // 2):
        if num % i == 0:
            k += 1
    if k <= 0:
        return True
    else:
        return False


def new_round():
    question = random.randint(1, 500)
    answer = prime_check(question)
    if answer is True:
        answer = 'YES'
    else:
        answer = 'NO'
    return question, answer
















'''import prompt
import random

def prime_not_prime():
    counter = 0
    while counter != 3:
        the_number = random.randrange(2, 15)
        print('Question:', the_number)
        user_answer = prompt.string('Your answer: ')

        k = 0
        for i in range(2, (the_number + 1) // 2):
            if (the_number % i == 0):
                k += 1
        if k <= 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        if user_answer == true_answer:
            print('Correct!')
            counter += 1
        else:
            break
    return counter, user_answer, true_answer'''


        