# The pattern in generator expressions is: expression for variable in iterable
#
#
# variable: A simple name (like number, x, item)
# expression: What you do with that variable (like str(number), number * 2)
# You can't use a function call like str(number) as the loop variable itself.

numbers = list(range(10))
print(f"There are {len(numbers)} numbers in the list.")
print(f"The numbers are: {', '.join(str(number) for number in numbers)}")


even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

#even_numbers = [number for number in numbers if number % 2 == 0]
#              └─┬──┘   └───────┬────────┘ └────────┬────────┘
#                │               │                    │
#          What to keep    Loop through      Filter condition

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    # to simplify the code we can use
    # squares.append(value ** 2)
# even more conveniently, we can use a list comprehension
# squares = [value ** 2 for value in range(1, 11)]
print(squares)

print(*range(1, 21))
print(list(range(1, 21)))
print(', '.join(str(value) for value in range(1, 21)))




