import prompt


def privet_user(module):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}! '.format(name))
    print(module.task)
    return name


def start(module):
    name = privet_user(module)
    i = 0
    while i < 3:
        question, result = module.new_round()
        print()
        print('Question: {}'.format(question))
        print()
        answer = prompt.string('Your answer: ')
        if answer.upper() != result:
            print()
            print("'{}' <--- is wrong answer ;(.Correct answer was '{}'. "
                  "Let's try again, {}!".format(answer.upper(), result, name))
            break
        print('Correct!')
        i += 1
    else:
        print('Congratulations, {}!'.format(name))
