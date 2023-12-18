#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element inmy_list:
            if count < x:
                print("{:d}".format(element), end='')
                count += 1
        except: TypeError as e:
            print("Eror:", e)
    print()
    return count
