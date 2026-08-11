# Day 13

## List Comprehension

Compact way of creating a list from a sequence. 
- List comprehension is considerably faster than processing a list using the for loop

```python
# syntax
[expression for i in iterable if condition]

#Example1
language = 'Python'
lst = [i for i in language]

# Example2 
even_numbers = [i for i in range(11) if i % 2 == 0] # generate even numbers list
numbers = [(i,i*i) for i in range(11)] # making a list of tuples
```

## Lambda Function

A small anonymous function without a name
- Take any number of arguments but can only have one expression 

### Creating a lambda function

`lambda`: use to create a lambda function.
- Lambda function does not use return but it explicitly returns the expression
```python
x = lambda param1,param2,param3: param1 + param2 + param3

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Lambda Function inside another function

```python
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```
