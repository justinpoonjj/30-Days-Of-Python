# Day 13 - List Comprehension | Exercises

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

def filter_neg_zero(arr: list):
    filtered_arr = [i for i in arr if i <= 0]
    return filtered_arr

print(filter_neg_zero(numbers))

# 2. Flatten the following list of lists of lists to a one dimensional list:
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# REVIEW: correct for this data. INSIGHT: the nesting order in a comprehension
# reads like nested for-loops top-to-bottom — `for inner_list in arr` must come
# BEFORE `for number in inner_list`, since the second depends on the first.
# Note this flattens exactly one level; the task title says "lists of lists of
# lists" but the given data is only 2 deep, so one level is all you need.
def flatten_list(arr: list):
    flattened_arr = [number for inner_list in arr for number in inner_list]
    return flattened_arr

print(flatten_list(list_of_lists))

# 3. Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

# REVIEW: correct. INSIGHT: row 0 works because Python defines 0**0 == 1, which
# is why the expected first row is (0, 1, 0, 0, 0, 0, 0) and not (0, 0, ...).
list_of_tuples = [(i, i**0, i**1, i**2, i**3,i**4,i**5) for i in range(11)]
print(list_of_tuples)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# MISTAKE: city is not uppercased -> 'Helsinki', expected 'HELSINKI'.
# Add .upper() to country_tuple[1] (you got this right in #5).
# NIT: typo in the name — flatten_coutries -> flatten_countries.
flatten_coutries = [[country_tuple[0].upper(), country_tuple[0][:3].upper(), country_tuple[1].upper()] for country_list in countries for country_tuple in country_list]
print(flatten_coutries)

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

list_of_dictionary = [ {'country': country_tuple[0].upper(), 'city': country_tuple[1].upper()} for country_list in countries for country_tuple in country_list]
print(list_of_dictionary)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output:
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# REVIEW: correct — the 'Yetaeyeh' in the expected output is a typo in the
# course material; your 'Asabeneh Yetayeh' matches the input data.
# NIT: f'{name_tuple[0]} {name_tuple[1]}' reads better than + ' ' + concatenation.
list_of_concat_string = [name_tuple[0] + ' ' + name_tuple[1] for name_list in names for name_tuple in name_list]
print(list_of_concat_string)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
# REVIEW: the math is right. Two nits:
#   - arg order y2,y1,x2,x1 is easy to mis-call; slope(x1,y1,x2,y2) is the
#     conventional order and matches how points are usually written.
#   - a vertical line (x2 == x1) raises ZeroDivisionError. Fine to leave for a
#     lambda exercise, just know the slope is undefined there, not infinite.
slope = lambda y2,y1,x2,x1: (y2 - y1) / (x2 - x1)
y_intercept = lambda y,x,m: y - m*x
print(slope(4,2,4,2))
print(y_intercept(3,0,slope(4,2,4,2)))