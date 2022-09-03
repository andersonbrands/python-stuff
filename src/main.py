from functools import update_wrapper, wraps


def answer():
    return 42


def basic_decorator(func):
    def wrapper():
        return func()

    return wrapper


def cool_decorator(func):
    @wraps(func)
    def wrapper():
        return func()

    return wrapper


def cooler_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def offset(offset_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + offset_

        return wrapper

    return decorator


class PrintNameUpper:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.name_upper = str(func.__name__).upper()

    def __call__(self, *args, **kwargs):
        print(self.name_upper)
        return self.func(*args, **kwargs)
