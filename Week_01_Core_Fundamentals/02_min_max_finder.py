"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

numbers = []
x = int(input("How many numbers would you like to enter?"))
for i in range(x):
  a = int(input("Enter a number: "))
  numbers.append(a)
def find_min_max(numbers):
  length = len(numbers)
  mx = numbers[0]
  for i in range(length):
    if numbers[i] > mx:
      mx = numbers[i]
  mn = numbers[0]
  for i in range(length):
    if numbers[i] < mn:
      mn = numbers[i]
  return (mn, mx)
print(find_min_max(numbers))
