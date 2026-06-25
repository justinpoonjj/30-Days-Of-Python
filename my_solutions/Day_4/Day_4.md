# Day 4

## Strings

Text is a string data type.
Any data type written as text is a string
Many string methods and built-in functions to deal with string data types

### Creating a string
- A string can be a single character or a bunch of texts
```python
letter = 'P'
```
- String could be made using a single `''` or double `""` quote
```python
text = 'Hello' 
text = "Hello"
```
- Multiline string is created by using triple single `'''` or triple double `""""""` quotes. 
```python
multi_line = """
This is multi line
creating string of multiple lines
"""
multi_line = '''
This is multi line
creating string of multiple lines
'''
```

### String Concatenation
Merging / Connecting strings is called concatenation
    - using `+` operator to concatenate string
```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
```

### Escape Sequences in Strings
\ followed by a character is an escape sequence 
    - `\n`: new line
    - `\t`: Tab (4 spaces)
    - `\'`: Single quote
    - `\"`: Double quote

### String formatting

#### Old Style String Formatting (% Operator)
The "%" operator is used to format a set of variable enclosed in a "tuple"
    - The tuple contains normal text together with "argument specifiers"
    - tuple: a fixed size list
    - argument specifiers: special symbols like %s, %d, %f,%.<small>(number of digits)</small>f

- %s - String (or any object with a string representation, like numbers)
- %d - Integers
- %f - Floating point numbers
- "%.<small>number of digits</small>f" - Floating point numbers with fixed precision

```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
```

#### New Style String Formatting (str.format)
This format was introduced in Python version 3

```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)

a = 3
b = 4
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
```

#### String Interpolation / f-Strings (Python 3.6+)
Another string formatting is string interpolation. 
    - String start with f and we can inject data in corresponding positions
```python
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
```

## Python Strings as Sequences of Characters
Strings are sequences of characters. 
They share the same methods of access other Python ordered sequences of objects - lists and tuples

### Unpacking Characters
```python
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

### Accessing Characters in Strings by index
Counting starts from zero 
    -> first letter of string is zero index
    -> last letter of string is len(string) - 1
```python
language = 'Python'
first_letter = language[0] # P
last_index = len(language) - 1 # y
```
We can use negative indexing to start from the right
    -> -1 is last index
```python
language = 'Python'
last_letter = language[-1] # n
second_last = language[-2] # o
```

### Slicing Python Strings
We can slice strings into substrings
```python
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3

last_three = language[3:6]
# Another way
last_three = language[-3:]
last_three = language[3:]
```

### Reversing a String
```python
greeting = 'Hello, World!'
greeting[::-1]
```

### Skipping Characters while Slicing
Skip character by passing step argument to slice method.
```python
language = 'Python'
pto = language[0:6:2] #skip one char 
```

## String Methods
String methods are functions that belong to string values.

Syntax pattern:
```python
text.method(arguments)
```

Strings are immutable, so a string method returns a new value instead of changing the original string in place.

### String Methods Cheatsheet

#### Change letter case

| Method         | What it does                                            | Example                                                        |
| -------------- | ------------------------------------------------------- | -------------------------------------------------------------- |
| `capitalize()` | Makes the first character uppercase                     | `'thirty days'.capitalize()` -> `'Thirty days'`                |
| `title()`      | Makes the first letter of each word uppercase           | `'thirty days of python'.title()` -> `'Thirty Days Of Python'` |
| `swapcase()`   | Swaps uppercase to lowercase and lowercase to uppercase | `'Python'.swapcase()` -> `'pYTHON'`                            |

```python
challenge = 'thirty days of python'

print(challenge.capitalize()) # Thirty days of python
print(challenge.title())      # Thirty Days Of Python
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
```

#### Search and count text

| Method | What it does | Example |
|---|---|---|
| `count(substring)` | Counts how many times a substring appears | `'banana'.count('a')` -> `3` |
| `find(substring)` | Returns the first index of a substring, or `-1` if not found | `'python'.find('t')` -> `2` |
| `rfind(substring)` | Returns the last index of a substring, or `-1` if not found | `'happy'.rfind('p')` -> `3` |
| `index(substring)` | Like `find()`, but raises an error if not found | `'python'.index('t')` -> `2` |
| `rindex(substring)` | Like `rfind()`, but raises an error if not found | `'happy'.rindex('p')` -> `3` |
| `startswith(prefix)` | Checks if a string starts with a value | `'python'.startswith('py')` -> `True` |
| `endswith(suffix)` | Checks if a string ends with a value | `'python'.endswith('on')` -> `True` |

```python
challenge = 'thirty days of python'

