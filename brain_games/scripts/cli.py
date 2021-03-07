import prompt


def main():
    pass


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


if __name__ == '__main__':
    main()
