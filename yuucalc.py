import PySimpleGUIQt as sg


def main():
    sg.theme("Dark")

    FSIZE = [
        [
            sg.Radio("MB", "-SIZE-", key="-MB-"),
            sg.Radio("GB", "-SIZE-", default=True, key="-GB-"),
        ],
        [sg.InputText(key="-SIZE-")],
    ]

    ISPEED = [
        [
            sg.Radio("KB/s", "-SPEED-", key="-KBs-"),
            sg.Radio("Mbit/s", "-SPEED-", key="-Mbs-"),
            sg.Radio("MB/s", "-SPEED-", default=True, key="-MBs-"),
        ],
        [sg.InputText(key="-SPEED-")],
    ]

    layout = [
        [sg.Frame("File Size", FSIZE)],
        [sg.Frame("Internet Speed", ISPEED)],
        [sg.Button("Submit"), sg.Text("(H:M:S):"), sg.Text(key="-TIME-")],
    ]

    window = sg.Window(
        "yuuCalc",
        layout,
        resizable=False,
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        try:
            if event == "Submit":
                if values["-SIZE-"]:
                    if values["-MB-"]:
                        size = float(values["-SIZE-"]) / 1000
                    elif values["-GB-"]:
                        size = float(values["-SIZE-"])
                if values["-SPEED-"]:
                    if values["-KBs-"]:
                        speed = float(values["-SPEED-"]) / 125
                    elif values["-Mbs-"]:
                        speed = float(values["-SPEED-"])
                    elif values["-MBs-"]:
                        speed = float(values["-SPEED-"]) * 8
                seconds = 8192 / (speed * 1024) * (size * 1024) * 1.05
                time = (
                    str(int(seconds / 3600))
                    + ":"
                    + str(int(seconds / 60 % 60))
                    + ":"
                    + str(int(seconds % 60))
                )
                window["-TIME-"].update(time)
        except Exception as e:
            sg.Popup(str(e))


if __name__ == "__main__":
    main()
