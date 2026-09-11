"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import numbers


def main():
  values = []
  a = int(input("How many numbers would you like to enter?"))
  while a<1:
    a = int(input("How many numbers would you like to enter?"))
  for i in range(a):
    b = int(input("Enter a number"))
    values.append(b)
  def calculate_average(values):
    average = sum(values) / len(values)
    return average
  average = calculate_average(values)
  print("The average is", average)
  pass

if __name__ == "__main__":
    main()
