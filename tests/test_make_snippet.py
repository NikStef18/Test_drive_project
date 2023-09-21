from lib.make_snippet import make_snippet

'''
A function called make_snippet that 
takes a string as an argument 
and returns the first five words 
and then a '...' if there are more 
than that.
'''

'''
If given an empty string,
it returns an empty string.
'''
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

"""
Given a string of four words,
it returns the same string
"""
def test_string_of_four_words_returns_same_string():
    result = make_snippet("Fly me to the")
    assert result == "Fly me to the"

'''
Given a string of five words,
it returns the same string.
'''
def test_string_of_five_words_returns_same_string():
    result = make_snippet("Fly me to the moon")
    assert result == "Fly me to the moon"
'''
Given a string of 10 words,
it returns the first five words and "...".
'''
def test_string_of_more_than_five_words_returns_five_word_string_ellipsis():
    result = make_snippet("Fly me to the moon let me play along the") 
    assert result == "Fly me to the moon..."