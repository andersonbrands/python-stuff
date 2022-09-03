from unittest.mock import Mock

from main import ClassyContextManager, answer, funky_context_manager


def test_answer():
    assert 42 == answer()


def test_class_context_manager():
    mock = Mock()
    with ClassyContextManager(mock) as classy:
        assert classy is mock


def test_funky_context_manager():
    mock = Mock()
    with funky_context_manager(mock) as funky:
        assert funky is mock
