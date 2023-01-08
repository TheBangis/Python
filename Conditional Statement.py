# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Tasks for today (Join and Append)

#Condition statement


mark = int(input("enter student marks: "))
if(mark < 40):
    result = "F"
elif(mark < 45):
    result = "E"
elif(mark < 50):
    result = "D"
elif(mark < 60):
    result = "C"
elif(mark < 70):
    result = "B"
elif(mark <= 100):
    result = "A"
else:
    result = "Out of Range"
print(result)



