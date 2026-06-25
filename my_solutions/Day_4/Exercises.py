# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = "Thirty"
string_2 = "Days"
string_3 = "Of"
string_4 = "Python"
string = string_1 + " " + string_2 + " " + string_3 + " " + string_4
print(string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_1 = 'Coding'
string_2 = 'For'
string_3 = 'All'
string = string_1 + " " + string_2 + " " + string_3
print(string)

#  Declare a variable named company and assign it to an initial value "Coding For All".
company = string

# Print the variable company using _print()_.
print(f"{company}")

# Print the length of the company string using _len()_ method and _print()_.
print(len(company))

# Change all the characters to uppercase letters using _upper()_ method.
company_upper = company.upper()
print(company_upper)

# Change all the characters to lowercase letters using _lower()_ method.
company_lower = company.lower()
print(company_lower)

# Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
company_capt = company.capitalize()
company_title = company.title()
company_swp = company.swapcase()
print(f"{company_capt}, {company_title} ,{company_swp}")

# Cut(slice) out the first word of _Coding For All_ string.
company_slice = company[1:]
print(f"{company_slice}")

# Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
index = company.index("Coding")
if index != -1:
    print(f"\'Coding\' exists at {index}")
else:
    print("\'Coding\' does not exists")

# Replace the word coding in the string 'Coding For All' to Python.
company_replace = company.replace('Coding', 'Python')
print(company_replace)

# Change "Python for Everyone" to "Python for All" using the replace method or other methods. 
new_string = "Python for Everyone"
print(new_string.replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) 
company_split = company.split(" ")
print(company_split)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_split = companies.split(",")
print(companies_split)

# What is the character at index 0 in the string _Coding For All_.
print(company[0])

# What is the last index of the string _Coding For All_.
print(company[-1])
print(company[len(company) - 1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
list_of_strings = 'Python For Everyone'.split(" ")
acronym = ""
for string in list_of_strings:
    acronym += string[0]
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
list_of_strings = 'Coding For All'.split(" ")
acronym = ""
for string in list_of_strings:
    acronym += string[0]
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
index = 'Coding For All'.index('C')
print(index)

# Use index to determine the position of the first occurrence of F in Coding For All.
index = 'Coding For All'.index('F')
print(index)

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
index = 'Coding For All People'.rindex('l')
print(index)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
index = sentence.find('because')
print(index)

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
index = sentence.rindex('because')
print(index)

# Slice out the phrase 'because because because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:47 + len('becuase')])

# Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
index = sentence.index('because')
print(index)

# Does 'Coding For All' start with a substring _Coding_?
sentence = 'Coding For All'
if sentence.startswith('Coding'):
    print("Yes")
else:
    print("No")

# Does 'Coding For All' end with a substring _coding_?
if sentence.endswith('Coding'):
    print("Yes")
else:
    print("No")

# '   Coding For All      ' 
# remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      ' 
print(sentence.strip())

# Which one of the following variables return True when we use the method isidentifier():
sentence_1 = '30DaysOfPython'
sentence_2 = 'thirty_days_of_python'
if sentence_1.isidentifier(): 
    print("sentence 1 return True")
else: 
    print("sentence_1 return False")
if sentence_2.isidentifier():
    print("sentence_2 return True")
else:
    print("sentence_2 returns False")

# The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
python_libaries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libaries))

# Use the new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines
print("Name\t\tAge\t\tCountry\t\tCity")
print("Asabeneh\t250\t\tFinland\t\tHelsinki")

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# Make the following using string formatting methods:
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print("{} / {} = {:.2f}".format(a,b,a/b))
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")