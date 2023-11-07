#!/usr/bin/python3
def multiple_returns(sentence):
    values = ()
    if (sentence):
        value = (len(sentence), sentence[0])
    else:
        value = (0, None)
    return (value)
