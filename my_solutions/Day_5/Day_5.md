# Day 5

## Lists

Four collection data types in python: 
    - List: ordered and changeable. Allows duplicate 
    - Tuple: ordered and unchangeable (immutable). Allows duplicate
    - Set: unordered, un-indexed and unmodifiable. Does not allow duplicate
    - Dictionary: unordered, changeable and indexed. No duplicate members

List can be empty or may have different data type items

### Create a List

- Using built in function
```python
lst = list()
```

- Using square brackets, []
```
lst = []
```

- `len()`: find the length of list
```python
lst = [1,2,3]
len(lst)
```

- List can contain different data types
```python
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
```

### Accessing List Using Positive Indexing

We access each item in a list using their index 
    - list index starts from 0

### Accessing List using Negative Indexing

Negative indexing means beginning from the end
    - -1 refers to last item
    - -2 refers to second last item

### Unpacking List Items

```python
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

### Slicing items from list

Positive index: specifying a range of positive indexes by specifying start, end and step
    - the return value will be a new list
    - defauly values for start = 0, end = len(lst) - 1, step = 1
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
```

Negative index: specfiying a range of negative indexes by specifying start, end and step
    - return value will be a new list

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
```

### Modifying Lists
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
```

### Checking Items in a list
Checking an item use in operator

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
```

### Adding Items to a List
`append()`: To add item to the end of existing list

```python
lst = list()
lst.append(item)
```

### Inserting items into a list
`insert()`: To insert a single item at specified index, note that other items are shifted to the right.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
```

### Removing Items from a List
`remove()`: removes a specified item from a list

```python
ruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
```

### Removing Item using Pop
`pop()`: removes the specified index, (or the last index if not specified)

```python
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

### Removing Items using Del
`del`: removes the specified index, or within index range, or delete list completely

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```

### Clearing List Items
`clear()`: empties the list

```python
lst = ['item1', 'item2']
lst.clear() # []
```

### Copying a List
It is possible to copy a list using assignment operator
    - lst1 = lst2
But this would mean that lst2 is a reference of lst1 (pointer of lst1 and pointer of lst2 points to the same memory space)
    - There are a lot of cases where we do not like to modify the original instead we like to have a different copy. 
    - Thus we use copy()

`copy()`: Copy a list

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### Joining Lists

`+`
```python
list3 = list1 + list2
```

`extend()`: extend method allows to append list in a list
```python
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)

print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
```

### Counting Items in a List
`count()`: returns the number of times an item appears in a list
```python
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### Finding index of an item
`index()`: returns the index of an item in the list
```python
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

### Reversing a List
`reverse()`: reverses the order of a list
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
```

### Sorting List Items
`sort()`: reorders the list in ascending order and modifies the original list.
    - if argument reverse=True -> descending order
```python
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

`sorted()`: returns the ordered list without modifying original list
```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```