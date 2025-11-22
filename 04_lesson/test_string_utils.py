import pytest
from string_utils import StringUtils

redactor = StringUtils()


# capitalize - слизано с подсказки, печатает строку с Заглавной буквы, все остальные - строчными

@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('skypro', 'Skypro'),
    ('hello world', 'Hello world'),
    ('python', 'Python'),
    ('p', 'P'),
    ('tesT', 'Test'),
    ('456', '456')
])
def test_capitalize_positive(input_str, expected):
    assert redactor.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('123abc', '123abc'),
    ('', ''),
    ('   ', '   '),
    ('!test', '!test'),
    (None, None)  # тест провален, но согласно описанию функции параметр д.б. типа "строка" - не баг
])
def test_capitalize_negative(input_str, expected):
    assert redactor.capitalize(input_str) == expected


# trim - удаляет пробелы в начале строки

@pytest.mark.positive
@pytest.mark.parametrize('text, result', [
    ('   Test1', 'Test1'),
    (' python', 'python'),
    (' test   ', 'test   '),
    (' 123test', '123test'),
    (' test tester testing', 'test tester testing')
])
def test_trim_positive(text, result):
    assert redactor.trim(text) == result


@pytest.mark.negative
@pytest.mark.parametrize('text, result', [
    ('test', 'test'),
    ('', ''),
    ('        ', ''),
    ('_test', '_test'),
    (None, '')  # тест провален, но согласно описанию функции параметр д.б. типа "строка" - не баг
])
def test_trim_negative(text, result):
    assert redactor.trim(text) == result


# contains - отвечает на вопрос - есть ли заданный символ в переданной строке

@pytest.mark.positive
@pytest.mark.parametrize('text, symbol, result', [
    ('home', 'o', True),
    ('homework', 'o', True),
    ('My name is', 'M', True),
    ('telephone', 'w', False),
    ('Jump!', '!', True),
    ('159', '5', True)
])
def test_contains_positive(text, symbol, result):
    assert redactor.contains(text, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize('text, symbol, result', [
    ('', 'o', False),
    ('   ', ' ', True),
    ('MMM', 'M', True),
    (None, '0', False),  # тест провален, но согласно описанию функции параметр д.б. типа "строка" - не баг
    ('!.!!+', '.', True),
    ('15985', '59', True),
    ('testX', None, False),  # тест провален, но согласно описанию функции параметр д.б. типа "строка" - не баг
    ('cool', 'о', False)  # поиск русской о в слове на английской раскладке
])
def test_contains_negative(text, symbol, result):
    assert redactor.contains(text, symbol) == result


# delete_symbol - удаляет символ или слово из заданной строки, возвращает урезанную строку

@pytest.mark.positive
@pytest.mark.parametrize('text, repl_str, result', [
    ('test', 't', 'es'),
    ('Summer', 'mer', 'Sum'),
    ('Christmas tree', ' ', 'Christmastree'),
    ('', '', ''),
    (' ', ' ', ''),
    ('1597534994249', '34', '15975994249')
])
def test_delete_symbol_positive(text, repl_str, result):
    assert redactor.delete_symbol(text, repl_str) == result


@pytest.mark.negative
@pytest.mark.parametrize('text, repl_str, result', [
    ('test', 'y', 'test'),
    ('1', '1', ''),
    ('rrrrrrrraw', 'rrr', 'rraw'),
    # согласно документации удаляет повторяющиеся наборы (rrr) столько раз, сколько сможет
    ('...empty', 'mpt', '...ey'),
    ('8-800-800-80-80', '-', '88008008080'),
    ('10000000000', '0000000000', '1'),
    ('20000000000', '00000', '2'),
    ('oooooooooops', 'ooooo', 'ps')
])
def test_delete_symbol_negative(text, repl_str, result):
    assert redactor.delete_symbol(text, repl_str) == result
