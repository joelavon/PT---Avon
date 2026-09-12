"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
list = []
for i in range(10):
    a = random.randint(1, 10)
    list.append(a)
def reverse_list(list):
  reversed_list = []
  for i in range(10):
    reversed_list.append(list[9-i])
  return reversed_list
print(list)
print(reverse_list(list))