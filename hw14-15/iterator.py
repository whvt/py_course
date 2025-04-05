import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("NumberGeneratorLogger")


def number_generator(n):
    for i in range(1, n + 1):
        logger.info(f"Generated number: {i}")
        yield i


def main():
    try:
        user_input = input("Enter an integer (N): ")
        n = int(user_input)
        logger.info(f"User provided input: {n}")

        if n <= 0:
            raise ValueError("The input number must be a positive integer.")

        gen = number_generator(n)
        total = sum(gen)
        logger.info(f"Sum of numbers from 1 to {n}: {total}")

        print(f"The sum of numbers from 1 to {n} is: {total}")
    except ValueError as e:
        logger.error(f"Error occurred: {e}")
        print("Invalid input. Please enter a positive integer.")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        print("An unexpected error occurred.")


if __name__ == "__main__":
    main()
