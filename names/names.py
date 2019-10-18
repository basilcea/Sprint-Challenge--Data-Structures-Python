from binary_search_tree import BinarySearchTree
import time
import sys

start_time = time.time()

f = open('names_1.txt', 'r')  # O(c)
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')  # O(c)
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1: #O(n)
#     for name_2 in names_2: #O(n)
#         if name_1 == name_2:
#             duplicates.append(name_1) #O(c)
listed = BinarySearchTree(names_1[0])
for name_1 in names_1: #0(n)
    listed.insert(name_1)
for name_2 in names_2: #0(n)
    if listed.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# runtime ----> 0(n) + 0(n) ------> 0(2n) ----> 0(n)
