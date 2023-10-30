#!/usr/bin/python3
"""Module that prints a 2 lines after a special character"""


def text_indentation(text: str):
    """Function that prints a 2 lines after a special character

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input text is not a string.

    Prints:
        The input text with two new lines after each occurrence of a special character ('.', '?', ':').
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == " ":
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == " ":
                c += 1
            continue
        c += 1


# if __name__ == "__main__":
#     import doctest

#     doctest.testfile("tests/5-text_indentation.txt")


text_indentation("    Hello?")
text_indentation("Lorem ipsum dolor sit amet")
text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
text_indentation("       Lorem ipsum dolor sit amet.      ")
text_indentation("Hello. How are you? I'm fine.")
