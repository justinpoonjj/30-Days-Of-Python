# Day 14 - Higher Order Functions | Exercises: Level 2

from functools import reduce
import sys
from pathlib import Path

# ponytail: path hack so this runs from any cwd; drop it if you always run from the repo root
sys.path.append(str(Path(__file__).parents[2] / 'data'))
from countries import countries as all_countries

# Given data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map to create a new list by changing each country to uppercase in the countries list

def to_upper(name: str):
    return name.upper()

uppercase_countries = map(to_upper,countries)
print(list(uppercase_countries))

# 2. Use map to create a new list by changing each number to its square in the numbers list

def square(number: int):
    return number ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

# 3. Use map to change each name to uppercase in the names list

uppercase_names = map(to_upper, names)
print(list(uppercase_names))

# 4. Use filter to filter out countries containing 'land'.

def contain_land(name: str):
    if "land" in name:
        return True
    return False

countries_with_land = filter(contain_land, countries)
print(list(countries_with_land))

# 5. Use filter to filter out countries having exactly six characters.

def have_six_char(name: str):
    if len(name) == 6:
        return True
    return False

counties_with_six_char = filter(have_six_char, countries)
print(list(counties_with_six_char))

# 6. Use filter to filter out countries containing six letters and more in the country list.

def have_six_char_or_more(name: str):
    if len(name) >= 6:
        return True
    return False

counties_with_six_char_and_more = filter(have_six_char_or_more, countries)
print(list(counties_with_six_char_and_more))

# 7. Use filter to filter out countries starting with an 'E'

def start_with_E(name: str):
    if name.startswith('E'):
        return True
    return False

countries_start_with_E = filter(start_with_E, countries)
print(list(countries_start_with_E))

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

numbers_even_squared = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))
print(list(numbers_even_squared))

# 9. Declare a function called get_string_lists which takes a list as a parameter
#    and then returns a list containing only string items.

def get_string_lists(arr: list):
    return list(filter(lambda item: type(item) == str, arr))

print(list(get_string_lists([1,2,"3","4"])))

# NOTE: the list() wrap is right - a bare filter object is single-use, so a
# second iteration would come back empty. Only nit left: prefer isinstance
# over type(...) == str, so str subclasses still count.
# model answer:
def get_string_lists_model(arr: list):
    return list(filter(lambda item: isinstance(item, str), arr))

print(get_string_lists_model([1, 2, "3", "4"]))

# 10. Use reduce to sum all the numbers in the numbers list.

total = reduce(lambda x, y: x + y, numbers)
print(total)

# 11. Use reduce to concatenate all the countries and to produce this sentence:
#     Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

sentence = reduce(lambda x,y: x + ", " + y, countries) + " are north European countries"
print(sentence)

# NOTE: target sentence has "and Iceland". A reduce over all six can't insert
# it - join everything but the last, then tack the last on separately.
# model answer:
sentence_model = (
    reduce(lambda x, y: x + ", " + y, countries[:-1])
    + ", and " + countries[-1]
    + " are north European countries"
)
print(sentence_model)

# 12. Declare a function called categorize_countries that returns a list of countries
#     with some common pattern (you can find the countries list in this repository
#     as countries.py) (eg 'land', 'ia', 'island', 'stan').

def categorize_countries(arr: list):
    return filter(lambda name: "land" in name, arr)

print(list(categorize_countries(countries)))

# NOTE: same filter-object issue as #9, and the pattern is hardcoded - the
# prompt lists several ('land', 'ia', 'stan'), so it wants to be a parameter.
# model answer:
def categorize_countries_model(arr: list, pattern: str):
    return list(filter(lambda name: pattern in name, arr))

print(categorize_countries_model(all_countries, 'stan'))

# 13. Create a function returning a dictionary, where keys stand for starting letters
#     of countries and values are the number of country names starting with that letter.

def dict_countries(countries: list):
    dictionary = dict()
    for country in countries:
        if country[0].upper() in dictionary:
            dictionary[country[0].upper()] += 1
        else:
            dictionary[country[0].upper()] = 1
    return dictionary

print(dict(dict_countries(countries)))

# NOTE: correct. Two nits: the parameter is named `countries`, which shadows
# the global list of the same name - fine today, a bug the day the function
# needs the outer one. And the whole loop is what collections.Counter does.
# model answer:
from collections import Counter

def dict_countries_model(arr: list):
    return dict(Counter(name[0].upper() for name in arr))

print(dict_countries_model(countries))

# 14. Declare a get_first_ten_countries function - it returns a list of first ten
#     countries from the countries.py list in the data folder.

def get_first_ten_countries(countries: list):
    return countries[:10]

print(get_first_ten_countries(all_countries))

# 15. Declare a get_last_ten_countries function that returns the last ten countries
#     in the countries list.

def get_last_ten_countries(countries:list):
    return countries[-10:-1]

print(get_last_ten_countries(all_countries))

# NOTE: still off by one - [-10:-1] stops BEFORE the last item, so this returns
# 9 countries and drops Zimbabwe. A negative stop excludes that element just
# like a positive one does. Omit the stop entirely to run to the end.
# model answer:
def get_last_ten_countries_model(arr: list):
    return arr[-10:]

print(get_last_ten_countries_model(all_countries))