# An open-source IDE for python and java
# By Jaden Arceneaux arceneauxJaden@gmail.com
# Feel free to change code as you feel

from tkinter import *
from tkinter import messagebox
import os
import subprocess
from subprocess import STDOUT, PIPE
import json
import sys

os.system('clear')

window = Tk()
window.geometry("550x350")

fileLine = str(sys.argv[-1])

try:
    currFile = open(str(fileLine))
except:
    newFile = open(str(fileLine), "w")
    newFile.close()
    currFile = open(str(fileLine))
editor = Text(window, wrap = CHAR)
for line in currFile:
    editor.insert(INSERT, line)
editor.place(rely = 0.07, relx = 0, relheight = 0.93, relwidth = 1.0)

window.title(str(fileLine))

def compile_java(java_file):
    cmd = 'javac ' + java_file
    proc = subprocess.Popen(cmd, shell=True)

def execute_java (java_file):
    cmd=['java', java_file]
    proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT)
    input = subprocess.Popen(cmd, stdin = PIPE)
    print(proc.stdout.read())

def save():
    file = open(str(fileLine), "w")
    file.write(editor.get('1.0', END))
    file.close()

def saveAs():
    saveAsWin = Tk()
    saveAsWin.geometry("550x125")
    saveAsWin.resizable(0,0)
    saveAsWin.title("Save As")

    def saveName():
        saveAsLoca = saveAsEditor.get('1.0', END)
        file = open(saveAsLoca[:-1], 'w')
        file.write(editor.get('1.0', END))

        fileLine = saveAsLoca[:-1]

        window.title(saveAsEditor.get('1.0', END)[:-1])

        file.close()

    saveAsBtn = Button(saveAsWin, text = "Save", command = lambda: saveName())
    saveAsBtn.pack()

    saveAsEditor = Text(saveAsWin)
    saveAsEditor.pack()

    saveAsWin.mainloop()

def run():
    save()
    os.system('clear')
    if '.py' in fileLine:
        os.system('python3 ' + str(fileLine))
    elif '.java' in fileLine:
        compile_java(str(fileLine))
        execute_java(str(fileLine[:-5]))
def clear():
    os.system('clear')

def settings():
    settingsWin = Tk()
    settingsWin.geometry("350x560")
    settingsWin.resizable(0,0)
    settingsWin.title("Settings")
    settingsWin.mainloop()

runBtn = Button(window, text = "Run", command = lambda: run())
runBtn.place(relx = 0, rely = 0, relwidth = 0.225, relheight = 0.07)

saveBtn = Button(window, text = "Save", command = lambda: save())
saveBtn.place(relx = 0.225, rely = 0, relwidth = 0.225, relheight = 0.07)

saveAsBtn = Button(window, text = "Save As", command = lambda: saveAs())
saveAsBtn.place(relx = 0.450, rely = 0, relwidth = 0.225, relheight = 0.07)

clearBtn = Button(window, text = "Clear", command = lambda: clear())
clearBtn.place(relx = 0.675, rely = 0, relwidth = 0.225, relheight = 0.07)

settingsBtn = Button(window, text = "⚙", command = lambda: settings())
settingsBtn.place(relx = 0.90, rely = 0, relwidth = 0.1, relheight = 0.07)

window.mainloop()












