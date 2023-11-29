#!/usr/bin/python3
count = 0
for i in range(0, 9):
    for j in range(i + 1, 10):
        if count > 0:
            print(',', end=' ')
        print('{}'.format(chr(i + ord('0'))), end='')
        print('{}'.format(chr(j + ord('0'))), end='')
        count += 1
