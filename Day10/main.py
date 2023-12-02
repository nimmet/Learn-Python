user_prompt = "Enter a todo: "

user_condition = True

while user_condition:
    user_action = input("Enter show, add, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action.title()[len("add")+1:].strip()

        with open("../files/todos.txt") as file:
            todos = file.readlines()

        todos.append(todo+"\n")

        with open("../files/todos.txt","w") as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open("../files/todos.txt") as file:
            todos = file.readlines()

        for index,todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1}-{todo}")

    elif user_action.startswith("edit"):

        try:

            edit_num = int(user_action.title().strip()[len("edit")+1:])



            with open("../files/todos.txt") as file:
                todos = file.readlines()


            new_todo = input("Enter a new todo: ")
            todos[edit_num-1] = new_todo.title()+"\n"

            with open("../files/todos.txt", "w") as file:
                    file.writelines(todos)

        except ValueError:
            print("You have to enter a number after Edit command!")

    elif user_action.startswith("complete"):
        try:
            complete_num = int(user_action.title()[len("Complete")+1:].strip())

            with open("../files/todos.txt") as file:
                todos = file.readlines()



            todo_to_remove = todos[complete_num-1].strip("\n")
            todos.pop(complete_num-1)

            msg = f"Todo '{todo_to_remove}' was removed from the list."
            print(msg)

            with open("../files/todos.txt", "w") as file:
                    file.writelines(todos)
        except IndexError:
            print("There is no item with that index.")



    elif user_action.startswith("exit") or user_action == 'q':
        user_condition = False

    else:
        print("You entered an unknown command!")

print("Bye!")

