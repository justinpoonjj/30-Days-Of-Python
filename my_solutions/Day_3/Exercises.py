from math import sqrt

#Declare your age as integer variable
age: int = 23

#Declare your height as a float variable
height: float = 165.0

#Declare a variable that store a complex number
x: complex = 1 - 2j

# Write a script that prompts the user to enter base and height 
# of the triangle and calculate an area of this triangle 
# (area = 0.5 x b x h).
base: float = float(input("Enter base: "))
height: float = float(input("Enter height: "))
area: float = 0.5 * base * height
print(f"The are of the triangle is {area}")

# Write a script that prompts the user to enter side a, side b, and side c 
# of the triangle. Calculate the perimeter of the triangle 
# (perimeter = a + b + c).
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width) 
print(f"The perimeter of the rectangle is {perimeter}")

# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and 
# circumference (c = 2 x pi x r) where pi = 3.14.
PI = 3.14
radius = float (input("Enter radius: "))
area = PI * (radius ** 2)
circumference = 2 * PI * radius
print(f"Area of circle: {area}\nCircumference of circle: {circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# When y = 0, 2x = 2 -> x = 1
# When x = 0, y = -2  
slope_task8 = 2
x_intercept = 2 / 2
y_intercept = -2 
print(f"Slope: {slope_task8}")

# Slope is (m = y2-y1/x2-x1). 
# Find the slope and 
# Euclidean distance between point (2, 2) and point (6,10)
point_1 = (2,2)
point_2 = (6,10)
diff_y = point_2[1]-point_1[1]
diff_x = point_2[0]-point_1[0]
slope_task9 = diff_y / diff_x
Euclidean_dist = sqrt((diff_y * diff_y) - (diff_x*diff_x))
print(f"Slope: {slope_task9}\nEuclidean_dist: {Euclidean_dist}")

# Compare the slopes in tasks 8 and 9.
Equal = slope_task8 == slope_task9
print(f"Are slope from task8 and task 9 equal?: {Equal}")

# Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and 
# figure out at what x value y is going to be 0.
x = 0
y = x**2 + 6*x + 9
while y != 0:
    x -= 1
    y = x**2 + 6*x + 9
print(f"x = {x}") # final answer: x = -3

# Find the length of 'python' and 'dragon' and 
# make a falsy comparison statement.
length_python = len("python")
length_dragon = len("dragon")
compare = length_python > length_dragon
print(f"Falsy statement: {compare}")

# I hope this course is not full of jargon. 
# Use in operator to check if jargon is in the sentence.
if "jargon" in "I hope this course is not full of jargon. ":
    print(True)
else:
    print(False)

# There is no 'on' in both dragon and python
if "on" not in "dragon" and "python":
    print(True)
else:
    print(False)

# Find the length of the text python and 
# convert the value to float and convert it to string
length_python = len("python")
length_python_float = float(length_python)
length_python_string = str(length_python)
print(f"Float: {length_python_float}\nString: {length_python_string}")

# Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
number = int(input("Number: "))
if number % 2 == 0:
    print("Number is even")
else: 
    print("Number is odd")

# Check if the floor division of 7 by 3 is equal to the int 
# converted value of 2.7.
if 7//3 == int(2.7): 
    print("floor division of 7 by 3 is equal to the int converted value of 2.7")
else: 
    print("floor division of 7 by 3 is not equal to the int converted value of 2.7")
print(f"floor div: {7//3}, int converted: {int(2.7)}")

# Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("type of '10' is equal to type of 10")
else: 
    print("type of '10' is not equal to type of 10")
print(f"type of '10': {type('10')}, type of 10: {type(10)}")

# Check if int('9.8') is equal to 10
if int(9.8) == 10:
    print("int('9.8') is equal to 10")
else: 
    print("int('9.8') is not equal to 10")
print(f"int(9.8): {int(9.8)}")

# Write a script that prompts the user to enter hours and rate per hour. 
# Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. 
# Assume a person can live hundred years
years_lived = float(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
max_range = int(input("Number: "))
for i in range(1,max_range + 1):
    print(i, end=" ")
    for j in range(0, max_range - 1):
        print(i**j, end=" ")
    print()