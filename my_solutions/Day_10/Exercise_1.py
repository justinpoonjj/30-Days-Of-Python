# Day 10 - Loops | Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.

def iterate_for_loop():
    for i in range(11):
        print(i, end=" ")
    print("")

def iterate_while_loop():
    i = 0
    while i < 11:
        print(i, end=" ")
        i += 1
    print("")


# 2. Iterate 10 to 0 using for loop, do the same using while loop.

def iterate_for_loop_rev():
    for i in range(10,-1,-1):
        print(i, end=" ")
    print("")

def iterate_while_loop_rev():
    i = 10
    while i > -1:
        print(i,end = " ")
        i -= 1
    print("")

# 3. Write a loop that makes seven calls to print(), so we get on the output
#    the following triangle:
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
def print_right_triangle(n: int):
    for i in range(1, n+1):
        print('#' * i)

# 4. Use nested loops to create the following:
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
def print_square(n: int):
    for row in range(n):
        for col in range(n):
            print("#", end=" ")
        print("") 


# 5. Print the following pattern:
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
def print_pattern(n: int):
    for i in range(n + 1):
        print(f"{i} x {i} = {i*i}")


# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask']
#    using a for loop and print out the items.

def print_items_in_list():
    lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
    for items in lst:
        print(items, end=" ")
    print()

# 7. Use for loop to iterate from 0 to 100 and print only even numbers.
def print_only_even():
    for i in range(101):
        if i % 2 == 0:
            print(i, end=" ")

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers.
def print_only_odd():
    for i in range(101):
        if i % 2 == 1:
            print(i, end=" ")

# iterate_for_loop()
# iterate_while_loop()
# iterate_for_loop_rev()
# iterate_while_loop_rev()
# print_right_triangle(7)
# print_square(8)
# print_pattern(10)
# print_items_in_list()
# print_only_even()
# print_only_odd()