import PySimpleGUIQt as Sg


def main():
    Sg.theme('Dark')

    FSIZE = [
        [
            Sg.Radio('MB', '-SIZE-', key='-MB-'),
            Sg.Radio('GB', '-SIZE-', default=True, key='-GB-'),
        ],
        [Sg.InputText(key='-SIZE-')],
    ]

    ISPEED = [
        [
            Sg.Radio('KB/s', '-SPEED-', key='-KBs-'),
            Sg.Radio('Mbit/s', '-SPEED-', key='-Mbs-'),
            Sg.Radio('MB/s', '-SPEED-', default=True, key='-MBs-'),
        ],
        [Sg.InputText(key='-SPEED-')],
    ]

    layout = [
        [Sg.Frame('File Size', FSIZE)],
        [Sg.Frame('Internet Speed', ISPEED)],
        [Sg.Button('Submit'), Sg.Text('(H:M:S):'), Sg.Text(key='-TIME-')]
    ]

    window = Sg.Window(
        'yuuCalc',
        layout,
        resizable=False,
    )

    while True:
        event, values = window.read()
        print(event, values)
        if event == Sg.WIN_CLOSED:
            break
        if event == 'Submit':
            if values['-SIZE-']:
                if values['-MB-']:
                    size = float(values['-SIZE-']) / 1000
                elif values['-GB-']:
                    size = float(values['-SIZE-'])
            if values['-SPEED-']:
                if values['-KBs-']:
                    speed = float(values['-SPEED-']) / 125
                elif values['-Mbs-']:
                    speed = float(values['-SPEED-'])
                elif values['-MBs-']:
                    speed = float(values['-SPEED-']) * 8
            seconds = 8192 / (speed * 1024) * (size * 1024) * 1.05
            time = (
                str(int(seconds / 3600))
                + ':'
                + str(int(seconds / 60 % 60))
                + ':'
                + str(int(seconds % 60))
            )
            window['-TIME-'].update(time)


if __name__ == '__main__':
    main()
