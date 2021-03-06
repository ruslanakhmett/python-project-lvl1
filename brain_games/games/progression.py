import random
from itertools import islice, count

task = 'What number is missing in the progression?'

SIZE = 10


def new_round():
    seq = list(islice(count(
               start=random.randint(10, 60),
               step=random.randint(1, 10)),
               SIZE))
    answer = random.choice(seq)
    index_num = seq.index(answer)
    seq[index_num] = '..'
    for i, _ in enumerate(seq):
        seq[i] = str(seq[i])
    question = ', '.join(seq)
    return question, str(answer)













'''import random
import prompt

def progression_funk():
    counter = 0
    while counter < 3:
        the_progression = []
        lenght_prog = random.randint(5, 10)
        hide_position = random.randrange(1, lenght_prog + 1)
        step_for_progression = random.randrange(1, 7)
        start_number = random.randrange(10)
        
        for i in range(1, lenght_prog + 1):
            if i == hide_position:
                the_progression.append('..')
                hidden_number = start_number + step_for_progression
                start_number += step_for_progression
            else:
                the_progression.append(start_number + step_for_progression)
                start_number += step_for_progression
        
        print('Question:', *the_progression)
        user_answer = int(prompt.string('Your answer: '))
        if user_answer != hidden_number:
            break
        else:
            print('Correct!')
            counter += 1
    return counter, the_progression, user_answer, hidden_number'''
