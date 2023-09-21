import pytest
from lib.check_for_todo_strings import *


"""
Given a valid task with a phrase "To do" and followed by semi-colon. 
Returns true
"""
def test_todo_and_semi_colon_and_a_string():
    result = check_for_todo_strings("todo: the dishes")
    assert result == True

"""
Given a task with no phrase to do.
Returns false
"""
def test_without_todo_and_semi_colon_but_only_a_string():
    result = check_for_todo_strings("the dishes")
    assert result == False

"""
Given a task with other letters or numbers between to...do
Returns false
"""
def test_with_letters_and_numbers_between_to_and_do():
    result = check_for_todo_strings("Tohsg536do: the dishes")
    assert result == False

"""
Given a task with an empty string
Raises an error.
"""
def test_with_empty_string_after_todo():
    with pytest.raises(Exception) as e:
        check_for_todo_strings("todo:")
    error_message = str(e.value)    
    assert error_message == "No tasks for today"





