# Day 9 - Conditionals | Exercises: Level 2

# 1. Write a code which gives grade to students according to their scores:
#    90-100, A
#    80-89, B
#    70-79, C
#    60-69, D
#    0-59, F
def grade_assignment():
    score = int(input("What is your score: "))
    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    elif score >= 0 and score <= 59:
        print("F")
    else: 
        print("Please input a valid score")

# 2. Get the month from user input then check if the season is Autumn, Winter,
#    Spring or Summer. If the user input is:
#    September, October or November, the season is Autumn.
#    December, January or February, the season is Winter.
#    March, April or May, the season is Spring.
#    June, July or August, the season is Summer.
def season_checker():
    month = input("Enter the current month: ")
    spring = ["march", "april", "may"]
    summer = ["june", "july","august"]
    autumn = ["september", "october", "november"]
    winter = ["december","january","february"]
    if month.lower() in spring:
        print("The season is Spring")
    elif month.lower() in summer:
        print("The season is Summer")
    elif month.lower() in autumn:
        print("The season is Autumn")
    elif month.lower() in winter:
        print("The season is Winter")
    else:
        print("Enter a valid month")
    

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
#    If a fruit doesn't exist in the list add the fruit to the list and print the
#    modified list. If the fruit exists print('That fruit already exist in the list')
def if_fruits_exist(fruits: list):
    fruit = input("Enter fruit: ")
    if fruit in fruits:
        print("That fruit already exist in the list")
    else: 
        fruits.append(fruit)
        print(fruits)

#grade_assignment()
#season_checker()
#if_fruits_exist(fruits)