# Day 12 - Modules | Exercises: Level 1

import random
import string
import sys

# 1. Write a function which generates a six digit/character random_user_id.
# print(random_user_id())
# '1ee33d'

# REVIEW: works. Two nits:
#   - `-> int` is wrong, it returns a str. Annotations aren't enforced at runtime
#     so nothing breaks, but linters/readers trust them. Use `-> str`.
#   - Task 1 asks for a *six* digit id with no args. `num_of_char=6` as a default
#     gives you both: random_user_id() for task 1, random_user_id(16) for task 2.
# INSIGHT: random.choices() samples WITH replacement -> repeats allowed, which is
# what you want for an id. random.sample() would be without replacement.
def random_user_id(num_of_char) -> int:
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choices(characters, k=num_of_char))
    return random_id

# print(random_user_id())


# 2. Modify the previous task. Declare a function named user_id_gen_by_user.
#    It doesn't take any parameters but it takes two inputs using input().
#    One of the inputs is the number of characters and the second input is
#    the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# output:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf
#
# print(user_id_gen_by_user()) # 16 5
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr

# MISTAKE: the task says "takes two inputs using input()", but this reads
# sys.argv — command-line args, not interactive input. It also crashes with
# IndexError if the script is run without two args (e.g. on plain `python
# Exercise_1.py`, or when imported). Swap to:
#     num_of_char = input('Number of characters: ')
#     num_of_ID   = input('Number of IDs: ')
# INSIGHT: input() always returns str, hence your int() casts — those are right.
def user_id_gen_by_user():
    num_of_char, num_of_ID = sys.argv[1], sys.argv[2]
    list_ID = []
    for i in range(int(num_of_ID)):
        list_ID.append(random_user_id(int(num_of_char)))
        print(list_ID[i])
    return list_ID

# 3. Write a function named rgb_color_gen. It will generate rgb colors
#    (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

# REVIEW: output is correct — 'rgb(77, 197, 104)' — but by accident.
# f"rgb{a,b,c}" builds a *tuple* and interpolates its repr, which happens to
# render as "(77, 197, 104)". Fragile: a 1-value version would print "(77,)".
# Say what you mean: f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})".
# NIT: task names it rgb_color_gen (US spelling) — matters if a test imports it.
# INSIGHT: randint(0, 255) is inclusive on BOTH ends, unlike range(0, 255).
def rgb_colour_gen():
    rgb = []
    for i in range(3):
        rgb.append(random.randint(0,255))
    return f"rgb{rgb[0],rgb[1],rgb[2]}"