# Day 12 - Modules | Exercises: Level 3

import random

# 1. Call your function shuffle_list, it takes a list as a parameter and it
#    returns a shuffled list

# REVIEW: correct, and the .copy() is the good call here. random.shuffle()
# shuffles IN PLACE and returns None — without the copy you'd mutate the
# caller's list. Classic trap: `return random.shuffle(arr)` returns None.
def shuffle_list(arr:list):
    shuffle_arr = arr.copy()
    random.shuffle(shuffle_arr)
    return shuffle_arr

# 2. Write a function which returns an array of seven random numbers in a
#    range of 0-9. All the numbers must be unique.
# MISTAKE: off-by-one. range(0, 9) stops at 8, so 9 can NEVER be drawn —
# verified over 200 runs, max was always 8. "range of 0-9" means 10 values:
# use range(10) (or range(0, 10)).
# INSIGHT: random.sample() is the right tool — samples WITHOUT replacement, so
# uniqueness is free. Note it silently would raise ValueError if you asked for
# more items than the population holds, which is a useful guardrail.
def random_unique_numbers():
    numbers = random.sample(range(0,10),7)
    return numbers

print(shuffle_list(['apple', 'banana', 'cherry', 'date', 'elderberry']))
print(random_unique_numbers())