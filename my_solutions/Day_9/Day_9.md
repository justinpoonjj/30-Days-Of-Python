# Day 9

## Conditionals

By defualt, Python script are executed sequentially from top to bottom. 

If processing logic require so, the sequential flow of execution can be altered in 2 ways:
    - Conditional execution
    - Repetive execution

### If Condition

`if`: used to check if a condition is true and execute the block code
```python
if condition:
    this part of code runs for truthy conditions
```

### If Else

`if-else`: 
    - if condition true first block will be executed
    - if not the else condition runs
```python
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

### If Elif Else

`if-elif-else`: use it when we have multiple condition
```python
if condition:
    code
elif condition:
    code
else:
    code
```

### Short Hand

```python
code if condition else code
```

### Nested Conditions

Conditions can be nested
```python
if condition:
    code
    if condition:
    code
```

### If Condition and Logical Operators
```python
if condition and condition:
    code
```

### If and Or Logical Operators 
```python
if condition or condition:
    code
```