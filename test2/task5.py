import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


def is_palindrome(s):
    solution = bool(s == s[::-1])

    return solution


logger.info("Is palindrome -> %s", is_palindrome("mam mam "))
