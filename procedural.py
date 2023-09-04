
def main():
    num = 5
    result = 1

    for i in range(1, num + 1):
        result *= i

    print("Factorial of", num, "is", result)

if __name__ == "__main__":
    main()