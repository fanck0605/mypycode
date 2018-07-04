# -*- coding: utf-8 -*-

age = int(input('Please Enter Your Age: '))

def agejudge(x):
    if 0 <= x <=100:
        if x >= 18:
            print('Hello, Adult!')
        elif x >= 6:
            print('Hello, Teenager!')
        else:
            print('Hello, Kid!')
    else:
        age = int(input('Please Enter Your Correct Age: '))
        agejudge(age)

agejudge(age)
