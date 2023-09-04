
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Functional programming approach
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_squares = map(lambda x: x ** 2, even_numbers)
sum_even_squares = sum(even_squares)

print("Sum of squares of even numbers:", sum_even_squares)
