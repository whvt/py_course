class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_first(self):
        return self.input_string[0] if self.input_string else None

    def get_last(self):
        return self.input_string[-1] if self.input_string else None

    def get_third(self):
        return self.input_string[2] if len(self.input_string) >= 3 else None

    def get_third_from_end_character(self):
        return self.input_string[-3] if len(self.input_string) >= 3 else None

    def get_length(self):
        return len(self.input_string)

    def reverse_string(self):
        return self.input_string[::-1]

    def get_first_eight_characters(self):
        return (
            self.input_string[:8] if len(self.input_string) >= 8 else self.input_string
        )


line = StringProcessor(
    """Neque porro quisquam est qui dolorem
    ipsum quia dolor sit amet, consectetur, adipisci velit."""
)
print("First symbol:", line.get_first())
print("Last symbol:", line.get_last())
print("Third from start:", line.get_third())
print("Third from end:", line.get_third_from_end_character())
print("Len:", line.get_length())
print("Reversed:", line.reverse_string())
print("First five chars:", line.get_first_eight_characters())
