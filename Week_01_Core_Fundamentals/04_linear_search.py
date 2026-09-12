"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
target = int(input("Enter a target value you would like to search for"))
list = []
for i in range(10):
    a = random.randint(1, 10)
    list.append(a)
def linear_search(list, target):
    for i in range(10):
      if list[i] == target:
        return i
    return -1
print(linear_search(list,target))
print(list)