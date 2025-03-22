from functions import get_todolist, write_todolist
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo_list_item = user_action[4:]

        todo_list = get_todolist()

        todo_list.append(todo_list_item + "\n")

        write_todolist(todo_list_arg=todo_list, filepath="todo_list.txt",)

    elif user_action.startswith('show'):

        todo_list = get_todolist()

        for index, item in enumerate(todo_list):
            item = item.strip("\n")
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todo_list = get_todolist()

            updated_todolist_item = input("Enter the updated to do: ")
            todo_list[number] = updated_todolist_item + "\n"

            with open(filepath, "w") as file:
                file.writelines(todo_list)
        except ValueError:
            print("Your command isn't valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todo_list = get_todolist()

            index = number - 1
            todo_list_to_complete = todo_list[index].strip("\n")
            todo_list.pop(index)

            write_todolist(todo_list_arg=todo_list, filepath="todo_list.txt")

            message = f"to-list item: {todo_list_to_complete} has been completed and removed from the list."
            print(message)
        except IndexError:
            print(f"You only have {len(todo_list)} items in your to-do list")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Please enter valid input.")

print("Bye!")
