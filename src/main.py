from contextlib import contextmanager


def answer():
    return 42


class ClassyContextManager:
    def __init__(self, thing):
        self.thing = thing

    def __enter__(self):
        return self.thing

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@contextmanager
def funky_context_manager(thing):
    yield thing
