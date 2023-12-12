def get_todos(filename="todos.txt"):
    """read data from a file and return as a list"""
    with open(filename, 'r') as file:
            todos = file.readlines()    
    return todos

def write_todos(todos_arg,filename="todos.txt") :
    with open(filename, 'w') as file:
            file.writelines(todos_arg)
            

    