from lib.count_words import *

"""
A function called count_words 
that takes a string as an argument 
and returns the number of words in that string.
"""

'''
If string is empty,
it returns 0
'''
def test_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

'''
If one word is added,
it returns 1.
'''
def test_given_one_string_returns_number_1():
    result = count_words("house")
    assert result == 1

'''
If 5 words are added,
it returns 5.
'''
def test_given_five_strings_returns_number_5():
    result = count_words("house, pet, bag, phone, glasses")
    assert result == 5

def test_multiple_spaces_between_words():
    result = count_words("   This    is   a    test   ")
    assert result == 4

def test_punctuation():
    result = count_words("Hello, world! This is a test.")
    assert result == 6

def test_unicode_characters():
    result = count_words("Résumé, café, and coördinate are words.")
    assert result == 6
    
def test_mix_of_alphanumeric_and_symbols():
    result = count_words("word123!@#")
    assert result == 1