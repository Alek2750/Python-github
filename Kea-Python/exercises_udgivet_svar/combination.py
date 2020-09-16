#!/usr/bin/python3
chars="abcd"

for i in range(len(chars)):
    for k in range(len(chars)):
        for m in range(len(chars)):
            print(chars[i]+chars[k]+chars[m],end=", ")
                

