# Day 14 - Higher Order Functions | Exercises: Level 3

import sys
from pathlib import Path
from collections import Counter

# ponytail: path hack so this runs from any cwd; drop it if you always run from the repo root
sys.path.append(str(Path(__file__).parents[2] / 'data'))
from countries_data import countries_data as countries

# 1. Use the countries_data.py file and follow the tasks below:

#    - Sort countries by name, by capital, by population

countries_sorted_name = sorted(countries, key=lambda c: c['name'])
#print(countries_sorted_name)
countries_sorted_capital = sorted(countries, key= lambda c: c['capital'])
#print(countries_sorted_capital)
countries_sorted_population = sorted(countries, key = lambda c:c['population'])
#print(countries_sorted_population)

# NOTE: all three sorts are correct. Two things worth knowing about this data:
#   - 5 countries have capital == '' (Antarctica, Bouvet Island, ...). An empty
#     string sorts BEFORE every real capital, so they land at the top of the
#     capital sort. Not wrong, just be aware of what you are looking at.
#   - sorted() is stable and returns a NEW list, so `countries` itself is never
#     reordered. That is why you can reuse it for all three sorts safely.
# model answer: same as yours, plus reverse=True when you want biggest-first.
countries_sorted_population_desc = sorted(
    countries, key=lambda c: c['population'], reverse=True
)

#    - Sort out the ten most spoken languages by location.

languages = [lang for c in countries for lang in c['languages']]
languages_dict = Counter(lang for lang in languages)
most_common_languages = languages_dict.most_common(10)

print(most_common_languages)

# NOTE: correct - flattening every country's languages then counting is exactly
# what "by location" means here (how many countries speak it). One nit:
# `Counter(lang for lang in languages)` rebuilds the list one item at a time for
# no reason. Counter already accepts any iterable, so pass `languages` straight in.
# model answer:
most_common_languages_model = Counter(
    lang for c in countries for lang in c['languages']
).most_common(10)

print(most_common_languages_model)

#    - Sort out the ten most populated countries.

print(countries_sorted_population[:10])

# BUG: this prints the ten LEAST populated countries. countries_sorted_population
# is sorted ASCENDING, so [:10] is the small end - your output starts with
# Bouvet Island (population 0) and Antarctica (1000). "Most populated" needs the
# other end: either sort with reverse=True and take [:10], or slice [-10:] and
# reverse it. Also printing the raw dicts dumps flag URLs and currencies - pull
# out just the fields you asked about.
# model answer:
top_ten_populated = sorted(
    countries, key=lambda c: c['population'], reverse=True
)[:10]

for c in top_ten_populated:
    print(f"{c['name']}: {c['population']:,}")