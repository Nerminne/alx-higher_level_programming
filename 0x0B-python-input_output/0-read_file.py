#!/usr/bin/python3
"""
Write a function that reads text file and prints it
"""


def read_file(filename=""):
    """ read file content and store it in string str """
    with open(filename, "r", encoding='utf=8') as text_file:
        text = text_file.read()
        print(text, end="")
