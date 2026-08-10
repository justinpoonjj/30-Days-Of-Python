# Day 12 - Modules | Exercises: Level 2

import string
import random

# 1. Write a function list_of_hexa_colors which returns any number of
#    hexadecimal colors in an array (six hexadecimal numbers written after #.
#    Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6
#    letters of the alphabet, a-f. Check the task 6 for output examples).

# REVIEW: correct. `string.digits + "abcdef"` is exactly the 16 hex symbols.
# INSIGHT: string.hexdigits exists but is '0123456789abcdefABCDEF' (22 chars,
# both cases) — your version is actually the better fit for lowercase hex.
def list_of_hexa_colors(num: int):
    characters = string.digits + "abcdef"
    list_of_hexa = []
    for i in range(num):
        hexa_color = ''.join(random.choices(characters,k=6))
        list_of_hexa.append('#' + hexa_color)
    return list_of_hexa

# NIT: a bare print at module level runs on *import* too, not just when you run
# this file. Park test calls under `if __name__ == '__main__':` — that's the
# whole point of the __name__ trick from today's Modules lesson.
print(list_of_hexa_colors(3))

# 2. Write a function list_of_rgb_colors which returns any number of RGB
#    colors in an array.

# MISTAKE: typo — f"rbg{...}" should be "rgb". Output is 'rbg(5, 55, 175)'.
# Silent bug: nothing errors, the string is just wrong. This is why reusing
# rgb_colour_gen() from Exercise_1 beats retyping the format string.
# REVIEW: `rgb = []` outside the loop + .clear() works, but it's a shared
# mutable you have to remember to reset. Declaring `rgb = []` INSIDE the
# for-loop is one less thing to get wrong.
def list_of_rgb_colors(num: int):
    list_of_rgb = []
    rgb = []
    for i in range(num):
        for j in range(3):
            rgb.append(random.randint(0,255))
        list_of_rgb.append(f"rbg{rgb[0],rgb[1],rgb[2]}")
        rgb.clear()
    return list_of_rgb

# 3. Write a function generate_colors which can generate any number of hexa
#    or rgb colors.
# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

# REVIEW: dispatch logic is right. Two nits:
#   - `type` shadows the builtin type(). Harmless here, bites you the day you
#     need type(x) in this function. Name it color_type.
#   - An unknown type falls off the end and returns None silently. Either
#     `return []` or raise ValueError so a typo'd call fails loudly.
def generate_colors(type, num):
    if type == 'hexa':
        return list_of_hexa_colors(num)
    if type == 'rgb':
        return list_of_rgb_colors(num)

