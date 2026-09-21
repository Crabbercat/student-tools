def is_positive_number(value):
    return isinstance(value, (int, float)) and value > 0


def is_non_empty_text(value):
    return isinstance(value, str) and value.strip() != ""
