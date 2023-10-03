from Functions.StartProgram import StartProgram
from Screen.MainScreen import MainScreen

from Screen.Settings import Settings

if __name__=="__main__":
    program = StartProgram()
    program.start()
    
    MainScreen(program)