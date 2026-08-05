# Day 11 - Functions | Exercises: Level 2

from math import sqrt

# 1. Declare a function named evens_and_odds. It takes a positive integer as
#    parameter and it counts number of evens and odds in the number.
#    print(evens_and_odds(100))
#    # The number of odds are 50.
#    # The number of evens are 51.

def evens_and_odds(num):
    even = 0
    odd = 0
    for i in range(num + 1):
        if i % 2 == 0: 
            even += 1
        if i % 2 == 1: 
            odd += 1
    return f"""
The number of odds are {odd}
The number of evens are {even}"""

# print(evens_and_odds(100))

# 2. Call your function factorial, it takes a whole number as a parameter and
#    it return a factorial of the number.

def factorial(num):
    res = 1
    for i in range(1,num + 1):
        res *= i
    return res

# print(factorial(4))

# 3. Call your function is_empty, it takes a parameter and it checks if it is
#    empty or not.

def is_empty(input):
    if input is None:
        return True
    return False

def correct_is_empty(input):
    return not input
# WRONG: only catches None. "" , [], {}, () and 0 are all "empty" but return False.
# Python already treats them as falsy, so the whole body is one line:
#     return not value
# Also: `input` shadows the builtin input() — rename the parameter.

# 4. Write different functions which take lists. They should calculate_mean,
#    calculate_median, calculate_mode, calculate_range, calculate_variance,
#    calculate_std (standard deviation).

numbers= [1,2,3,4,4,3,2,1,2,3,4,1,2,3,4,5]

def caluculate_mean(nums: list):
    sum = 0
    for num in nums:
        sum += num
    mean = sum / len(nums)
    return mean
# Logic correct. Two nits: name is misspelled (caluculate -> calculate), and
# `sum` shadows the builtin sum() inside the function. Rename to total.

def caluculate_median(nums: list):
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        median = (nums[mid-1] + nums[mid]) / 2
        return median
    return nums[mid]
# WRONG, two separate bugs:
# 1. The list is never sorted. Median is defined on sorted data. With the given
#    `numbers` this returns 1.5 instead of the correct 3.0.
# 2. The odd-length branch returns `mid + 1` — that's an index, not a value.
#    It should return the element at that index.
# Fix:
#     nums = sorted(nums)          # sorted() copies, so the caller's list is safe
#     mid = len(nums) // 2
#     if len(nums) % 2 == 0:
#         return (nums[mid-1] + nums[mid]) / 2
#     return nums[mid]

def calculate_mode(nums: list):
    dict_nums = {}
    for num in nums:
        if num in dict_nums:
            dict_nums[num] += 1
        else:
            dict_nums[num] = 1

    list_modes = []
    max = -1
    for num in dict_nums:
        if dict_nums[num] > max:
            list_modes.clear()
            list_modes.append(num)
            max = dict_nums[num]
        elif dict_nums[num] == max:
            list_modes.append(num)
    print(list_modes)
    return list_modes
# Correct — the "reset the list when a new max appears" pattern handles ties
# properly. Two nits: `max` shadows the builtin, and the print() is debug output
# left in a function that already returns the value. Drop the print.

def calculate_range(nums: list):
    min = nums[0]
    max = nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    return max - min
# WRONG: .pop(0) MUTATES the caller's list — it permanently deletes the first two
# elements. This is why the print block below is misleading: after
# calculate_range(numbers) runs, `numbers` has 14 items instead of 16, so the
# variance/std printed afterwards are computed on a damaged list.
# It also crashes on a list with fewer than 2 items.
# Fix: read, don't pop.
#     lo = hi = nums[0]
#     for num in nums:
#         if num < lo: lo = num
#         if num > hi: hi = num
#     return hi - lo

def calculate_variance(nums: list):
    mean = caluculate_mean(nums)
    sum_squares = 0
    for num in nums:
        sum_squares += (num - mean) ** 2
    var = sum_squares / len(nums)
    return var

def calculate_std(nums: list):
    var = calculate_variance(nums)
    return sqrt(var)
# Both correct. Note this is POPULATION variance (divide by n). Sample variance
# divides by n - 1. Either is a fine answer here, just know which one you wrote.
# Reusing calculate_variance inside calculate_std is the right call.

# print(caluculate_mean(numbers))
# print(caluculate_median(numbers))
# calculate_mode(numbers)
# print(calculate_range(numbers))
# print(calculate_variance(numbers))
# print(calculate_std(numbers))
# NOTE: this call order is a trap — calculate_range(numbers) pops 2 items off
# `numbers`, so variance/std below run on a 14-item list. Fix calculate_range
# and the ordering stops mattering.

# 5. Write a function called greet which takes a default argument, name.
#    If no argument is supplied it should print "Hello, Guest!", otherwise it
#    should greet the person by name.
#    greet()
#    # "Hello, Guest!"
#    greet("Alice")
#    # "Hello, Alice!"

def greet(*name):
    if not name:
        print("Hello, Guest!")
        return
    print(f"Hello, {name[0]}!")
    return

def correct_greet(name="Guest"):
    print(f"Hello, {name}")
    return

# `*arg` is being stored as a tuple, you would have to index it to avoid the awkwardness in formatting
# Output is right, but this doesn't answer the exercise: it asked for a DEFAULT
# ARGUMENT, which is the whole point of the question. *args is a workaround for
# the feature being practised. What was asked:
#     def greet(name="Guest"):
#         print(f"Hello, {name}!")
# One line, no tuple, no indexing, no branch. That's what defaults buy you.
    
# greet()
# greet("Alice")    

# 6. Create a function called show_args to take an arbitrary number of named
#    arguments and print their names and values.
#    show_args(name="Alice", age=30, city="New York")
#    # Received: name: Alice, age: 30, city: New York
#    show_args(name="Bob", pet="Fluffy, the bunny")
#    # Received: name: Bob, pet: Fluffy, the bunny

def show_args(**kwargs):
    string = "Received: "
    for key in kwargs:
        string += f"{key}: {kwargs[key]}, "
    print(string)
    return
# Close, but leaves a trailing comma: "Received: name: Alice, age: 30, city: New York,"
# Joining is the fix for "separator between items, not after the last one":
#     print("Received: " + ", ".join(f"{k}: {v}" for k, v in kwargs.items()))
# Also .items() beats indexing kwargs[key] inside the loop.

# show_args(name="Alice", age=30, city="New York")