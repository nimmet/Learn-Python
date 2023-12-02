user_prompt = "Enter a todo: "

user_condition = True

while user_condition:
    user_action = input("Enter show, add, edit, complete or exit: ").strip()

    match user_action.capitalize():
        case "Show" | "Display":

            with open("../files/todos.txt", 'r') as file:
                todos = file.readlines()

            # todos = [t.replace("\n", "") for t in todos]

            for index, item in enumerate(todos):
                # item = item.replace("\n","")
                item = item.strip("\n")
                print(f"{index+1}-{item}")

        case "Add":
            todo = input(user_prompt)+"\n"

            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
                todos.append(todo.title())




            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)

        case "Exit" | "Q":
            user_condition = False
            print("Bye!")

        case "Edit":
            item_num = int(input("Number of the todo to edit: "))
            # todos.pop(item_num-1)


            new_todo = input("Enter a new todo: ")+"\n"
            todos[item_num-1] = new_todo.title()

            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)

            # if item_num > 0:
            #     todos.insert(item_num-1,new_todo.title())
            # elif item_num == 0:
            #     todos.insert(item_num, new_todo.title())
            # else:
            #     print("Invalid index, Index should be greate or equal to 0.")

        case "Complete":
            num = int(input("Number of the todo to complete: "))

            todo_to_remove = todos[num-1].strip("\n")
            todos.pop(num-1)
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)

            msg = f"Todo '{todo_to_remove}' was removed from the list."
            print(msg)

        case _:
            print("You entered an unknown command!")



