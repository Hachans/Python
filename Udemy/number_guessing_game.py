import random


def get_integer(prompt: str) -> int:
    """
    Get an integer from Standart Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will enter,
        when they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a  valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        else:
            print("Please guess higher")