import time
from collections import defaultdict


class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_data(self):
        return self.value

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
bst = BSTNode()
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if(bst.contains(name_2)):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


# init_list = [names_1, names_2]
# d = defaultdict(int)
# for values in init_list:
#     for v in set(values):
#         d[v] += 1
# final_list = [value for value, number in d.items() if number > 1]

# print(final_list)
# print(len(final_list))

# runtime approx .05 sec
