# Day 14 - Higher Order Functions | Exercises: Level 1

# Given data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Explain the difference between map, filter, and reduce.

"""
map as the definition of the word is essentially mapping the chosen function to every 
iterable in the list. It is essentially a for loop where every iterable will go through
the function

filter as the definition of the word is essentially filtering the list based on the 
function. The function return value is boolean. It is essentailly a for loop where the iterable 
will be passed through the function as only those that return True will be kept in the list

reduce is essentially reducing the iterables in the list in to one value as defined by the
function. For example if its the summation function, reduce in-built funciton takes all the
iterables and add them up into a single value, being the sum of all the numbers in the list
"""

# REVIEW: right idea, wrong word. The LIST is the iterable; its members are
# "items" / "elements". Swap "iterable" -> "item" everywhere above.
# Also missing: in Python 3 map and filter are LAZY - they return iterators,
# not lists, so you must wrap them in list() to see anything. reduce is the
# exception: it returns a single value immediately.
#
# MODEL ANSWER:
# map(func, iterable)    -> iterator, applies func to every item. Same length in/out.
# filter(func, iterable) -> iterator, keeps only the items where func(item) is truthy.
#                           Length shrinks (or stays the same); items are unchanged.
# reduce(func, iterable) -> ONE value. func takes two args (accumulator, item) and
#                           folds the list down pairwise. Lives in functools.
#
# numbers = [1, 2, 3, 4]
# list(map(lambda n: n * n, numbers))       # [1, 4, 9, 16]   - transform
# list(filter(lambda n: n % 2 == 0, numbers))  # [2, 4]        - select
# reduce(lambda a, b: a + b, numbers)       # 10               - collapse

# 2. Explain the difference between higher order function, closure and decorator

"""
The definition of higher order function is a function that does at least one of 2 things: 
- it takes one or more function as arguments
- it returns a function as its output

So based on this definiton, a decorator is strictly a higher order function meeting the definition
of a higher order function as it takes one or more function as arguments 

Whereas closure may not necessarily be a higher order function as it is just a state-preservation 
mechanism. There are examples where a function may not take in one or more function as argument
but the nested function can still exhibit closure mechanism
"""

# REVIEW: correct on all three. Nothing to change.
#
# MODEL ANSWER (same points, plus the code that shows each):
# Higher order function - takes a function as an argument, and/or returns a function.
#     map, filter, reduce, sorted(key=...) are all higher order functions.
# Closure   - an inner function that REMEMBERS variables from the enclosing scope
#             after the outer function has already returned. It is about captured
#             state, not about taking functions as arguments.
# Decorator - a specific higher order function: takes a function, returns a
#             replacement function. Usually implemented WITH a closure (the wrapper
#             captures the original func), which is why the three get conflated.
#
# def make_counter():          # closure - no function passed in, so not a HOF
#     count = 0
#     def increment():
#         nonlocal count       # 'count' survives because increment closed over it
#         count += 1
#         return count
#     return increment         # ...though returning a function DOES make it a HOF
#
# def shout(func):             # decorator = HOF + closure
#     def wrapper(*args):
#         return func(*args).upper()
#     return wrapper
#
# @shout
# def greet(name):
#     return f'hello {name}'
# print(greet('asabeneh'))     # HELLO ASABENEH

# 3. Define a call function before map, filter or reduce, see examples.
from functools import reduce

def call(type, function, arr):
    if type == "map":
        return map(function, arr)
    elif type == "filter":
        return filter(function, arr)
    elif type == "reduce":
        return reduce(function, arr)

# REVIEW: this is a valid higher order function, but it answers a different
# question. In the chapter's wording "call function" means CALLBACK - the point
# is to define and NAME the callback before handing it to map/filter/reduce,
# instead of inlining a lambda (see 14_higher_order_functions.md, Example 3).
# Also: `type` shadows the builtin type() - rename it to `kind` if you keep this.
#
# MODEL ANSWER:
# def change_to_upper(name):          # named callback, defined BEFORE map
#     return name.upper()
#
# def is_even(num):                   # named callback, defined BEFORE filter
#     return num % 2 == 0
#
# def add_two_nums(x, y):             # named callback, defined BEFORE reduce
#     return x + y
#
# print(list(map(change_to_upper, names)))    # ['ASABENEH', 'LIDIYA', ...]
# print(list(filter(is_even, numbers)))       # [2, 4, 6, 8, 10]
# print(reduce(add_two_nums, numbers))        # 55

# 4. Use for loop to print each country in the countries list.

def print_countries(arr):
    for country in arr:
        print(country)

print_countries(countries)

# 5. Use for to print each name in the names list.

def print_names(arr):
    for name in arr:
        print(name)

print_names(names)

# 6. Use for to print each number in the numbers list.

def print_numbers(arr):
    for number in arr:
        print(number)

print_numbers(numbers)

# REVIEW (4-6): all three work, but you wrote three near-identical wrappers for
# something the exercise asked as a bare loop. Wrapping in a function only pays
# off when you call it more than once - here each is called exactly once.
#
# MODEL ANSWER:
# for country in countries:
#     print(country)
#
# for name in names:
#     print(name)
#
# for number in numbers:
#     print(number)
