from Functions.functions import *
import time

user_prompt = "Enter a todo: "

user_condition = True

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is "+now)

while user_condition:
    user_action = input("Enter show, add, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action.title()[len("add")+1:].strip()

        todos = get_todos()

        todos.append(todo+"\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index,todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1}-{todo}")

    elif user_action.startswith("edit"):

        try:

            edit_num = int(user_action.title().strip()[len("edit")+1:])
            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[edit_num-1] = new_todo.title()+"\n"

            write_todos(todos)

        except ValueError:
            print("You have to enter a number after Edit command!")

    elif user_action.startswith("complete"):
        try:
            complete_num = int(user_action.title()[len("Complete")+1:].strip())

            todos = get_todos()

            todo_to_remove = todos[complete_num-1].strip("\n")
            todos.pop(complete_num-1)

            msg = f"Todo '{todo_to_remove}' was removed from the list."
            print(msg)

            write_todos(todos)

        except IndexError:
            print("There is no item with that index.")



    elif user_action.startswith("exit") or user_action == 'q':
        user_condition = False

    else:
        print("You entered an unknown command!")

print("Bye!")

