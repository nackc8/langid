from langcode import is_valid_langcode


def test_is_valid_langcode():
    assert is_valid_langcode("sv") == False
