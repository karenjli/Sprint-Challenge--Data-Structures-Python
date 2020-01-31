import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Run time is 10.3 seconds
# The run time complexity is O(n^2)
# because each item in the first list needs to loop through
# every single item in the second list once. Hence, it results in a
# n^2 run time complexity.

# Need to reduce to 1 or less second
# Double for loop is time consuming
# The following method runs in O(n) becauase it only needs tro loop through
# the lists once.

# Create a hash
hash = {}

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for names in names_1:
    # Save each item in file 1 in hash
    hash[names] = True

for names_in_two in names_2:
    # check if each name is in hash
    if names_in_two in hash:
        # add duplicated name to the duplicates array
        duplicates.append(names_in_two)
    else:
        pass

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
