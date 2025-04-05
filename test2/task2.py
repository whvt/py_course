import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()


class ProcessNum:
    def __init__(self, input_num):
        self.input_num = input_num

    def get_square(self):
        input_num_valid = isinstance(self.input_num, int)
        return self.input_num * self.input_num if input_num_valid else None

    def is_odd(self):
        return True if (self.input_num % 2 == 0 and self.input_num != 0) else False


reference = ProcessNum(12)

logger.info("Reference's square is: %s", reference.get_square())
logger.info("Given number is odd? -> %s", reference.is_odd())
