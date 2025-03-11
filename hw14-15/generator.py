import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("PrimeNumberGeneratorLogger")


def prime_number_generator(start, end):
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            logger.info(f"Generated prime number: {num}")
            yield num


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start > end:
            raise ValueError(
                "Start of range must be less than or equal to the end of range."
            )

        logger.info(f"Generating prime numbers in range {start} to {end}...")

        prime_gen = prime_number_generator(start, end)
        primes = [next(prime_gen) for _ in range(10)]
        logger.info(f"First 10 prime numbers in range {start} to {end}: {primes}")

        print(f"The first 10 prime numbers in range {start} to {end} are: {primes}")
    except StopIteration:
        logger.warning("There are fewer than 10 prime numbers in the given range.")
        print("The range contains fewer than 10 prime numbers.")
    except ValueError as e:
        logger.error(f"Error: {e}")
        print("Invalid input. Please enter valid integer values.")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        print("An unexpected error occurred.")


if __name__ == "__main__":
    main()
