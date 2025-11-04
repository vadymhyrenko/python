# print(', ' .join(str(number) for number in range(1, 21)))

# print(foo :="bar".title())

#numbers = list(range(1, 21))
#print(numbers)

#print(*range(1, 21))

# million_numbers = list(range(1, 1_000_001))
# for number in million_numbers:
#     print(number)

# print(min(million_numbers))
# print(max(million_numbers))
# print(sum(million_numbers))

# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)
#
# odd_numbers = [number for number in numbers if number % 2 != 0]
# print(odd_numbers)
#
# even_numbers = list(range(1, 21, 2))
# print(even_numbers)

# numbers = list(range(3, 31, 3))
# for number in numbers:
#     print(number)

numbers = list(range(1, 11))
# cubes = [number ** 3 for number in numbers]
# print(cubes)
print(', ' .join(str(number**3) for number in numbers))
print(', ' .join(str(number**3) for number in list(range(1, 11))))
