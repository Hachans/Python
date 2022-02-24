def fizz_buzz(n: int) -> str:
    """
    Game to play vs computer to test your math.

    :param n: `int` to check if it divides by 3, 5 or both
    :return: Returns "fizz buzz" if divides by 3 and 5,
    "buzz" if only by 5, "fizz" if only by 3.
    If `n` does not divide by either, returns the number.
    """
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    return str(n)


input("Press `Enter` to play Fizz Buzz.")
print()
i = 0
correct_answer = 0
while i < 99:
    i += 1
    print(fizz_buzz(i))
    i += 1
    correct_answer = fizz_buzz(i)
    player_answer = input("Your go: ")
    if player_answer != correct_answer:
        print("You loose, correct answer was {}".format(correct_answer))
        break
else:
    print("You won!! You reached {}".format(correct_answer))