print(challenge.count('y'))        # 3
print(challenge.find('days'))      # 7
print(challenge.rfind('y'))        # 16
print(challenge.index('python'))   # 15
print(challenge.startswith('th'))  # True
print(challenge.endswith('on'))    # True
```

Use `find()` when the substring might not exist. Use `index()` only when you expect it to exist.

```python
text = 'Python'

print(text.find('z'))  # -1
# print(text.index('z')) would raise ValueError
```

#### Check string content

These methods return `True` or `False`.

| Method | What it checks | Example |
|---|---|---|
| `isalnum()` | All characters are letters or numbers, with no spaces | `'Python3'.isalnum()` -> `True` |
| `isalpha()` | All characters are letters only | `'Python'.isalpha()` -> `True` |
| `isdecimal()` | All characters are decimal digits `0-9` | `'123'.isdecimal()` -> `True` |
| `isdigit()` | All characters are digits, including some Unicode digits | `'123'.isdigit()` -> `True` |
| `isnumeric()` | All characters are numeric, including more number-like Unicode characters | `'123'.isnumeric()` -> `True` |
| `isidentifier()` | The string is a valid Python variable name | `'first_name'.isidentifier()` -> `True` |
| `islower()` | All alphabetic characters are lowercase | `'python'.islower()` -> `True` |
| `isupper()` | All alphabetic characters are uppercase | `'PYTHON'.isupper()` -> `True` |

```python
print('ThirtyDaysPython'.isalnum())     # True
print('thirty days'.isalnum())          # False, space is not alphanumeric
print('Python'.isalpha())               # True
print('Python3'.isalpha())              # False
print('123'.isdecimal())                # True
print('30Days'.isdigit())               # False
print('123'.isnumeric())                # True
print('30_days'.isidentifier())         # False, starts with a number
print('thirty_days'.isidentifier())     # True
print('python'.islower())               # True
print('PYTHON'.isupper())               # True
```

#### Split, join, strip, and replace

| Method | What it does | Example |
|---|---|---|
| `split(separator)` | Breaks a string into a list | `'a,b,c'.split(',')` -> `['a', 'b', 'c']` |
| `join(iterable)` | Joins list items into one string using a separator | `', '.join(['a', 'b'])` -> `'a, b'` |
| `strip(chars)` | Removes leading and trailing spaces or characters | `'  Python  '.strip()` -> `'Python'` |
| `replace(old, new)` | Replaces one substring with another | `'I like Java'.replace('Java', 'Python')` -> `'I like Python'` |

```python
sentence = 'thirty days of python'
libraries = ['Django', 'Flask', 'Bottle']

print(sentence.split())                  # ['thirty', 'days', 'of', 'python']
print(' # '.join(libraries))             # Django # Flask # Bottle
print('   Coding For All   '.strip())    # Coding For All
print(sentence.replace('python', 'code')) # thirty days of code
```

#### Formatting and spacing

| Method | What it does | Example |
|---|---|---|
| `format()` | Inserts values into `{}` placeholders | `'{} + {} = {}'.format(2, 3, 5)` -> `'2 + 3 = 5'` |
| `expandtabs(size)` | Replaces tab characters `\t` with spaces | `'a\tb'.expandtabs(4)` -> `'a   b'` |

```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'

print('I am {} {}. I teach {}.'.format(first_name, last_name, language))
# I am Asabeneh Yetayeh. I teach Python.

print('Name\tAge\tCity'.expandtabs(10))
# Name      Age       City
```

#### Quick memory guide

| Goal | Useful methods |
|---|---|
| Change capitalization | `capitalize()`, `title()`, `swapcase()` |
| Find text position | `find()`, `rfind()`, `index()`, `rindex()` |
| Count text | `count()` |
| Check start or end | `startswith()`, `endswith()` |
| Validate content | `isalnum()`, `isalpha()`, `isdecimal()`, `isdigit()`, `isnumeric()`, `isidentifier()`, `islower()`, `isupper()` |
| Break or combine text | `split()`, `join()` |
| Clean or edit text | `strip()`, `replace()` |
| Format output | `format()`, `expandtabs()` |
