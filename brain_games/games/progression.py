import random


task = 'What number is missing in the progression?'


def new_round():
    the_progression = []
    length_prong = random.randint(5, 10)
    hide_position = random.randrange(1, length_prong + 1)
    step_for_progression = random.randrange(1, 7)
    start_number = random.randrange(10)

    for i in range(1, length_prong + 1):
        if i == hide_position:
            the_progression.append('..')
            hidden_number = start_number + step_for_progression
            start_number += step_for_progression
        else:
            the_progression.append(start_number + step_for_progression)
            start_number += step_for_progression
    question = ''
    for elem in the_progression:
        question += str(elem) + ' '
    answer = str(hidden_number)
    return question, answer
