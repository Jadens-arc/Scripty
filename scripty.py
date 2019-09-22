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
    saveAsBtn.place(relx = 0, rely = 0, relwidth=1.0, relheight = 0.2)

    saveAsEditor = Text(saveAsWin)
    saveAsEditor.place(relx = 0, rely = 0.2, relwidth=1.0, relheight = 0.8)

    with open('Config.json', 'r') as configFile:
        configFile = configFile.read()
        configFile = json.loads(configFile)
        saveAsBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])
        saveAsEditor.configure(background=configFile["bg-color"], foreground = configFile["font-color"], insertbackground=configFile["curser-color"])
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
    settingsWin.geometry("350x360")
    settingsWin.resizable(0,0)
    settingsWin.title("Settings")

    def saveSettings():
        with open('Config.json', 'w') as configFile:
            newSettings = settingsEditor.get('1.0', END)
            configFile.write(newSettings)
            messagebox.showinfo("WAIT", "Please reload to apply changes")

    saveSettingsBtn = Button(settingsWin, text = 'Save', command = lambda: saveSettings())
    saveSettingsBtn.place(relx = 0, rely = 0, relwidth = 1.0, relheight = 0.1)

    settingsEditor = Text(settingsWin)
    settingsEditor.place(relx = 0, rely = 0.1, relwidth = 1.0, relheight = 0.9)

    with open('Config.json', 'r') as configFile:
        configFile = configFile.read()
        settingsEditor.insert(INSERT, configFile)
    with open('Config.json', 'r') as configFile:
        configFile = json.loads(configFile.read())
        saveSettingsBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])
        settingsEditor.configure(background=configFile["bg-color"], foreground = configFile["font-color"], insertbackground=configFile["curser-color"])

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

with open('Config.json', 'r') as configFile:
    configFile = configFile.read()
    configFile = json.loads(configFile)
    editor.configure(background=configFile["bg-color"], foreground = configFile["font-color"], insertbackground=configFile["curser-color"])
    settingsBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])

    clearBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])

    saveAsBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])

    runBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])

    saveBtn.configure(background=configFile["bg-color"], foreground = configFile["font-color"])

window.mainloop()








