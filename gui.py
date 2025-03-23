import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-do List App",
                   layout=[[label], [input_box, add_button]],
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
        case sg.WIN_CLOSED:
            break


window.close()