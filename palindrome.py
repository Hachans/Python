def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    Palindrome is a string that reads the same from both sides.

    :param string: The string to check.
    :return: True if `string` is palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    Palindrome is a string that reads the same way from both sides.

    Function ignore whitespaces, capitalization and punctuation
    in the sentence.

    :param sentence: Sentence to check
    :return: True if sentence is a palindrome, False otherwise
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
