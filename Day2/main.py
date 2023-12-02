
msg = "Enter a todo: "

condition = True

todos = []

while condition:
    todo = input(msg)
    todos.append(todo.capitalize())

    if todo == "exit":
        condition = False

    print(todos)
