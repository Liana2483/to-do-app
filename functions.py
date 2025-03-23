FILEPATH = "todo_list.txt"


def get_todolist(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do list items.
    """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todolist(todo_list_arg, filepath=FILEPATH):
    """ Write the to-do list item to the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todo_list_arg)


if __name__ == "__main__":
    print("oy mate")