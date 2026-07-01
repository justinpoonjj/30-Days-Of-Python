# Day 7 - Sets | Exercises: Level 2

# Given data
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
C = A.union(B)
print(C)

# 2. Find A intersection B
intersection = A.intersection(B)
print(intersection)

# 3. Is A subset of B
if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

# 4. Are A and B disjoint sets
if A.isdisjoint(B):
    print("A and B disjoint sets")
else:
    print("A and B are not disjoint sets")

# 5. Join A with B and B with A
A = A.union(B)
B = B.union(A)
print(A)
print(B)

# 6. What is the symmetric difference between A and B
symm_diff = A.symmetric_difference(B)
print(symm_diff)

# 7. Delete the sets completely
del A
del B

# ----------------------------------------------------------------------
# MISTAKES
# ----------------------------------------------------------------------
# #5 breaks #6: reassigning A and B to the union overwrites the originals,
#    so by the time #6 runs A and B are identical -> symmetric_difference
#    prints set() instead of the expected {27, 28}.
#    Fix: don't reassign; just print the two unions so the originals survive:
#        print(A.union(B))
#        print(B.union(A))
