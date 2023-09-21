1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

We'll ignore any intermediate sentences.

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE
'''
python

def check_sentence_grammar():
    # Parameters:
    #   text: a string representing human-readable text
    # Returns:
    #   Boolean, True if valid, False otherwise
'''


3. Create Examples as Tests

Make a list of examples of what the function will take and return.

'''
python

"""
Given a valid sentence with a capital letter and full stop.
Returns true
"""
check_sentence_grammar("Hello, this is a fine day.")
# => True

"""
Given a valid sentence with a capital letter and a question mark.
Returns true
"""
check_sentence_grammar("Hello, this is a fine day?")
# => True


"""
Given a valid sentence with a capital letter and an exclamation mark.
Returns true
"""
check_sentence_grammar("Hello, this is a fine day!")
# => True


"""
Given a sentence with a capital letter but no full stop or other mark.
Returns False 
"""
check_sentence_grammar("Hello, this is a fine day")
 # => False

"""
Given a sentence with no capital letter but a full stop.
Returns False 
"""
check_sentence_grammar("hello, this is a fine day.")
# => False

"""
Given a sentence with a capital letter but ends in a comma.
Returns False 
"""
check_sentence_grammar("Hello, this is a fine day,")
# => False

"""
Given a sentence with a capital letter but ends in a colon.
Returns False 
"""
check_sentence_grammar("Hello, this is a fine day:")
# => False

"""
Given a sentence with an empty string
Raises an error.
"""
check_sentence_grammar("")
# Raises "Cannot check grammar of empty string.

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

