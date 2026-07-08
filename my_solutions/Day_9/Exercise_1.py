# Day 9 - Conditionals | Exercises: Level 1

# 1. Get user input using input("Enter your age: "). If user is 18 or older, give
#    feedback: "You are old enough to learn to drive." If below 18 give feedback to
#    wait for the missing amount of years.
#    Output:
#    Enter your age: 30
#    You are old enough to learn to drive.
#    Enter your age: 15
#    You need 3 more years to learn to drive.
def elibility_to_drive():
    age = int(input("Enter you age: "))
    if age >= 18: 
        print("You are old enough to learn to drive.")
    else: 
        print(f"You need {18 - age} more years to learn to drive")


# 2. Compare the values of my_age and your_age using if ... else. Who is older
#    (me or you)? Use input("Enter your age: ") to get the age as input. You can use
#    a nested condition to print 'year' for 1 year difference in age, 'years' for
#    bigger differences, and a custom text if my_age = your_age.
#    Output:
#    Enter your age: 30
#    You are 5 years older than me.
def comparing_age():
    age = int(input("Enter your age: "))
    my_age = 23
    diff = abs(age - my_age)
    if age > my_age:
        if diff == 1:
            print("You are 1 year older than me")
        else:
            print(f"You are {diff} years older than me")
    elif age == my_age:
        print(f"You are the same age as me")
    else: 
        if diff == 1:
            print("You are 1 year younger than me")
        else: 
            print(f"You are {diff} years younger than me")
    


# 3. Get two numbers from the user using input prompt. If a is greater than b return
#    "a is greater than b", if a is less than b return "a is smaller than b", else
#    "a is equal to b".
#    Output:
#    Enter number one: 4
#    Enter number two: 3
#    4 is greater than 3
def comparing_numbers():
    num_1 = int(input("Enter number one: "))
    num_2 = int(input("Enter number two: "))
    if num_1 > num_2:
        print(f"{num_1} is greater than {num_2}")
    elif num_1 == num_2:
        print(f"{num_1} is equal to {num_2}")
    else:
        print(f"{num_1} is smaller than {num_2}")

#elibility_to_drive()
#comparing_age()
#comparing_numbers()