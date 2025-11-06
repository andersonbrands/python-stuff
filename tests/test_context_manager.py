from unittest.mock import Mock

from context_manager import ClassyContextManager, funky_context_manager


def test_class_context_manager():
    mock = Mock()
    with ClassyContextManager(mock) as classy:
        assert classy is mock


def test_funky_context_manager():
    mock = Mock()
    with funky_context_manager(mock) as funky:
        assert funky is mock
