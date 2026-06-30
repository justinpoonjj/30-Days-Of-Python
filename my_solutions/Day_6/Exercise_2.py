family_members = ('brother_1', 'brother_2', 'brother_3', 'sister_1', 'sister_2', 'sister_3', 'Father', 'Mother')

# Unpack siblings and parents from family_members
*siblings, parent_1, parent_2 = family_members
parents = (parent_1, parent_2)
print(siblings, parents)

# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "mango", "strawberry", "orange")
vegetables = ("broccoli", "spinach", "carrot", "onion", "tomato")
animal_products = ("milk", "cheese", "eggs", "chicken", "beef")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 1:
    print(food_stuff_tp[mid])
else:
    print(food_stuff_tp[mid: mid+2])

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three, last_three)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("\'Estonia\' is a nordic country")
if 'Iceland' in nordic_countries:
    print("\'Iceland\' is a nordic country")