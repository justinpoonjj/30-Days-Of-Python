# Day 8 - Dictionaries | Exercises

# 1. Create an empty dictionary called dog
dog = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Xiao Hei"
dog['color'] = 'black'
dog['breed'] = 'shiba inu'
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary and add first_name, last_name, gender, age,
#    marital status, skills, country, city and address as keys
student = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'gender' : 'male',
    'age' : 18,
    'marital status' : 'single',
    'skills' : [],
    'country' : 'Singapore',
    'city': 'Singapore',
    'address': 'Jalan lapang 3'
}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].append("frisbee")
student['skills'].append("tennis")
print(student['skills'])

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list
print(student.values())

# 9. Change the dictionary to a list of tuples using items() method
print(list(student.items()))

# 10. Delete one of the items in the dictionary
del student['city']
print(student)

# 11. Delete one of the dictionaries
del student