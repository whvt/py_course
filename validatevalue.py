import os

os.system("clear")


def validate_value(func):
    """
    Function "validate_value" prints Error message
    if value given is not int, returns True otherwise
    """

    def wrapper(*args):
        error_message = ""
        for arg in args:
            if not isinstance(arg, int):
                error_message = "One of given arguments is not integer"
        pass_wrap = func(*args)
        return f"Arguments given: {pass_wrap} {error_message}"

    return wrapper


@validate_value
def get_value(*args):
    return args


print(get_value(1, "s"))
