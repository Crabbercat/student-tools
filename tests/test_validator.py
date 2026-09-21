from src.validator import is_non_empty_text, is_positive_number


def test_is_positive_number():
    assert is_positive_number(3)
    assert not is_positive_number(-1)


def test_is_non_empty_text():
    assert is_non_empty_text("hello")
    assert not is_non_empty_text("   ")
