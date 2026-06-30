# Create an empty tuple
tpl = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("brother_1", "brother_2", "brother_3")
sisters = ("sister_1","sister_2","sister_3")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append("Father")
family_members.append("Mother")
family_members = tuple(family_members)
print(family_members)