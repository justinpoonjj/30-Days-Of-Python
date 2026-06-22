import os
import sys
import subprocess
from math import sqrt

def check_python_version() -> str:
    command = [sys.executable, "--version"]
    result = subprocess.run(command, capture_output=True,text = True)
    return result.stdout

def addition(a: int, b: int) -> int:
    return a + b 

def subtraction(a: int, b: int) -> int:
    return a - b

def multiplication(a: int, b: int) -> int:
    return a * b

def modulus(a: int, b: int) -> int:
    return a % b

def division(a: int, b: int) -> int:
    return a / b

def exponential(a: int, b: int) -> int:
    return a ** b

def floor_division_operator(a: int, b: int) -> int:
    return a // b

def answer_question_3() -> None:
    print("Justin")
    print("Poon")
    print("Singapore")
    print("I am enjoying 30 days of python")



def elucidianDistance(point_1: tuple, point_2: tuple) -> int:
    x_diff = point_1[0] - point_2[0]
    y_diff = point_1[1] - point_2[1]
    res_sq = exponential(x_diff,2) + exponential(y_diff,2)
    return sqrt(res_sq)

def main(a: int, b: int) -> int:
    print("Question 2.1: ")
    print(check_python_version())

    print("Question 2.2: ")
    print(addition(a,b))
    print(subtraction(a,b))
    print(multiplication(a,b))
    print(modulus(a,b))
    print(division(a,b))
    print(division(a,b))
    print(exponential(a,b))
    print(floor_division_operator(a,b), "\n")

    print("Question 2.3: ")
    answer_question_3()
    print("\n")

    print("Question 2.4: ")
    print(type(10))
    print(type(9.8))
    print(type(3.14))
    print(type(4 -4j))
    print(type(['Asabeneh', 'Python', 'Finland']))
    print(type("Justin"), "\n")

    print("Question 3.1: ")
    print(type(3))
    print(type(1.2))
    print(type(2 +8j))
    print(type("Hello"))
    print(type(True))
    print(type([1,2,3]))
    print(type((1,2,3)))
    print(type({"1","2"}))
    print(type({"key":"value"}), "\n")

    print("Question 3.2")
    print(elucidianDistance((2,3),(10,8)))




main(3,4)