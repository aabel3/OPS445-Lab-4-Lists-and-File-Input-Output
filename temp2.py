#!/usr/bin/env python3
# OPS435 - Lab 4
# temp2.py
# Author: Avraham Abel

courses = ['uli101', 'ops235', 'ops335', 'ops435', 'ops535', 'ops635']
print(courses[0])

courses[0] = 'eac150'
print(courses[0])

print(courses)

courses.append('ops245') # Add a new item to the end of the list
print(courses)

courses.append('hwl101') # Add a new item to the specifed index location
print(courses)

courses.remove('ops635')
print(courses)
