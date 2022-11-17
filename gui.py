import PySimpleGUI as sg
import generator as gen

layout = [  [sg.Text("Please select the number of keys you'd like to generate.")],
            [sg.InputText()],
            [sg.Button('Continue'), sg.Button('Exit')]]

window = sg.Window(title="Password Generator", layout = layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print('inside continue event')
    print(values[0])
    layout = []
    for x in range(int(values[0])):
        layout.append([sg.Text(gen.generate_passowrd())])
    layout.append([sg.Button('Exit')])
    window.close()
    window = sg.Window(title="Password Generator", layout = layout)

window.close()