#!/usr/bin/python3
"""A model that defines a function to indentate text"""

def text_indentation(text):
    skip_next = False
    for i in text:
        if skip_next:
            skip_next = False
            continue
        if i == "\\":
            skip_next = True
            continue

        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print("")
            print("")
            skip_next = True
