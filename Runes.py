#!/usr/bin/env python3
import sys
import os.path

e2r_table = {
        'a':'ᚨ', 'b':'ᛒ', 'c':'ᚳ', 'd':'ᛞ', 'e':'ᛖ',
        'f':'ᚠ', 'g':'ᚷ', 'h':'ᚻ', 'i':'ᛁ', 'j':'ᛃ',
        'k':'ᚲ', 'l':'ᛚ', 'm':'ᛗ', 'n':'ᚾ', 'o':'ᛟ',
        'p':'ᛈ', 'q':'ᛩ', 'r':'ᚱ', 's':'ᛋ', 't':'ᛏ',
        'u':'ᚢ', 'v':'ᚡ', 'w':'ᚹ', 'x':'ᛪ', 'y':'ᚣ',
        'z':'ᛉ',
        }

r2e_table = {
        'ᚨ':'a', 'ᛒ':'b', 'ᚳ':'c', 'ᛞ':'d', 'ᛖ':'e',
        'ᚠ':'f', 'ᚷ':'g', 'ᚻ':'h', 'ᛁ':'i', 'ᛃ':'j',
        'ᚲ':'k', 'ᛚ':'l', 'ᛗ':'m', 'ᚾ':'n', 'ᛟ':'o',
        'ᛈ':'p', 'ᛩ':'q', 'ᚱ':'r', 'ᛋ':'s', 'ᛏ':'t',
        'ᚢ':'u', 'ᚡ':'v', 'ᚹ':'w', 'ᛪ':'x', 'ᚣ':'y',
        'ᛉ':'z',
        }

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
        for i in e2r_table:
            d = d.replace(i, e2r_table[i])

    if sys.argv[1] == '-d':
        d = s
        for i in r2e_table:
            d = d.replace(i, r2e_table[i])

    print(d)


if __name__ == "__main__":
    arguments = ('-e', '-d')

    if len(sys.argv) not in range(2, 4):
        print(help_message)
    elif sys.argv[1] not in arguments:
        print('you used wrong argument.')
        print(help_message)
    else:
        main()
