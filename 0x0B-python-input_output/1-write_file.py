#!/usr/bin/python3
"""
function that writes a string to text file
returns the number of characters written
"""


def write_file(filename="", text=""):
    """ using "w" to overwrite the content """
    with open(filename, "w", encoding='utf=8') as text_file:
        length = text_file.write(text)
        return (length)
