user_prompt = "Enter a todo: "
todos = []
user_condition = True

while user_condition:
    user_action = input("Enter show, add, edit or exit: ")
    match user_action.capitalize():
        case "Show" | "Display":
            for item in todos:
                print(item)
        case "Add":
            todo = input(user_prompt)
            todos.append(todo.title())
        case "Exit" | "Q":
            user_condition = False
            print("Bye!")

        case "Edit":
            item_num = int(input("Number of the todo to edit: "))
            # todos.pop(item_num-1)
            new_todo = input("Enter a new todo: ")
            todos[item_num-1] = new_todo.title()
            # if item_num > 0:
            #     todos.insert(item_num-1,new_todo.title())
            # elif item_num == 0:
            #     todos.insert(item_num, new_todo.title())
            # else:
            #     print("Invalid index, Index should be greate or equal to 0.")


        case _:
            print("You entered an unknown command!")



