import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def calculate_sum_upto(n):
    pos = sum(range(1, n + 1))
    neg = sum(range(n, 1))

    return pos if n > 0 else neg


number = -2
result = calculate_sum_upto(number)
logger.info("Summ is: %s", result)
