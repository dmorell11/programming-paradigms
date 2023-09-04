
def calculate_factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def main():
    num = 5
    fact = calculate_factorial(num)
    print("Factorial of", num, "is", fact)

if __name__ == "__main__":
    main()