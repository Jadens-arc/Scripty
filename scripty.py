# An open-source IDE for python, java, and C++
# By Jaden Arceneaux arceneauxJaden@gmail.com
# Feel free to change code as you feel
try:
    from tkinter import *
    from tkinter import messagebox
except:
    os.system('sudo apt-get install python3-tk')
    from tkinter import *
    from tkinter import messagebox
# Checks if tkinter is installed
# if not then installs it
# used for UI

import sys
import os
# For running commands in the terminal ^

import json
# For parsing json files ^

import time

import threading
# For running multiple tasks on the CPU ^


appAlive = True
# This keeps track of whether the app is still open 
# Used for killing threads


defaultConfigFile = open('Settings/DefaultConfig.json')
defaultConfigFile = defaultConfigFile.read()
defaultConfigFile = json.loads(defaultConfigFile)
# This opens and parses the defaut config file 


configFile = open('Settings/Config.json')
configFile = configFile.read()
try:
    configFile = json.loads(configFile)
except:
    configFile = defaultConfigFile
# This attemts to open the user config file; if json error is 
# thrown opens default file



os.system('clear')
# ^ clears the terminal at the start of the program

window = Tk()
window.geometry("550x350")
# ^ declared window and sets size (in pixels)

fileLine = str(sys.argv[-1])
window.title(str(fileLine))
# ^  find the arument for which file to edit in the terminal
# and sets it as the title of the window


try:
    currFile = open(str(fileLine))
except:
    newFile = open(str(fileLine), "w")
    newFile.close()
    currFile = open(str(fileLine))
# This tests to see if the file the user inputed exists other wise it will create a new one


if configFile['line-wrap'] == True:
    if configFile['line-wrap-type'] == 'CHAR':
        editor = Text(window, wrap = CHAR)
    elif configFile['line-wrap-type'] == 'WORD':
        editor = Text(window, wrap = WORD)
    else:
        editor = Text(window, wrap = CHAR)
    for line in currFile:
        editor.insert(INSERT, line)
    editor.place(rely = 0.07, relx = 0, relheight = 0.93, relwidth = 1.0)
else:
    scrollbar = Scrollbar(window, orient=HORIZONTAL, background = configFile['bg-color'])
    scrollbar.place(relx = 0, rely = 0.95, relheight = 0.05)

    editor = Text(window, wrap = NONE)
    editor.config(yscrollcommand=scrollbar.set)

    scrollbar.config(command=editor.xview)

    for line in currFile:
        editor.insert(INSERT, line)

    editor.place(rely = 0.07, relx = 0, relheight = 0.88, relwidth = 1.0)


def save():
    global appAlive
    try:
        user = editor.get('1.0', END)
        file = open(str(fileLine), "w")
        file.write(user)
        file.close()
    except:
        appAlive = False

def saveShortCut(arg):
    save()
    # This function save the current file along with its changes

def saveAs():
    saveAsWin = Tk()
    saveAsWin.geometry("550x125")
    saveAsWin.resizable(0,0)
    saveAsWin.title("Save As")
    # This declares the save as window and its fixed size
    def saveName():
        saveAsLoca = saveAsEditor.get('1.0', END)
        file = open(saveAsLoca[:-1], 'w')
        file.write(editor.get('1.0', END))
        fileLine = saveAsLoca[:-1]
        window.title(saveAsEditor.get('1.0', END)[:-1])
        file.close()
        # This function saves the location of the file the user inputed

    saveAsBtn = Button(saveAsWin, text = "Save", command = lambda: saveName())
    saveAsBtn.place(relx = 0, rely = 0, relwidth=1.0, relheight = 0.2)

    saveAsEditor = Text(saveAsWin)
    saveAsEditor.place(relx = 0, rely = 0.2, relwidth=1.0, relheight = 0.8)

    def tab(arg):
        saveAsEditor.insert(INSERT, " " * configFile["python-indent-spacing"])
        return 'break'
        

    saveAsEditor.bind("<Tab>", tab)
    saveAsBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)
    saveAsEditor.configure(background=configFile["bg-color"], foreground = configFile["font-color"])
    saveAsEditor.configure(insertbackground=configFile["curser-color"], highlightthickness = 0, bd = 0)
    saveAsWin.mainloop()

def executeCode():
    save()
    os.system('clear')
    if '.py' in fileLine:
        os.system('python3 ' + str(fileLine))
    elif '.java' in fileLine:
        os.system('javac ' + str(fileLine))
        os.system('java ' + fileLine[:-5])
    elif '.cpp' in fileLine:
        os.system('g++ ' + str(fileLine) + ' -o ' + fileLine[:-4])
        os.system('./' + fileLine[:-4])
    elif '.cs' in fileLine:
        os.system('dotnet run ' + fileLine)

def enableEditor():
    editor.configure(state=NORMAL)

def run():
    if configFile['run-lock'] == False:
        runThread = threading.Thread(target = executeCode, name = "runThread1")
        runThread.start()
    else:
        editor.configure(state=DISABLED)
        runThread = threading.Thread(target = executeCode, name = "runThread1")
        runThread.start()
        runThread.join()
        enableThread = threading.Thread(target = enableEditor, name = "enableThread1")
        enableThread.start()
        enableThread.join()

