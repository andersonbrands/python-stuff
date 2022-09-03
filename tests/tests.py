from main import (
    PrintNameUpper,
    answer,
    basic_decorator,
    cool_decorator,
    cooler_decorator,
    offset,
)


def test_answer():
    assert 42 == answer()


def test_basic_decorator_changes_name_and_doc():
    def bla():
        """blabla"""
        pass

    assert "bla" == bla.__name__
    assert "blabla" == bla.__doc__

    bla = basic_decorator(bla)

    assert "bla" != bla.__name__
    assert "blabla" != bla.__doc__


def test_cool_decorator_keeps_name_and_doc():
    def bla():
        """blabla"""
        pass

    assert "bla" == bla.__name__
    assert "blabla" == bla.__doc__

    bla = cool_decorator(bla)

    assert "bla" == bla.__name__
    assert "blabla" == bla.__doc__


def test_cooler_decorator_decorates_functions_with_args_and_kwargs():
    @cooler_decorator
    def bla(a):
        pass

    @cooler_decorator
    def ble(a, b):
        pass

    bla(1)
    ble(1, b=2)


def test_decorator_with_args():
    @offset(42)
    def bla(a):
        return a

    value = 5
    assert (value + 42) == bla(value)


def test_class_decorator(capsys):
    @PrintNameUpper
    def bla():
        pass

    bla()
    out = capsys.readouterr().out
    assert "BLA" in out
    assert "bla" not in out
