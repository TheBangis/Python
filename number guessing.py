# -*- coding: utf-8 -*-
import random 
"""
Spyder Editor

This is a temporary script file.
"""

# Tasks for today (Join and Append)

#Condition statement

num = random.randint(5, 10)
n = 1
while n <= 3:
    n = n + 1
    guess = int(input("guess number btw 5 - 10: "))
    if(guess == num):
        print("Congratulation!") 
        break
    else:
        print("Wrong, try again")
p 
