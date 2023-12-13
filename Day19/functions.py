def get_todos(filepath="files/todos.txt"):
    with open(filepath) as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath="files/todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos)
