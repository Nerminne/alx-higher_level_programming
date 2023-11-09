#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (len(my_list) == 0):
        return (None)
    new_list = my_list.copy()
    index = new_list.index(search)
    new_list.remove(search)
    new_list.insert(index, replace)
    return (new_list)
