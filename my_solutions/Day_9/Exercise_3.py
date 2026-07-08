# Day 9 - Conditionals | Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript','React'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if the person dictionary has skills key, if so print out the middle skill
#    in the skills list.
def check_skills(person:dict):
    if "skills" in person:
        skills_list = person["skills"]
        length_of_skills = len(skills_list)
        mid = length_of_skills // 2
        print(f"Middle skill: {skills_list[mid]}")
    else: 
        print("Person has no skill list")
    

# 2. Check if the person dictionary has skills key, if so check if the person has
#    'Python' skill and print out the result.
def check_python_skill(person:dict):
    if "skills" in person:
        if "Python" in person["skills"]:
            print(True)
        else:
            print("Person does not have \'Python\' skill")
    else:
        print("Person does not have skill list")

# 3. If a person skills has only JavaScript and React, print('He is a front end
#    developer'), if the person skills has Node, Python, MongoDB, print('He is a
#    backend developer'), if the person skills has React, Node and MongoDB,
#    print('He is a fullstack developer'), else print('unknown title') - for more
#    accurate results more conditions can be nested!
def check_developer_type(person: dict):
    frontend = {'JavaScript','React'}
    backend = {'Node','Python','MongoDB'}
    fullstack = {'React','Node','MongoDB'}
    if "skills" in person:
        skill_list = person['skills']
        if frontend.issubset(set(skill_list)):
            print("He is a front end developer")
        elif backend.issubset(set(skill_list)):
            print("He is a back end developer")
        elif fullstack.issubset(set(skill_list)):
            print("He is a fullstack developer")
        else:
            print("unknown title")
    else:
        print("He does not have a skill list")
        

# 4. If the person is married and if he lives in Finland, print the information in
#    the following format:
#    Asabeneh Yetayeh lives in Finland. He is married.
def information(person:dict):
    first_name = person['first_name']
    last_name = person['last_name']
    country = person['country']
    string = f"{first_name} {last_name} lives in {country}. "
    if person['is_married']:
        str += f"He is married"
    else:
        string += f"He is not married"
    print(str)


#check_skills(person)
# check_python_skill(person)
# check_developer_type(person)
information(person)