import os
from functions import get_todos, write_todos
import time
# todos = []
   
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True:
    
    
    action = input("\nType add, show, edit, clear, complete or exit: ").strip()
   
                
    if "add" in action or "new" in action or "more" in action:
        
        # todos.append(todo.title())
        # todo = action.replace("add","").strip()
        todo = action[4:]
        
        todos = get_todos()
        
        todos.append("\n"+todo.title().strip())
    
        write_todos(todos,'todo.txt')
    # else:
    #     todo = input("Enter a todo: ")+"\n"
            
        
    elif "show" in action:
        
        todos = get_todos()
        
        # for index,item in enumerate(todos):
        #     todos[index] = item.strip("\n")
        
        todos = [item.strip("\n") for item in todos]
        
        for i in range(len(todos)):
            if i =='':
                continue
            print(f"{i+1} - {todos[i]}")
            
    elif "display" in action:
        
        todos = get_todos('todo.txt')
        
        # for index,item in enumerate(todos):
        #     todos[index] = item.strip("\n")
        
        todos = [item.strip("\n") for item in todos]
        
        for i in range(len(todos)):
            print(f"{i+1} - {todos[i]}")
        
        
    elif "edit" in action:
        try:
            
            todos = get_todos('todo.txt')
            
            
            # num = int(input("Number of the todo to edit:"))
            num = int(action[5:])
            new_todo = input("Enter new todo: ")
            todos[num-1]=new_todo.title()+"\n"
            write_todos(todos)
            
        except ValueError:
            print("You command is not valid.")
            continue
        
    elif "complete" in action:
        
        try:
            # num = int(input("\nNumber of the todo to complete: "))
            num = int(action[len("complete"):])
            todos = get_todos('todo.txt')
            
            todos = [item for item in todos] 
                
            todos.pop(num-1)
            
            
            write_todos(todos)
                
        except IndexError:
            print("There is no item with that number.")
            continue
            
        
    elif "exit" in action:
        break
    
    elif "clear" in action:
        os.system("cls")
    
    else:
        print("Command is not valid.")
    
    # case _:
    #     print("Please just enter the command offered")
print("Bye!")
        
    