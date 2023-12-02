user_prompt = "Enter a todo: "

user_condition = True

while user_condition:
    user_action = input("Enter show, add, edit, complete or exit: ").strip()

    match user_action.capitalize():
        case "Show" | "Display":

            file = open("../files/todos.txt", 'r')
            todos = file.readlines()
            file.close()

            # todos = [t.replace("\n", "") for t in todos]

            for index, item in enumerate(todos):
                # item = item.replace("\n","")
                item = item.strip("\n")
                print(f"{index+1}-{item}")

        case "Add":
            todo = input(user_prompt)+"\n"

            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(todo.title())




            file = open("../files/todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "Exit" | "Q":
            user_condition = False
            print("Bye!")

        case "Edit":
            item_num = int(input("Number of the todo to edit: "))
            # todos.pop(item_num-1)


            new_todo = input("Enter a new todo: ")+"\n"

            file = open("../files/todos.txt", "w")
            todos[item_num-1] = new_todo.title()
            file.writelines(todos)
            file.close()
            # if item_num > 0:
            #     todos.insert(item_num-1,new_todo.title())
            # elif item_num == 0:
            #     todos.insert(item_num, new_todo.title())
            # else:
            #     print("Invalid index, Index should be greate or equal to 0.")

        case "Complete":
            num = int(input("Number of the todo to complete: "))

            file = open("../files/todos.txt", "w")
            todos.pop(num-1)
            file.writelines(todos)
            file.close()

        case _:
            print("You entered an unknown command!")



