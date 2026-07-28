# Day 11 - Functions | Exercises: Level 1
from math import sqrt

PI = 3.14

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    return a + b

# 2. Area of a circle is calculated as follows: area = π x r x r.
#    Write a function that calculates area_of_circle.

def area_of_circle(r):
    area = PI * r * r
    return area

# 3. Write a function called add_all_nums which takes arbitrary number of
#    arguments and sums all the arguments. Check if all the list items are
#    number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) != int:
            return "list are not number types"
        sum += num
    return sum
# WRONG: `type(num) != int` rejects valid floats (e.g. add_all_nums(1.5) fails).
# Better: use isinstance and allow both int and float:
#     if not isinstance(num, (int, float)):
#         return "All arguments must be numbers"
# isinstance also handles subclasses; type() does not.

# print(add_all_nums(1,2,3,4))

# 4. Temperature in °C can be converted to °F using this formula:
#    °F = (°C x 9/5) + 32. Write a function which converts °C to °F,
#    convert_celsius_to_fahrenheit.

def convert_celsius_to_fahrenheit(temp_deg):
    temp_f = (temp_deg * (9/5)) + 32
    return temp_f

# 5. Write a function called check_season, it takes a month parameter and
#    returns the season: Autumn, Winter, Spring or Summer.

def check_season(month: str):
    spring = ["march", "april", "may"]
    summer = ["june", "july", "august"]
    autumn = ["september", "october", "november"]
    winter = ["december", "january", "february"]

    if month.lower() in spring:
        return "Spring"
    if month.lower() in summer:
        return "Summer"
    if month.lower() in autumn:
        return "Autumn"
    if month.lower() in winter:
        return "Winter"
    return "Enter valid month"

# print(check_season("july"))

# 6. Write a function called calculate_slope which return the slope of a
#    linear equation.

def calculate_slope(point1: tuple, point2:tuple):
    slope = (point2[0] - point1[0]) / (point2[1] - point1[1])
    return slope
# WRONG: slope is rise/run = (y2 - y1) / (x2 - x1), but this computes
# (x2 - x1) / (y2 - y1) — the reciprocal. Points are (x, y), so index 1 is y.
# Correct:
#     slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
# print(calculate_slope((1,1),(2,2)))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
#    Write a function which calculates solution set of a quadratic equation,
#    solve_quadratic_eqn.

def sol_quadratic(a,b,c):
    eqn_1 = -b/(2*a) 
    eqn_2 = sqrt(b*b - 4*a*c) / (2 * a)
    x1 = eqn_1 + eqn_2
    x2 = eqn_1 - eqn_2
    return x1, x2

# print(sol_quadratic(1/2, -3,5/2))

# 8. Declare a function named print_list. It takes a list as a parameter and
#    it prints out each element of the list.

def print_list(arr: list):
    for ele in arr:
        print(ele)

# print_list(list)

# 9. Declare a function named reverse_list. It takes an array as a parameter
#    and it returns the reverse of the array (use loops).
#    print(reverse_list([1, 2, 3, 4, 5]))
#    # [5, 4, 3, 2, 1]
#    print(reverse_list(["A", "B", "C"]))
#    # ["C", "B", "A"]

def reverse_list(arr):
    res = []
    for i in range(len(arr) - 1, -1, -1):
        res.append(arr[i])
    print(res)
# WRONG: exercise says "returns the reverse" — this prints instead of returning,
# so it gives None back. The expected `print(reverse_list([1,2,3]))` won't work.
# Fix: replace `print(res)` with `return res`.

# reverse_list([1,2,3,4,5])

# 10. Declare a function named capitalize_list_items. It takes a list as a
#     parameter and it returns a capitalized list of items.

def capitalize_list_items(items: list):
    res = []
    for item in items:
        res.append(item.capitalize())
    return res

# arr = ["potato","tomato"]
# print(capitalize_list_items(arr))

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

# 11. Declare a function named add_item. It takes a list and an item parameters.
#     It returns a list with the item added at the end.
#     food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     print(add_item(food_stuff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
#     numbers = [2, 3, 7, 9]
#     print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]

def add_item(arr, item):
    arr.append(item)
    return arr

# print(add_item(food_stuff, 'Meat'))

# 12. Declare a function named remove_item. It takes a list and an item parameters.
#     It returns a list with the item removed from it.
#     food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
#     print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
#     numbers = [2, 3, 7, 9]
#     print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(arr:list, item):
    if item in arr:
        arr.remove(item)
    else:
        print("item not inside")

    return arr

# print(remove_item(food_stuff,'Mango'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and
#     it adds all the numbers in that range.
#     print(sum_of_numbers(5))  # 15
#     print(sum_of_numbers(10)) # 55
#     print(sum_of_numbers(100)) # 5050

def sum_of_numbers(number):
    sum = 0
    for i in range(number+1):
        sum += i
    return sum

# print(sum_of_numbers(5))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it
#     adds all the odd numbers in that range.

def sum_of_odds(number):
    sum = 0
    for i in range(number + 1):
        if i % 2 == 1:
            sum += i
    return sum

# 15. Declare a function named sum_of_even. It takes a number parameter and it
#     adds all the even numbers in that range.
def sum_of_odds(number):
    sum = 0
    for i in range(number + 1):
        if i % 2 == 0:
            sum += i
    return sum
# WRONG: named sum_of_odds — same name as #14, so this redefines/overwrites it.
# Logic is right (sums evens) but the exercise wants `def sum_of_even(number):`.