#!/usr/bin/python3
"""
function that appends a string at the end of a text file
returns the number of characters added
"""


def append_write(filename="", text=""):
    """ using "a" to add text at the end of file """
    with open(filename, "a", encoding='utf-8') as text_file:
        length = text_file.write(text)
        return (length)
