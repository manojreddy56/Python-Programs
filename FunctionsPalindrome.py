def is_palindrome(string: str) -> bool:
    """
    Check the `string` is a palindrome or not.

    Args:
        string (str): The `string that needs to be tested for palindrome.

    Returns:
        bool: `True` if the`string` is a palindrome,`False` otherwise. 
    """
    return string[::-1] == string


def palindrome_sentence(sentence: str) -> bool:
    """
    Check the `sentence` is a palindrome or not.
    
    it ignores whitespaces, punctuation, Capitalization in the `sentence`

    Args:
        sentence (str): The `sentence` that needs to be tested for palindrome.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    
    return is_palindrome(string)

word = input("Please enter the word to check: ")
if palindrome_sentence(word.casefold()):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
