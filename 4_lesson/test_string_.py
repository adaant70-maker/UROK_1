import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("Тест", "Тест"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("123abc", "123abc")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str", [
    None,
    "",
    "   ",
    [],
    123
])
def test_capitalize_negative(input_str):
    if isinstance(input_str, str):
        assert string_utils.capitalize(input_str) == input_str
    else:
        with pytest.raises(TypeError):
            string_utils.capitalize(input_str)