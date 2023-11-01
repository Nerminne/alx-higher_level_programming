#!/usr/bin/python3

def remove_char_at(str, n):
    x = 0
    s = ""
    for m in str:
        if x != n:
            s += m
        x += 1
    return (s)
