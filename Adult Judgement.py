# -*- coding: utf-8 -*-

age = int(input('Please Enter Your Age: '))

if 0 <= age <=100:
    if age >= 18:
        print('Hello, Adult!')
    elif age >= 6:
        print('Hello, Teenager!')
    else:
        print('Hello, Kid!')
else:
    print('Please Enter Your Correct Age!')
