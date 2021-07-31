import PySimpleGUI as sg

class HumanPlayer:
    def __init__(self, symbol):
        sg.theme('DarkAmber')
        self.layout = [  [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
                [sg.Button('   '), sg.Button('   '), sg.Button('   ')],
                [sg.Button('   '), sg.Button('   '), sg.Button('   ')] ]
        self.window = sg.Window('Tic Tac Toe', self.layout)
    
    def getMove(self, game):
        event, values = self.window.read()
        if event == sg.WIN_CLOSED:
            return -1
        if(event == "   "):
            xVal = 0
            yVal = 0
        else:
            eventNum = int(event[3:4])
            getXVal = eventNum % 3
            if(getXVal == 2):
                xVal = 0
            if(getXVal == 0):
                xVal = 1
            if(getXVal == 1):
                xVal = 2
            if(eventNum < 2):
                yVal = 0
            elif(eventNum < 5):
                yVal = 1
            elif(eventNum < 8):
                yVal = 2
        returned = [yVal,xVal]
        return returned

    def reward(self, num):
        pass