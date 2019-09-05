from tkinter import *
from tkinter import messagebox
import os

window = Tk()
window.geometry("550x350")
window.resizable(0,0)
currFile = 'file.py'

editor = Text(window)
with open("file.py") as file:
        for line in file:
            editor.insert(INSERT, line)
editor.grid(column = 0, row = 1, columnspan = 4)
def save():
        preSave = editor.get('1.0', END)
        file = open("file.py", "w")
        file.write(preSave)
def run():
	save()
	result = os.system('python3 ' + currFile)
	#resultWindow = Tk()
	#resultWindow.geometry("550x350")
	#resultWindow.resizable(0,0)
	#resultText = Text(resultWindow)
	#for line in result:
        #    resultText.insert(INSERT, line)
	#resultText.grid(column = 0, row = 0)
	#resultWindow.mainloop()


runBtn = Button(window, text = "Run", command = lambda: run())
runBtn.grid(column = 0, row = 0)

saveBtn = Button(window, text = "Save", command = lambda: save())
saveBtn.grid(column = 1, row = 0)

window.mainloop()
