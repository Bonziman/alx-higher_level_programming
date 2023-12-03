#!/usr/bin/python3
def element_at(my_list, idx):
    if idx not in range(0, len(my_list) - 1) or idx < 0:
        return "NONE"
    else:
        return my_list[idx]
