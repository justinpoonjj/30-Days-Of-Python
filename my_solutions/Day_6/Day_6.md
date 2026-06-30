# Day 6

## Tuples 

A tuple is a collection of different data types 
    - ordered
    - unchangable (immutable)

Tuples are written with round brackets ()

Once a tuple is created, we cannot change its value
    - cannot use add, insert, remove methods in a tuple because it is not modifiable. 

### Methods

`tuple()`: to create an empty tuple
`count()`: to count the number of specified item in a tuple
`index()`: to find the index of a specified item in a tuple
`+ operator`: to join 2 or more tuple and to create a new tuple

### Creating a Tuple

Empty tuple: 
```python
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
```

Tuple with initial values: 
```python
# syntax
tpl = ('item1', 'item2','item3')
```

### Tuple length

`len()`: Length of a tuple
```python
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Accessing Tuple Items

Positive Indexing: Simliar to list
```python
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```

Negative Indexing: SImilar to list
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```

### Slicing tuples

Slicing out a sub-tuple by specifying a range of indexes 

Range of positive indexes
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
```

Range of negative indexes
```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
```

### Changing tuples to lists

Tuple is immutable if we want to modify a tuple we should change it to a list

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

### Checking an item in a Tuple

Checking if an item exists using `in` -> returns a boolean

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

### Joining Tuples 

Join 2 or more tuples using + operator
```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

### Deleting tuples

delete the tuple itself using del
```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```
