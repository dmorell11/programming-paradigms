
import concurrent.futures

# Function to calculate the square of a number
def calculate_square(number):
    return number * number

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]

    # Use ThreadPoolExecutor to run tasks in parallel.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map function to numbers and get results.
        results = list(executor.map(calculate_square, numbers))

    print("Results:", results)
