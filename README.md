# student-tools
Dự án cung cấp một tập hợp các công cụ đơn giản phục vụ sinh viên.

## Chuyển đổi nhiệt độ

- `kelvin_to_celsius(kelvin)`: chuyển nhiệt độ Kelvin sang Celsius theo công thức `Celsius = Kelvin - 273.15`.
## Converter usage

The temperature converter accepts numeric values. Convert Celsius to
Fahrenheit with `celsius_to_fahrenheit(celsius)`:

```python
from src.converter import celsius_to_fahrenheit

fahrenheit = celsius_to_fahrenheit(25)
print(fahrenheit)  # 77.0
```

The formula is `fahrenheit = (celsius * 9 / 5) + 32`.

To convert Fahrenheit to Celsius, use `celsius = (fahrenheit - 32) * 5 / 9`.
For example, `77` Fahrenheit becomes `25.0` Celsius. Both the input and
output are numeric temperature values.

See [docs/usage.md](docs/usage.md) for the complete converter and tool usage
guide.
