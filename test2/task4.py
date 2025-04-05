import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def add_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


logger.info(add_one([9]))
logger.info(add_one([1, 2, 3]))
logger.info(add_one([1, 1, 9]))
logger.info(add_one([9, 9, 9]))
