import PySimpleGUI as sg

def main():
    sg.theme('DarkBlue17')

    layout = [[sg.InputText(visible=True, do_not_clear=False, justification='r',
                             size=(20,20), key='-S-', focus=True),
               sg.Button('Find out', size=(20, 2))],
              [sg.Button('Add item', size=(20, 2))],
              ]


    window = sg.Window('V-Belts', layout, size=(500, 400))

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()
