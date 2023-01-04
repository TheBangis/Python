# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Tasks for today (Join and Append)

students = ['babangida', 'sani', 'hamza', 'aliyu']
print(len(students))
print(max(students))
print(min(students))
print(sorted(students))

students.append('abubakar')
students[-1] = 'sadik'
print('\n'.join(students))