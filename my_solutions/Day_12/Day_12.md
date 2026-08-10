# Day 12

## Modules

A module is a file containing a set of codes or a set of functions which can be included to an application. 

A module could be a file containing a single variable, a function or a big code base. 

### Creating Module

To create a module, we write our codes in a python script and save it as .py file

Create mymodule.py file with some code
```python
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

### Importing a Module

`import`: Used to import the file 

Create main.py file and import mymodule.py file
```python
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Import Functions from a Module

We have many functions in a file and import all functions differently

```python
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Import Functions from a Module and Renaming

During importing we can rename the name of the module

```python
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Built-in Modules

Import common module we use most of the time. 
- datetime
- os
- sys
- random
- statistics
- collections
- json
- re

### OS Module

Possible to automatically perform many operating system tasks

Provides functions for 
- creating
- changing current working directory
- removing a directory
- fetching contents
- changing and identifying the current directory

```python
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### Sys Module 

Provides functions and variables used to manipulate different parts of the Python runtime environment

- `sys.argv` returns a list of command line arguemnts passed to a python script
```python
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```
```txt
python script.py Asabeneh 30DaysOfPython

The result:
Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
```

```python
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

### Statistics Module

Provides functions for mathematical statistics of numeric data. 

The popular statistical functions defined in this module: 
```python
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Math Module

Module containing many mathematical operations and constants
```python
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

Possible to import multiple functions
```python
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
```

Import all the function we can use `*`
```python
from math import *
```

When importing we can rename the function
```python
from math import pi as PI
```

### String Module

Example shows some use of the string module
```python
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random Module

Some example of random module

```python
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```