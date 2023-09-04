
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Approach without functional programming
sum_even_squares = 0
for num in numbers:
    if num % 2 == 0:
        sum_even_squares += num ** 2

print("Sum of squares of even numbers:", sum_even_squares)
