from tkinter import *
from tkinter import messagebox
import time
'''
By Jaden Arceneaux
arceneauxjaden@gmail.com
(c) CC BY-SA
'''
def sortGames(mainMenuWin):
    gameFileA = open("games.txt", "r")
    gameList = []
    for line in gameFileA:
        gameList.append(line)
    gameList.sort()
    gameFileA.close()

    gameFileB = open("games.txt", "w")
    gameFileB.write('')
    gameFileB.close()

    gameFileC = open("games.txt", "a")
    for game in gameList:
        gameFileC.write(game)


    mainMenuWin.destroy()
    mainMenu()

def clearGames(mainMenuWin):
    gameFile = open("games.txt", "w")
    gameFile.write('')
    gameFile.close()
    mainMenuWin.destroy()
    mainMenu()

def addGame(mainMenuWin):
    def gameWrite():
        # name, price, downloaded, consoles
        gameFile = open("games.txt", "a")
        newGameName = gameNameEnt.get()
        newGamePrice = gamePriceEnt.get()
        newGameConsole = gameConsoleEnt.get()
        if newGameName != '' and newGamePrice != '' and newGameConsole != '':
            if CheckVar1.get() == 0:
                gameFile.write('{}, {}, No, {}\n'.format(newGameName, newGamePrice, newGameConsole))
            else:
                gameFile.write('{}, {}, Yes, {}\n'.format(newGameName, newGamePrice, newGameConsole))
            gameFile.close()
            addGameWin.destroy()
            mainMenu()
        else:
            messagebox.showwarning("Warning","Please Fill In All Boxes")
        
    mainMenuWin.destroy()

    addGameWin = Tk()
    addGameWin.title("Add Game")
    addGameWin.geometry('200x130')



    CheckVar1 = IntVar()

    gameNameLbl = Label(addGameWin, text="Name: ")
    gameNameLbl.grid(column=0, row=0)
    gameNameEnt = Entry(addGameWin,width=10)
    gameNameEnt.grid(column=1, row=0)

    gamePriceLbl = Label(addGameWin, text="Price: ")
    gamePriceLbl.grid(column=0, row=1)
    gamePriceEnt = Entry(addGameWin,width=10)
    gamePriceEnt.grid(column=1, row=1)

    gameConsoleLbl = Label(addGameWin, text="Device: ")
    gameConsoleLbl.grid(column=0, row=2)
    gameConsoleEnt = Entry(addGameWin,width=10)
    gameConsoleEnt.grid(column=1, row=2)

    gameDownloadedLbl = Label(addGameWin, text="Downloaded: ")
    gameDownloadedLbl.grid(column=0, row=3)
    gameDownloadedCheck = Checkbutton(addGameWin, variable = CheckVar1, onvalue = 1, offvalue = 0)
    gameDownloadedCheck.grid(column=1, row=3)



    btn = Button(addGameWin, text="Done!", command = lambda: gameWrite())
    btn.grid(column=1, row=5)

    addGameWin.mainloop()
    
    try:
        addGameWin.protocol("WM_DELETE_WINDOW", mainMenu())
    except:
        pass

def mainMenu():

    mainMenuWin = Tk()
    mainMenuWin.title("Games")
    mainMenuWin.geometry('550x350')
    mainMenuWin.resizable(0,0)


    addGameBtn = Button(mainMenuWin, text="+", command = lambda:addGame(mainMenuWin))
    addGameBtn.grid(column=0, row=0)

    clearGameBtn = Button(mainMenuWin, text="x", command = lambda:clearGames(mainMenuWin))
    clearGameBtn.grid(column=1, row=0)

    gamesList = Text(mainMenuWin)

    with open("games.txt") as gameFile:
        for line in gameFile:
            gamesList.insert(INSERT, line)


    gamesList.config(state=DISABLED)
    gamesList.grid(column = 0, row = 1, columnspan = 4)

    mainMenuWin.mainloop()

mainMenu()


