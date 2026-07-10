# Day 10

## Loops

2 types of loop: 
    - while loop
    - for loop

### While loop

Used to execute a block of statements repeatedly until given condition is satisfied

When condition becomes false, lines of code after the loop will continue to execute

```python
while condition:
    code goes here
```

### For loop

Loop is used for iterating over a sequence.

- Using `For` loop on list
```python
for iterator in lst:
    code goes here
```

- Using `For` loop on string
```python
for iterator in string:
    code goes here
```

- Using `For` loop on tuple
```python
for iterator in tpl:
    code goes here
```

- Using `For` loop on dict gives you key of dict
```python
for iterator in dct:
    code goes here

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

- Using `For` loop on dict gives you key of dict
```python
for iterator in st:
    code goes here
```

#### The Range Function

`range()`: return a list of numbers
    - range(start,end,step)
    - By default starts from 0 and increment 1
    - arnge needs at least 1 argument (end)

```python
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for iterator in range(start, end, step):
```

#### Nested For Loop 

Writing loops inside a loop

```python
for x in y:
    for t in x:
        print(t)
```

#### For Else

Execute some message when loop ends, we use else
```python
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

#### Pass

In python when statement is required (after semicolon), but we dont like to execute any code, we can write word pass to avoid errors
    - use it as placeholder for future statements
```python
for number in range(6):
    pass
```

### Break and Continue

`Break`: We use break when we like to get out of or stop the loop

```python
while condition:
    code goes here
    if another_condition:
        break

for number in numbers:
    print(number)
    if number == 3:
        break
```

`Continue`: Skip the current iteration and continue with the next

```python
while condition:
    code goes here
    if another_condition:
        continue

for iterator in sequence:
    code goes here
    if condition:
        continue
```

## Additional cheatsheet

Sorting dictionary based on values making use of the key argument of `sorted()`
```python
sorted(population_list, key= lambda kv:kv[1], reverse=True)
```