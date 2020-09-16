#!/usr/bin/python3

letters="abcdefghijklmnopqrstvwuxyz"

option=input("Would you like to encrypt [1] or decrypt [2]?: ")
text=input("Please enter the text?: ").lower()
key=int(input("Please enter the key?: "))
a=97
z=122

output=""

if option=="2":
    key=26+key*-1


for m in range(len(text)):
    char=ord(text[m])+key
    if char>z or char<a:
        output=output+chr(char-z+a-1)
    else:
        output=output+chr(char)
    

print("The result is: "+output)
