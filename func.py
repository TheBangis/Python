# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 21:24:06 2023

@author: Bangis
"""

def plus_ten(ten):
    return ten + 10

def add_ten(ten):
    return ten + 10

print("Call plus ten function")
fun_plus_ten = plus_ten(10)
print("plus ten {}".format(fun_plus_ten))
print("call add ten::")
fun_add_ten = add_ten(10)
print("add ten {}".format(fun_add_ten))

def readable(days):
    
    weeks = days // 7
    
    reminders = days % 7
    
    return (weeks, reminders)
print(readable(10))