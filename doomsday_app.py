import PySimpleGUI as sg 
from doomsday_calc import CalculateDayOfWeek
from datetime import datetime
import dateutil.parser as parser


def main():
    window = render()

    while True: 
        event, values = window.read() 
        if event == 'Calculate Day':
            inputText = values['-IN-']
            try:
                toDisplay = getResult(inputText)
            except Exception as exc:
                toDisplay = format(exc)
            window['-DISPLAY-'].update(toDisplay)
            
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      

    window.close()

def render():
    layout = [[sg.Text('Enter Date:'), sg.Input(key='-IN-')],
            [sg.Text(key='-DISPLAY-')],  
            [sg.Button('Calculate Day'), sg.Exit()]]      

    return sg.Window('Doomsday Algorithm Demo', layout)   

def getResult(dateText):
    date = parser.parse(dateText)
    return CalculateDayOfWeek(date.month, date.day, date.year)

main()
