# Day 14 

## Higher Order Functions

Operations that can be operated on functions: 
- A function can take one or more functions as parameter
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

In this section: 
- Handling function as parameter 
- Returning functions as return value from another function
- Using Python closures and decorators

### Function as a Parameter
```python
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

## Function as a Return Value

Higher order function is returning different dunctions depending on the passed parameter

```python
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_function(type): # higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

## Python CLosures

Python allows nested function to access the outer scope of the enclosing function
- closure is created by nesting a function inside another encapsulating function then return the inner function

```python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Python Decorators

A decorator is a design pattern in Python
- allows user to add new functionality to an existing object without modifying its structure

Decorators are usually called before the definition of a functionyou want to decorate.

### Creating Decorators

To create: we need an outer function with an inner wrapper function

```python
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator
'''This decorator is a higher order function that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())
```

### Applying Multiple Decorators to a Single Function

```python
'''These decorator functions are higher order functions that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())
```

### Accepting Parameters in Decorator Functions 

Most of the time we need our funcions to take parameters, so we might need to define a decorator that accepts parameters

```python
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1,para2,para3)
        print(f"I live in {para3}")
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach")

print_full_name("Asabeneh", "Yetayeh", "Finland")
```

## Built-in Higher Order Functions

### Python - Map Function

`map()`: built-in function that takes a function and iterable as parameters
```python
map(function, iterable)

#Example
numbers = [1,2,3,4,5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
# applying it with lambda function
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]

# Example 
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int)) 
```

### Python - Filter Function

`filter()` : calls the specified function which returns boolean for each item in iterable.
- It filters the items that satisfy teh filtering criteria
```python
filter(function, iterable)

numbers = [1,2,3,4,5]

def if_even(num):
    if num%2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers)) # [2,4]
```

### Python - Reduce Function

`reduce()` : It returns a single value
- defined in the functools module
- takes 2 parameters (function, iterable)
```python
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```