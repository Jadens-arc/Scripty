# By Jaden Arceneaux arceneauxJaden@gmail.com
from tkinter import *
from tkinter import messagebox
import os
import subprocess
from subprocess import STDOUT, PIPE

os.system('clear')

window = Tk()
window.geometry("550x350")
currDir = open('directory.txt', 'r')
lineList = []
for file in currDir:
    lineList.append(file)
fileLine = lineList[0]
try:
    currFile = open(str(fileLine[:-1]))
except:
    newFile = open(str(fileLine[:-1]), "w")
    newFile.close()
    currFile = open(str(fileLine[:-1]))
editor = Text(window, wrap = CHAR)
for line in currFile:
    editor.insert(INSERT, line)
editor.place(rely = 0.07, relx = 0, relheight = 0.93, relwidth = 1.0)

window.title(str(fileLine[:-1]))

def compile_java(java_file):
    cmd = 'javac ' + java_file
    proc = subprocess.Popen(cmd, shell=True)

def execute_java (java_file):
    cmd=['java', java_file]
    proc=subprocess.Popen(cmd, stdout = PIPE, stderr = STDOUT)
    input = subprocess.Popen(cmd, stdin = PIPE)
    print(proc.stdout.read())

def save():
    file = open(str(fileLine[:-1]), "w")
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

        dirFileSave = open("directory.txt", "w")
        dirFileSave.write(saveAsEditor.get('1.0', END) + '\n')

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
        os.system('python3 ' + str(fileLine[:-1]))
    elif '.java' in fileLine:
        compile_java(str(fileLine[:-1]))
        execute_java(str(fileLine[:-6]))
def cd():
    os.system('ls')

    fileWindow = Tk()
    fileWindow.geometry("550x125")
    fileWindow.resizable(0,0)
    fileWindow.title("Change Working File")

    dirSaveBtn = Button(fileWindow, text = "Save", command = lambda: saveDir())
    dirSaveBtn.pack()

    dirEditor = Text(fileWindow)
    dirEditor.pack()

    def saveDir():
        messagebox.showinfo("wait", "please reload to apply changes")
        dirFileSave = open("directory.txt", "w")
        dirFileSave.write(dirEditor.get('1.0', END) + '\n')

    currDir = open('directory.txt', 'r')
    for file in currDir:
        dirEditor.insert(INSERT, file)

    fileWindow.mainloop()

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

fileBtn = Button(window, text = "File", command = lambda: cd())
fileBtn.place(relx = 0.675, rely = 0, relwidth = 0.225, relheight = 0.07)

settingsBtn = Button(window, text = "⚙️", command = lambda: settings())
settingsBtn.place(relx = 0.90, rely = 0, relwidth = 0.1, relheight = 0.07)

window.mainloop()







