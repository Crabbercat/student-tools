from src.converter import celsius_to_fahrenheit, km_to_miles


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32


def test_km_to_miles():
    assert round(km_to_miles(1), 6) == 0.621371
