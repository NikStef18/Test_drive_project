import pytest
from lib.check_sentence_grammar import *


"""
Given a valid sentence with a capital letter and a full stop.
Returns true
"""

def test_with_valid_sentence():
    result = check_sentence_grammar("Hello, this is a fine day.")
    assert result == True

"""
Given a sentence with a capital letter but no full stop or other mark.
Returns False 
"""
def test_capital_letter_but_no_ending_mark():
    result = check_sentence_grammar("Hello, this is a fine day")
    assert result == False


"""
Given a valid sentence with a capital letter and a question mark.
Returns true
"""
def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammar("Hello, this is a fine day?")
    assert result == True

"""
Given a valid sentence with a capital letter and an exclamation mark.
Returns true
"""
def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, this is a fine day!")
    assert result == True

"""
Given a sentence with a capital letter but ends in a comma.
Returns False 
"""
def test_with_capital_letter_and_comma():
    result = check_sentence_grammar("Hello, this is a fine day,")
    assert result == False

"""
Given a sentence with a capital letter but ends in a colon.
Returns False 
"""
def test_with_capital_letter_and_colon():
    result = check_sentence_grammar("Hello, this is a fine day:")
    assert result == False


"""
Given a sentence with no capital letter but a full stop.
Returns False 
"""
def test_with_lowercase_start_letter_and_full_stop():
    result = check_sentence_grammar("hello, this is a fine day.")
    assert result == False

"""
Given a sentence with an empty string
Raises an error.
"""

def test_with_empty_string():
    with pytest.raises(Exception) as e:
        check_sentence_grammar("") 
    error_message = str(e.value)
    assert error_message == "Cannot check grammar of empty string."

 

