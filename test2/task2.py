class ProcessNum:
    def __init__(self, input_num):
        self.input_num = input_num

    def get_square(self):
        input_num_valid = isinstance(self.input_num, int)
        return self.input_num * self.input_num if input_num_valid else None

    def is_odd(self):
        return True if (self.input_num % 2 == 0 and self.input_num != 0) else False


reference = ProcessNum(12)

print("References square is:", reference.get_square())
print("Given number is odd? ->", reference.is_odd())
