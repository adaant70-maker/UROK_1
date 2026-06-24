import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# БЛОК ПОЗИТИВНЫХ ТЕСТОВ для метода capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
     # Тест со строкой, содержащей пробел
    ("hello world", "Hello world"),
     # Тест с одной буквой
    ("a", "A"),
    # Тест с полностью заглавной строкой
    ("PYTHON", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# БЛОК НЕГАТИВНЫХ ТЕСТОВ для метода capitalize
# Проверяем обработку некорректных входных данных

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
     # Тест с кириллицей
    ("привет", "Привет"),
    # Тест со строкой, начинающейся с символа
    ("!hello", "!hello"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Примеры теста для метода trim
# Позитивные тесты

import pytest

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # Базовый случай: пробелы только слева
    ("   skypro", "skypro"),
    # Пробелы слева и справа: справа пробелы должны остаться
    ("  hello world  ", "hello world  "),
    # Строка без ведущих пробелов: должна остаться без изменений
    ("no_leading_spaces", "no_leading_spaces"),
])
def test_trim_positive(input_str, expected):
    # Предполагаем, что trim является методом класса StringUtils
    from string_utils import StringUtils
    utils = StringUtils()
    assert utils.trim(input_str) == expected

# Негативные тесты

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # Табуляция в начале: функция НЕ должна её удалять (так как удаляет только пробел " ")
    ("\t\t  skypro", "\t\t  skypro"),
    # Перенос строки в начале: функция НЕ должна его удалять
    ("\n\n  skypro", "\n\n  skypro"),
    # Смешанные символы: удаляем только пробелы, остальное оставляем
    ("  \t  skypro", "\t  skypro"),
])
def test_trim_negative_edge_cases(input_str, expected):
    from string_utils import StringUtils
    utils = StringUtils()
    assert utils.trim(input_str) == expected


# Примеры теста для contains
# Позитивные тесты

import pytest

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    # Символ в начале строки
    ("SkyPro", "S", True),
    # Символ в середине строки
    ("SkyPro", "y", True),
    # Символ в конце строки
    ("SkyPro", "o", True),
    # Строка содержит несколько таких символов
    ("banana", "a", True),
])
def test_contains_positive(string, symbol, expected):
    from string_utils import StringUtils
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected

# Негативные тесты

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    # Символ отсутствует
    ("SkyPro", "U", False),
    # Проверка регистра (строчная 's' не равна заглавной 'S')
    ("SkyPro", "s", False),
    # Пустая строка: в ней не может содержаться никакой символ
    ("", "a", False),
])
def test_contains_negative(string, symbol, expected):
    from string_utils import StringUtils
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected


# Примеры теста для delete_symbol

import pytest

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    # Удаление символа, который встречается несколько раз
    ("banana", "a", "bnn"),
    # Удаление символа, который встречается один раз
    ("SkyPro", "P", "Skyro"),
    # Символ отсутствует — строка не меняется
    ("SkyPro", "z", "SkyPro"),
    # Удаление пробела
    ("a b c", " ", "abc"),
])
def test_delete_symbol_positive(string, symbol, expected):
    from string_utils import StringUtils
    utils = StringUtils()
    assert utils.delete_symbol(string, symbol) == expected

