import random
#from itertools import islice, count

task = 'What number is missing in the progression?'

#SIZE = 10


'''def new_round():
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
    return question, str(answer)'''


import random
#import prompt

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
        
    question = ''.join(str(the_progression)[1 : -1])
    answer = str(hidden_number)
    return question, answer

