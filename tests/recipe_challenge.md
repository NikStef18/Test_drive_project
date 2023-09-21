1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

I will add semi-colon after to do: in order to know that this is the task the user needs to complete(compared to other info saved)

2. Design the Function Signature

Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE
'''
python

def check_for_todo_strings():
# Parameters:
#   text: a string contains phrase # TO DO
# Returns: 
#   Boolean: true, if there is, otherwise false
'''

3. Create Examples as Tests

Make a list of examples of what the function will take and return.

'''
python

"""
Given a valid task with a phrase "todo" and followed by semi-colon and a string.
Returns true
"""
check_for_todo_strings("to do: the dishes")
# => True




"""
Given a task with no phrase to do.
Returns false
"""
check_for_todo_strings("the dishes")
# => False

"""
Given a task with other letter or numbers between to ...do
Returns false
"""
check_for_todo_strings("Tohsg536do: Take dog to the vet")
# => False


"""
Given a task with an empty string
Raises an error.
"""
check_for_todo_strings("")
# Raises "No tasks for today"

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

