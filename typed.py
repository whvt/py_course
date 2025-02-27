import os

os.system("clear")


def typed(typ):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = [typ(arg) for arg in args]
            new_kwargs = {k: typ(v) for k, v in kwargs.items()}
            return func(*new_args, **new_kwargs)

        return wrapper

    return decorator


@typed(typ=str)
def add(a, b):
    return a + b


print(add("3", 5))  # "35"
print(add(5, 5))  # "55"
print(add("a", "b"))  # 'ab'
