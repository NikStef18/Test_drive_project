def check_for_todo_strings(task):
    correct_task = task.replace(" ", "").lower()
    if correct_task == "todo:":
        raise Exception("No tasks for today")
    return True if 'todo:' in correct_task else False
    
    # if words and words[0] == 'todo:':
    #     return True
    # else:
    #     return False
    
   
        
