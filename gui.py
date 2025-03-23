import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todolist(), key="todo_list",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-do List App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Arial', 14))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_todolist()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions.write_todolist(todo_list)
            window['todo_list'].update(values=todo_list)

        case "Edit":
            todo_to_edit = values['todo_list'][0]
            new_todo = values['todo']

            todo_list = functions.get_todolist()
            index = todo_list.index(todo_to_edit)
            todo_list[index] = new_todo + "\n"
            functions.write_todolist(todo_list)
            window['todo_list'].update(values=todo_list)
        case "todo_list":
            window['todo'].update(value=values['todo_list'][0])
        case sg.WIN_CLOSED:
            break


window.close()