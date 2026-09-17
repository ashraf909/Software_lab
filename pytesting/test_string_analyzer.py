from string_analyzer import count_and_sum_vowels

def test_standard_string():
    assert count_and_sum_vowels("Hello World") == (3, 324)

def test_no_matches_and_empty():
    assert count_and_sum_vowels("") == (0, 0)
    assert count_and_sum_vowels("bcdfg") == (0, 0)

def test_symbols_and_spaces():
    assert count_and_sum_vowels("1&***A^& e") == (2, 198)