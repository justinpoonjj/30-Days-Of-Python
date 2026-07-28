# Day 11 

## Functions

A function is a resuable block of code or programming statements desgined to perform a certain task. 

`def`: To define or declare a function

## Declaring and Calling a Function

We make a function by declaring a function 

We call a function by invoking/calling a function

Functions can be declared with/without parameters

```python
# Declaring a function
def function_name():
    codes
    codes

# Calling a function
function_name()
```

## Function Returning a Value

`return`: used to help functions return values 
- returns `None` if function has no return statement

```python
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
```

We can return any data types
```python
# Return String
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

# Return Integer
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

# Return Boolean
def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

# Return List
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

## Function with Parameters

We can pass different data types as parameters.

- Single Parameter: 
    - If function takes a parameters it should be called with an argument
```python
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
```

- Multiple Parameter:
    - If function takes parameters, it should be called with arguments 
```python
# Declaring a function
def function_name(para1, para2):
codes
codes
# Calling function
print(function_name(arg1, arg2))
```

- Passing Arguments with Key and Value:
    - the order of arguments does not matter.
```python
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
```

## Function with Default Parameters

We pass default values to parameters when invoking the function.
- If we do not pass the arguments when calling the function, their default values will be used.

```python
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

## Arbitrary Number of Arguments

We can create a function which can take arbitrary number of arguments by adding * before the parameter name

```python
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

## Default and Arbitrary Number of Parameters in Functions
```python
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

## Dictionary unpacking

You can call a function which has named arguments using a dictionary with matching key names
- Do so using `**`

```python
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York
```

## Arbitrary Number of Named Arguments (Avoid this to prevent ambiguity)

Define a function to accept an arbitrary number of named arguments

```python
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

## Function as a Parameter of Another Function

```python
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```
