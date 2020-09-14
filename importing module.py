list_1 = ['History', 'Math', 'Physics', 'CompSci']

# import new_module
# print(new_module.find_index(list_1,'Physics'))


# import new_module as mod
# print(mod.find_index(list_1,'Physics'))


# from new_module import *
# print(find_index(list_1, 'Physics'), test)
# but difficult while debugging


from new_module import find_index, test
import sys

print(find_index(list_1, 'Physics'), test)

print(sys.path)

# importing module
# 2 Physics test string


# ['C:\\Users\\User\\Desktop\\py tutorial',
#  'C:\\Users\\User\\Desktop\\py tutorial',
#  'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip',
#  'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs',
#  'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32\\lib',
#  'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32',
#  'C:\\Users\\User\\AppData\\Roaming\\Python\\Python38\\site-packages',
#  'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']



# what if the module we are trying to import is in another dir
# then we need to add the path to sys.path
# sys.path is a list like what we have seen before
# so we can append the path

#but thats not the good way to track back if we have to change it again

# so we can go to system settings and add path envir variable












# some modules from std lib
# random

import random

print(random.choice(list_1))

# datetime , calender

import  datetime
import calendar

print(datetime.date.today())
# 2020-09-11

print(calendar.isleap(2020))
# True

# os mod

import os

print(os.getcwd())
#C:\Users\User\Desktop\py tutorial

print(os.getcwdb())
print(os.__file__) # dunder file attribute


import antigravity


