user_prompt = "Enter a todo: "

user_condition = True

while user_condition:
    user_action = input("Enter show, add, edit, complete or exit: ").strip()

    if "Add" in user_action.title():
        todo = user_action.title()[len("add")+1:].strip()

        with open("../files/todos.txt") as file:
            todos = file.readlines()

        todos.append(todo+"\n")

        with open("../files/todos.txt","w") as file:
            file.writelines(todos)
    elif "Show" in user_action.title():
        with open("../files/todos.txt") as file:
            todos = file.readlines()

        for index,todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1}-{todo}")

    elif "Edit" in user_action.title():
        edit_num = int(user_action.title().strip()[len("edit")+1:])

        with open("../files/todos.txt") as file:
            todos = file.readlines()


        new_todo = input("Enter a new todo: ")
        todos[edit_num-1] = new_todo.title()+"\n"

        with open("../files/todos.txt", "w") as file:
                file.writelines(todos)


    elif "Complete" in user_action.title():
        complete_num = int(user_action.title()[len("Complete")+1:].strip())

        with open("../files/todos.txt") as file:
            todos = file.readlines()



        todo_to_remove = todos[complete_num-1].strip("\n")
        todos.pop(complete_num-1)

        msg = f"Todo '{todo_to_remove}' was removed from the list."
        print(msg)

        with open("../files/todos.txt", "w") as file:
                file.writelines(todos)




    elif "Exit" in user_action.title() or "Q" in user_action.title():
        user_condition = False

    else:
        print("You entered an unknown command!")

print("Bye!")





    # match user_action.capitalize():
    #     case "Show" | "Display":
    #
    #
    #         with open("../files/todos.txt", 'r') as file:
    #             todos = file.readlines()
    #
    #         # todos = [t.replace("\n", "") for t in todos]
    #
    #         for index, item in enumerate(todos):
    #             # item = item.replace("\n","")
    #             item = item.strip("\n")
    #             print(f"{index+1}-{item}")
    #
    #     case "Add":
    #
    #         todo = input(user_prompt)+"\n"
    #
    #         with open("../files/todos.txt", "r") as file:
    #             todos = file.readlines()
    #             todos.append(todo.title())
    #
    #
    #
    #
    #         with open("../files/todos.txt", "w") as file:
    #             file.writelines(todos)
    #
    #     case "Exit" | "Q":
    #         user_condition = False
    #         print("Bye!")
    #
    #     case "Edit":
    #         item_num = int(input("Number of the todo to edit: "))
    #         # todos.pop(item_num-1)
    #
    #
    #         new_todo = input("Enter a new todo: ")+"\n"
    #         todos[item_num-1] = new_todo.title()
    #
    #         with open("../files/todos.txt", "w") as file:
    #             file.writelines(todos)
    #
    #         # if item_num > 0:
    #         #     todos.insert(item_num-1,new_todo.title())
    #         # elif item_num == 0:
    #         #     todos.insert(item_num, new_todo.title())
    #         # else:
    #         #     print("Invalid index, Index should be greate or equal to 0.")
    #
    #     case "Complete":
    #         num = int(input("Number of the todo to complete: "))
    #
    #         todo_to_remove = todos[num-1].strip("\n")
    #         todos.pop(num-1)
    #         with open("../files/todos.txt", "w") as file:
    #             file.writelines(todos)
    #
    #         msg = f"Todo '{todo_to_remove}' was removed from the list."
    #         print(msg)
    #
    #     case _:
    #         print("You entered an unknown command!")
    #
    #
    #
