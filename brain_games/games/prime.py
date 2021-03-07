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
