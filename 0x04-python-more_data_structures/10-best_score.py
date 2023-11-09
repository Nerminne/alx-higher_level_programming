#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        max_value = max(a_dictionary.values())
        best_key = None
        for key in a_dictionary:
            if (a_dictionary[key] == max_value):
                return (key)
    else:
        return (None)
