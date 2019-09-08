
from tkinter import *
from tkinter import messagebox
import os

os.system('clear')

window = Tk()
window.geometry("550x350")
window.resizable(0,0)
window.title("Code With Jaden")
try:
    window.iconbitmap('favicon.ico')
except:
    pass
currDir = open('directory.txt', 'r')
for file in currDir:
    currDir = file
currDir = currDir[:-1]
currFile = open(str(currDir))

editor = Text(window, wrap = CHAR, width = 68)
for line in currFile:
    editor.insert(INSERT, line)
editor.grid(column = 0, row = 1, columnspan = 3)

def save():
    preSave = editor.get('1.0', END)
    file = open(str(currDir), "w")
    file.write(preSave)
    
def run():
    save()
    os.system('clear')
    result = os.system('python3 ' + str(currDir))
    
def cd():
    fileWindow = Tk()
    fileWindow.geometry("550x350")
    
    fileWindow.mainloop()

runBtn = Button(window, text = "Run", command = lambda: run())
runBtn.grid(column = 0, row = 0)

saveBtn = Button(window, text = "Save", command = lambda: save())
saveBtn.grid(column = 1, row = 0)

fileBtn = Button(window, text = "File", command = lambda: cd())
fileBtn.grid(column = 2, row = 0)

window.mainloop()
