#!/usr/bin/python3
"""
function that writes a string to a text file
returns the number of characters written
"""


def write_file(filename="", text=""):
    """ using "w" to overwrite the content """
    with open(filename, "w") as text_file:
        length = text_file.write(text)
        return (length)
