#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    total = 0
    for i in range(len(my_list)):
        if (i == 0 or my_list[i] != my_list[i - 1]):
            total += my_list[i]
    return (total)
