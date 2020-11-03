# A lambda function is a small one-liner anonymous function., without def and return statements

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:


x = lambda a: a + 10
print(x(5))  # 15

# Lambda functions can take any number of arguments:


x = lambda a, b: a * b
print(x(5, 6))  # 30

max_of_2 = lambda a, b: a if a > b else b
print(max_of_2(5, 6))  # 6


# Why Use Lambda Functions? goal is to make it short
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:

# Use that function definition to make a function that always doubles the number you send in:

# Example
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)  # becomes mydoubler= lambda a: a * 2 (same as x=lambda a:a*n)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))

# 22
# 33


# maps

# if there a list /sequence and a function,
# if we want to apply the function to each item in the list and return a new list, then we can use map() function

# list(map(func,list))

list1 = [1, 2, 3, 4, 5]

sq_list = list(map(lambda x: x ** 2, list1))
print(sq_list)  # [1, 4, 9, 16, 25]


# map function iterates through our list and passes each element into lambda function
# and then rhe return value is cast as list and printed


# alternatively we can use normal def function in place of lambda 2) use list comprehensions

def square(num):
    return num ** 2


sq_list2 = list(map(square, list1))
print(sq_list2)
# [1, 4, 9, 16, 25]


# filters
# consider function as a black box , if we pass an list and a condition ,
# we will get a list with all the items having that condition passed

list1 = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x > 2, list1)))
# can be done using list comprehension ,

# remove -ve weights and and get a lis with all positive weights
list1 = [1, 2,-9,-8, 3, 4, 5]
print(list(filter(lambda x: x > 0, list1)))
# [1, 2, 3, 4, 5]


