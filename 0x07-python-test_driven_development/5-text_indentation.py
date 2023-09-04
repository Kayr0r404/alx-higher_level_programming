#!/usr/bin/python3

def text_indentation(text):
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        new_text += i
        if (i == "." or i == "?" or i == ":"):
            print(new_text.lstrip())
            new_text = ""
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")