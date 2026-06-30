# Declare an empty list
lst = []
lst = list()

# Declare a list with more than 5 items
lst = [0,1,2,3,4]

# Find the length of your list
length = len(lst)
print(length)

# Get the first item, the middle item and the last item of the list
first = lst[0]
middle = lst[int(length/2)]
last = lst[-1]
print(first,middle,last)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Justin", 23, 1.65, "Taken", "address"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(mixed_data_types)
print(it_companies)

# Print the number of it_companies in the list
length = len(it_companies)
print(length)

# Print the first, middle and last company
first = it_companies[0]
middle = it_companies[int(length/2)]
last = it_companies[-1]
print(first, middle, last)

# Print the list after modifying one of the it_companies
it_companies[4] = "NVDIA"
print(it_companies)

# Add an IT company to it_it_companies
it_companies.append("IBM")
print(it_companies)

# Insert an IT company in the middle of the companies list
mid = int(len(it_companies) / 2)
it_companies.insert(mid, "ST Engg")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
string = '#; '.join(it_companies)
print(string)

# Check if a certain company exists in the it_companies list.
if "Facebook" in it_companies:
    print("True")
else:
    print("False")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# Slice out the middle IT company or companies from the list
mid = len(it_companies) // 2
print(it_companies[mid])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
mid = len(it_companies) // 2
it_companies.pop(mid)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
combine = front_end + back_end
print(combine)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, 
# then insert Python and SQL after Redux.
full_stack = combine.copy()
Redux_index = full_stack.index("Redux")
full_stack.insert(Redux_index,"SQL")
full_stack.insert(Redux_index,"Python")
print(full_stack)

