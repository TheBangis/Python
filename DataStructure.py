# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:14:16 2023

@author: Bangis
"""
list_of_random_things = [1, 'a string', True, 8]
list_of_random_things[0] = 'one'
print(list_of_random_things[0])
#above code showed list is a mutable data structure

#print the items data using for loop
for i in list_of_random_things:
    print(i)
    
#String
name = 'Babangida'
print('\n')
print(name[:4])

# Tasks for today (Join and Append)

students = ['babangida', 'sani', 'hamza', 'aliyu']
print(len(students))
print(max(students))
print(min(students))
print(sorted(students))

students.append('abubakar')
students[-1] = 'sadik'
print('\n'.join(students))

#print('tuple')

angkorwat = (13.41233, 102.688887)

print(type(angkorwat))

print("angkorwat is at latitude: {}".format(angkorwat[0]))
print("angkorwat is at longitude: {}".format(angkorwat[1]))

print("\n Tuple ia another container that store related pieces of information \n its data type of immutable orderred sequence")

print("latitude", angkorwat[0])
print("longitude", angkorwat[1])

print("\n")

dimensions = 40, 57, 53
print(type(dimensions))
length, height, width = dimensions
#print("The dimensions are {} x {} x {}".format(length, width, height))
print("The dimensions are {} * {} * {}".format(length, height, width))

print("\n")

length, height, width = 11, 43, 87
print("The dimensions are {} * {} * {}".format(length, height, width))

#Set is a data type for mutable unorderred collection of unique elements. 

country = {'nigeria', 'niger', 'south africa', 'ghana', 'algeria', 'marocco'}
country.add('babangida')
country.pop()
uniq = set(country)
print(uniq)
numbers = [1, 3, 1, 4, 4, 1, 2, 1]
print(numbers[2:])