def runShortCut(arg):
    runThread = threading.Thread(target = executeCode, name = "runThread1")
    runThread.start()

def clear():
    os.system('clear')

def settings():
    settingsWin = Tk()
    settingsWin.geometry("350x500")
    settingsWin.title("Settings")

    def saveSettings():
        with open('Settings/Config.json', 'w') as configFile:
            newSettings = settingsEditor.get('1.0', END)
            configFile.write(newSettings)
            messagebox.showinfo("WAIT", "Please reload to apply changes")

    saveSettingsBtn = Button(settingsWin, text = 'Save', command = lambda: saveSettings())
    saveSettingsBtn.place(relx = 0, rely = 0, relwidth = 1.0, relheight = 0.1)

    settingsEditor = Text(settingsWin)
    settingsEditor.place(relx = 0, rely = 0.1, relwidth = 1.0, relheight = 0.9)
 
    def tab(arg):
        settingsEditor.insert(INSERT, " " * configFile["default-indent-spacing"])
        return 'break'
    settingsEditor.bind("<Tab>", tab)

    settingsEditor.insert(INSERT, open('Settings/Config.json').read())
    saveSettingsBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)
    settingsEditor.configure(background=configFile["bg-color"], foreground = configFile["font-color"], insertbackground=configFile["curser-color"], highlightthickness = 0, bd = 0)

    settingsWin.mainloop()

def autoSave():
    if configFile["auto-save"] == True:
        while appAlive == True:
            save()
            time.sleep(configFile["auto-save-interval"])

runBtn = Button(window, text = "Run", command = lambda: run())
runBtn.place(relx = 0, rely = 0, relwidth = 0.225, relheight = 0.07)

saveBtn = Button(window, text = "Save", command = lambda: save())
saveBtn.place(relx = 0.225, rely = 0, relwidth = 0.225, relheight = 0.07)

saveAsBtn = Button(window, text = "Save As", command = lambda: saveAs())
saveAsBtn.place(relx = 0.450, rely = 0, relwidth = 0.225, relheight = 0.07)

clearBtn = Button(window, text = "Clear", command = lambda: clear())
clearBtn.place(relx = 0.675, rely = 0, relwidth = 0.225, relheight = 0.07)

settingsBtn = Button(window, text = configFile["settings-icon"], command = lambda: settings())
settingsBtn.place(relx = 0.90, rely = 0, relwidth = 0.1, relheight = 0.07)

def tab(arg):
    if '.py' in str(fileLine):
    	editor.insert(INSERT, " " * configFile["python-indent-spacing"])
    elif '.java' in str(fileLine):
        editor.insert(INSERT, " " * configFile["java-indent-spacing"])
    elif '.cpp' in str(fileLine):
        editor.insert(INSERT, " " * configFile["cpp-indent-spacing"])
    else:
        editor.insert(INSERT, " " * configFile["default-indent-spacing"])
    return 'break'

def paraComplete(arg):
    editor.insert(INSERT, "()")
    return 'break'

def curlComplete(arg):
    editor.insert(INSERT, "{}")
    return 'break'

def bracketComplete(arg):
    editor.insert(INSERT, "[]")
    return 'break'

def arrowComplete(arg):
    editor.insert(INSERT, "<>")
    return 'break'

def dubQuoteComplete(arg):
    editor.insert(INSERT, '""')
    return 'break'

def singQuoteComplete(arg):
    editor.insert(INSERT, "''")
    return 'break'

def autoIndent(arg):
    if str(' ' * configFile["python-indent-spacing"]) in editor.get(INSERT):
        editor.insert(INSERT, "    ")

editor.bind("<Tab>", tab)
editor.bind(configFile["run-shortcut"], runShortCut)
editor.bind(configFile["save-shortcut"], saveShortCut)

if configFile["auto-indent"] == True:
    editor.bind("<0xff0d>", autoIndent)

if configFile["auto-complete"] == True:
    editor.bind("<0x0028>", paraComplete)
    editor.bind("<0x08af>", curlComplete)
    editor.bind("<0x005b>", bracketComplete)
    editor.bind("<Shift-0x002c>", arrowComplete)
    editor.bind("<Shift-0x0ad0>", dubQuoteComplete)
    editor.bind("<0x0ad0>", singQuoteComplete)

editor.configure(background=configFile["bg-color"], foreground = configFile["font-color"])
editor.configure(insertbackground=configFile["curser-color"])
editor.configure(font = (configFile["font"], configFile["font-size"]), highlightthickness = 0, bd = 0)

settingsBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)

clearBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)

saveAsBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)

runBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)

saveBtn.configure(background=configFile["button-color"], foreground = configFile["font-color"], highlightthickness = 0, bd = 0)

autoSaveThread = threading.Thread(target = autoSave, name = "autosave1")
autoSaveThread.start()

window.mainloop()











































































