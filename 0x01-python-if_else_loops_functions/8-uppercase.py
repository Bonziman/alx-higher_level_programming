#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= ord(char) <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
