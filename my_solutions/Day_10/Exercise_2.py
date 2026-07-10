# Day 10 - Loops | Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#    Expected output:
#    The sum of all numbers is 5050.
def sum_of_all_numbers():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and
#    the sum of all odds.
#    Expected output:
#    The sum of all evens is 2550. And the sum of all odds is 2500.
def sum_of_even_and_odd():
    sum_even = 0
    sum_odd = 0
    for i in range(101):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")

sum_of_all_numbers()
sum_of_even_and_odd()