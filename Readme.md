English to Runes  ᛖᚾᚷᛚᛁᛋᚻ ᛏᛟ ᚱᚢᚾᛖᛋ 
======================
A command line tool to switch English letters to [Runes letters][Runes] or vice versa.  
Written in Python3.  
I am just a Python newbie, so the code is rookie-like.  

[Runes]: http://en.wikipedia.org/wiki/Runes

Usage  ᚢᛋᚨᚷᛖ
------

```
$python3 runes.py -e|-d [file]

     -e: English to Runes
     -d: Runes to English

    Use stdin when no file be specified.
```

```
$ echo "English to Runes" | python3 runes.py -e
> ᛖᚾᚷᛚᛁᛋᚻ ᛏᛟ ᚱᚢᚾᛖᛋ
```

```
$ echo "English to Runes" | python3 runes.py -e | python3 runes.py -d
> english to runes
```
Runes letters are case-insensitive, so I only trans Runes letters to English letters in lowecase.

`$ python3 runes.py -e Readme.md > Readme_Runes.md`  
Generated [this markdown file](examples/Readme_Runes.md) which is this readme in Runes version.


Screenshot   ᛋᚳᚱᛖᛖᚾᛋᚻᛟᛏ  
--------     
![1](http://i.imgur.com/u2r07ww.jpg)



License  ᛚᛁᚳᛖᚾᛋᛖ
----------
Copyright &copy; 2013 m157q  
Licensed under the [GPL license][GPL].

[GPL]: http://www.gnu.org/licenses/gpl.html
