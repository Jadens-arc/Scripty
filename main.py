# By Jaden Arceneaux arceneauxJaden@gmail.com
from tkinter import *
from tkinter import messagebox
import os
import subprocess
from subprocess import STDOUT, PIPE

os.system('clear')

window = Tk()
window.geometry("550x350")
window.title("Code With Jaden") 
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
editor.place(rely = 0.1, relx = 0, relheight = 0.9, relwidth = 1.0)

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

def run():
    save()
    os.system('clear')
    if '.py' in fileLine:
        os.system('python3 ' + str(fileLine[:-1]))
    elif '.java' in fileLine:
        compile_java(str(fileLine[:-1]))
        execute_java(str(fileLine[:-6]))
def cd():
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
        dirFileSave.write(dirEditor.get('1.0', END))

    currDir = open('directory.txt', 'r')
    for file in currDir:
        dirEditor.insert(INSERT, file)

    fileWindow.mainloop()

runBtn = Button(window, text = "Run", command = lambda: run())
runBtn.place(relx = 0, rely = 0, relwidth = 0.333, relheight = 0.1)

saveBtn = Button(window, text = "Save", command = lambda: save())
saveBtn.place(relx = 0.333, rely = 0, relwidth = 0.333, relheight = 0.1)

fileBtn = Button(window, text = "File", command = lambda: cd())
fileBtn.place(relx = 0.666, rely = 0, relwidth = 0.333, relheight = 0.1)

window.mainloop()

