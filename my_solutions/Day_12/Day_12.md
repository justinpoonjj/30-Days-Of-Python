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
