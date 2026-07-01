# Day 7

## Sets

Set is a collection a collection of unordered and un-indexed distinct elements
    - Mathematics definition of a set can be applied in Python
    - Set is used to store unique items 
    - It is possible to find the 
        - union 
        - intersection  
        - difference 
        - symmetric difference 
        - subset 
        - super set  
        - disjoint set 
    among sets

### Creating a Set

`set()`: used to create an empty set
    - Empty curly brackets will create a dictionary

- Creating empty set: 
```python
st = set()
```

- Creating a set with intial items
```python
st = {'item1', 'item2', 'item3', 'item4'}
```

### Getting Set's Length
 
`len()`: used to find length of set
```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

### Accessing Items in a Set

We use loops to access items. Covered in the loop section

### Checking an Item

check if an item exist in a list we use in membership operator.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

### Adding Items to Set

Once a set is created we cannot change any items
But we can add additional items

- `add()`: add one item
```python
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

- `update()`: add multiple items, update() takes a list argument
```python
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

### Removing Items from a Set

- `remove()`: to remove an item
    - raise error if item not found
    - good to check if item exist
```python
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

- `discard()`: to remove an item
    - does not raise any error

- `pop()`: remove a random item and return the removed item
```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
```

### Clearing Items in a Set

`clear()`: to clear or empty the set
```python
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

### Deleting a Set

`del` operator: Delete the set itself
```python
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

### Converting List to Set

Comverting list to set removes duplicates, only unique items preserved
```python
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

### Joining Sets

To join 2 sets we can use
    - `union()`
    - `update()`
    - `|` symbol
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) # or st3 = st1 | st2
```
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

### Finding Intersection Items

`Intersection()`: returns a set of items which are in both the sets
    - & operator is also usable 

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2
```

### Checking Subset and Super Set

A set can be a subset or super set of other sets: 
    - Subset: `issubset()`
    - Super set: `issuperset()`

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

### Checking Difference Between Two Sets

`difference()`: returns the difference between two sets 
    - `-` symbol is also possible
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### Finding Symmetric Difference 

`symmetric_difference()`: returns a set that contains all items from both sets, except items that are present in both sets
    - mathematically: (A\B) ∪ (B\A)
    - can use `^` operator
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

Note the pattern, ### Checking Difference Between Two Sets

`difference()`: returns the difference between two sets 
    - `-` symbol is also possible
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### Finding Symmetric Difference 

`symmetric_difference()`: returns a set that contains all items from both sets, except items that are present in both sets
    - mathematically: (A\B) ∪ (B\A)
    - can use `^` operator
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

Note the pattern, symmetric_difference is basically unioning the difference of both set

### Disjoining Sets

`isdisjoint()`: checking is 2 sets are joint or disjoint
    - if 2 sets do not have common item or items we call them disjoint sets
```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```