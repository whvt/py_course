import os

os.system("clear")


def validate_arguments(func):
    """
    Function "validate_arguments" raises ValueError
    on first not positive (zero included) value given.
    """

    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError("Validation not passed!")

        pass_wrap = func(*args, **kwargs)
        return f"Arguments given: {pass_wrap}, Validation passed"

    return wrapper


@validate_arguments
def get_arguments(*args):
    return args
