# Day 7 - Sets | Exercises: Level 3

# Given data
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert the ages to a set and compare the length of the list and the set,
#    which one is bigger?
ages = set(age)
if len(age) > len(ages):
    print("length of list is bigger")
elif len(age) == len(ages):
    print("length of list is equal to length of set")
else:
    print("length of set is bigger")

# 2. Explain the difference between the following data types:
#    string, list, tuple and set
"""
String is a list of characters having the characteristic of list data set
List is a ordered and mutable collection of data, able to store different types of data set
Tuple is a ordered and immutable collection of data, able to store duplicate elements
Set is an unordered and immutable collection of data, storing unique elements
"""


# 3. I am a teacher and I love to inspire and teach people.
#    How many unique words have been used in the sentence?
#    Use the split method and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
list_words = sentence.split(" ")
set_words = set(list_words)
print(f"There are {len(set_words)} unique words used in the sentence")

# ----------------------------------------------------------------------
# MISTAKES
# ----------------------------------------------------------------------
# #2 explanation:
#   - Set is MUTABLE, not immutable (you can .add() / .remove() elements).
#     Only a set's ELEMENTS must be immutable/hashable. The immutable
#     version is `frozenset`.
#   - String is better described as an immutable, ordered sequence of
#     characters (not "having the characteristic of a list" - lists are
#     mutable, strings are not).
#   - Tuple: correct that it can hold duplicates, but so can a list; the
#     distinguishing trait of a tuple is immutability.
