import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def transform_string(s, n):
    if n <= 0 or n > len(s):
        raise ValueError("Wrong input")

    p = s[:n]
    result = list(p)

    for i in range(n - 2, -1, -1):
        result.append(p[i])

    return "".join(result)


s1 = "123"
logger.info(transform_string(s1, 1))
logger.info(transform_string(s1, 2))
logger.info(transform_string(s1, 3))
logger.info(transform_string(s1, 4))  # ValueError: Wrong input
