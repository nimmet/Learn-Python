user_prompt = "Type add, show or exit: "

todos = []

decition = True

while decition:
    user_action = input(user_prompt)

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())

        case "show" | "display":
            for item in todos:
                print(item)

        case "exit" | "q":
            decition = False

        case _:
            print("You entered an unknown command!")

print("Bye!")