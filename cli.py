# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)
        todos.sort()

        functions.write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number-1] = new_todo + "\n"
            todos.sort()

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.\n")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todo_to_remove = todos[number-1].strip("\n")
            todos.pop(number-1)
            todos.sort()
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.\n")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered an unknown command!")
print("Bye!")