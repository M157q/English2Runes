#!/usr/bin/env python3
import sys
import os.path
import string

intab   = string.ascii_lowercase
outtab  = "ᚨᛒᚳᛞᛖᚠᚷᚻᛁᛃᚲᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛪᚣᛉ"

help_message = \
'''
[Usage] $python3 ''' + sys.argv[0] + ''' -e|-d [file]
        -e: English to Runes
        -d: Runes to English
        use stdin when no file input
'''

def main():
    try:
        sys.argv[2]
    except IndexError:
        s = input()
    else:
        if os.path.exists(sys.argv[2]):
            f = open(sys.argv[2], 'r')
            s = f.read()
            f.close()
        else:
            print('File "' + sys.argv[2] + '" not exists!')
            sys.exit(1)

    if sys.argv[1] == '-e':
        d = s.lower()
        print(d.translate(str.maketrans(intab, outtab)))

    if sys.argv[1] == '-d':
        d = s
        print(d.translate(str.maketrans(outtab, intab)))



if __name__ == "__main__":
    arguments = ('-e', '-d')

    if len(sys.argv) not in range(2, 4):
        print(help_message)
    elif sys.argv[1] not in arguments:
        print('you used wrong argument.')
        print(help_message)
    else:
        main()
