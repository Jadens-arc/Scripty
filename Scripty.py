#!/usr/bin/env python3
# An open-source IDE for python, java, and C++
# By Jaden Arceneaux arceneauxJaden@gmail.com
# Feel free to change code as you feel

import sys
import os
# For running commands in the terminal

try:
    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog
except:
    os.system('sudo apt-get install python3-tk')
    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog
# Checks if tkinter is installed
# if not then installs it
# used for UI

import json
# For parsing json files 

import time

import threading
# For running multiple tasks on the CPU 

os.system('chmod +x Scripty.py')

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

styleSheet = open("Settings/Themes/" + configFile["theme"].lower() + '.json')
styleSheet = json.loads(styleSheet.read())

os.system('clear')
# ^ clears the terminal at the start of the program

window = Tk()
window.geometry("550x350")
# ^ declared window and sets size (in pixels)

if sys.argv[-1] == "Scripty.py":
    fileLine = filedialog.asksaveasfilename(initialdir = "~/Scripty/Projects",title = "Select file",filetypes = (("All Files","*.*"),("C++","*.cpp"), ("Java", "*.java"), ("Python", "*.py")))
else:
    fileLine = 'Projects/' + str(sys.argv[-1])

window.title(str(fileLine))
# ^  find the arument for which file to edit in the terminal
# and sets it as the title of the window

try:
    try:
        currFile = open(str(fileLine))
    except:
        newFile = open(str(fileLine), "w")
        newFile.close()
        currFile = open(str(fileLine))
except:
    i = 0
    while '/' in fileLine:
        fileLine.replace(fileLine[i], "")
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
    scrollbar = Scrollbar(window, orient=HORIZONTAL, background = styleSheet['bg-color'])
    scrollbar.place(relx = 0, rely = 0.95, relheight = 0.05)

    editor = Text(window, wrap = NONE)
    editor.config(yscrollcommand=scrollbar.set)

    scrollbar.config(command=editor.xview)

    for line in currFile:
        editor.insert(INSERT, line)

    editor.place(rely = 0.07, relx = 0, relheight = 0.88, relwidth = 1.0)
# checks if line wrap is enabled and which kind on line wrap it is 
# if line wrap is not enable it enables the scroll butttons 

def save():
    global appAlive
    try:
        user = editor.get('1.0', END)
        file = open(str(fileLine), "w")
        file.write(user)
        file.close()
    except:
        appAlive = False
# Save function
# it takes all the text in the editor and writes it to the appropriate file
        
def saveShortCut(arg):
    save()
# This function maps the save function to work with a keyboard shortcut

def openWindow():
    global editor, fileLine
    openFile = str(filedialog.asksaveasfilename(initialdir = "~/Scripty/Projects",title = "Select file",filetypes = (("All Files","*.*"),("C++","*.cpp"), ("Java", "*.java"), ("Python", "*.py"))))
    editor.delete('1.0', END)
    openFileData = open(openFile)
    openFileData = openFileData.read()
    editor.insert(INSERT, openFileData)
    fileLine = openFile
    i = 0
    while i < len(fileLine):
        if '/' in fileLine:
            fileLine.replace(fileLine[i], "")
        i += 1
    window.title(str(fileLine))
    # redraw the editor but skinner and left sided
# This function allows the user to open muiltiple files

def saveAs():
    global fileLine, appAlive
    fileLine = filedialog.asksaveasfilename(initialdir = "~/Scripty/Projects",title = "Select file",filetypes = (("All Files","*.*"),("C++","*.cpp"), ("Java", "*.java"), ("Python", "*.py")))
    try:
        user = editor.get('1.0', END)
        file = open(str(fileLine), "w")
        file.write(user)
        file.close()
    except:
        appAlive = False
    window.title(str(fileLine))

# Function for save as button

def executeCode():
    save()
    # saves file before running
    
    if configFile['clear-on-run'] == True:
        os.system('clear')
    # checks if clear on run is enabled in settings 
    # if so clears terminal before running code
    
    if '.py' in fileLine:
        os.system('python3 ' + str(fileLine))
    elif '.java' in fileLine:
        os.system('javac ' + str(fileLine))
        os.system('cd Projects && java ' + (fileLine[:-5]).replace('Projects/', ''))
    elif '.cpp' in fileLine:
        os.system('g++ ' + str(fileLine) + ' -o ' + fileLine[:-4])
        os.system('./' + fileLine[:-4])
    elif '.cs' in fileLine:
        os.system('dotnet run ' + fileLine)
    # finds which programming language the program is written in
    # runs code using that language

def enableEditor():
    editor.configure(state=NORMAL)
# sets editor to is enabled state

def run():
    if configFile['run-lock'] == False:
        runThread = threading.Thread(target = executeCode, name = "runThread1")
        runThread.start()
    else:
        editor.configure(state=DISABLED)
        # disables editor while running if run lock is True
        runThread = threading.Thread(target = executeCode, name = "runThread1")
        runThread.start()
        runThread.join()
        enableThread = threading.Thread(target = enableEditor, name = "enableThread1")
        enableThread.start()
        enableThread.join()
        # once it is done running renables editor 
 # function for running code

def runShortCut(arg):
    runThread = threading.Thread(target = executeCode, name = "runThread1")
    runThread.start()
# keyboard short cut for running code
# accepts argument from keyboard
    
def clear():
    os.system('clear')
# function for clearing terminal

def settings():
    settingsWin = Tk()
    settingsWin.geometry("350x600")
    settingsWin.title("Settings")
    # delcares settings window

    def saveSettings():
        with open('Settings/Config.json', 'w') as configFile:
            newSettings = settingsEditor.get('1.0', END)
            configFile.write(newSettings)
            messagebox.showinfo("WAIT", "Please reload to apply changes")
    # function for saving settings

    saveSettingsBtn = Button(settingsWin, text = 'Save', command = lambda: saveSettings())
    saveSettingsBtn.place(relx = 0, rely = 0, relwidth = 1.0, relheight = 0.1)
    # declares saveSettingsButton

    settingsEditor = Text(settingsWin)
    settingsEditor.place(relx = 0, rely = 0.1, relwidth = 1.0, relheight = 0.9)
    # delcares settings editor
 
    def tab(arg):
        settingsEditor.insert(INSERT, " " * configFile["default-indent-spacing"])
        return 'break'
    settingsEditor.bind("<Tab>", tab)
    # binds tab to appropriate spacing

    settingsEditor.insert(INSERT, open('Settings/Config.json').read())
    saveSettingsBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)
    settingsEditor.configure(background=styleSheet["bg-color"], foreground = styleSheet["font-color"], insertbackground=styleSheet["curser-color"], highlightthickness = 0, bd = 0)
    # configures settings editor and buttons to match styling
    
    settingsWin.mainloop()

def autoSave():
    if configFile["auto-save"] == True:
        while appAlive == True:
            save()
            time.sleep(configFile["auto-save-interval"])
# function for auto save

runBtn = Button(window, text = "Run", command = lambda: run())
runBtn.place(relx = 0, rely = 0, relwidth = 0.18, relheight = 0.07)
# delcares run button 

saveBtn = Button(window, text = "Save", command = lambda: save())
saveBtn.place(relx = 0.18, rely = 0, relwidth = 0.18, relheight = 0.07)
# delcares save button 

saveAsBtn = Button(window, text = "Save As", command = lambda: saveAs())
saveAsBtn.place(relx = 0.36, rely = 0, relwidth = 0.18, relheight = 0.07)
# delcares save as button 

openBtn = Button(window, text = "Open", command = lambda: openWindow())
openBtn.place(relx = 0.54, rely = 0, relwidth = 0.18, relheight = 0.07)
# delcares open button

clearBtn = Button(window, text = "Clear", command = lambda: clear())
clearBtn.place(relx = 0.72, rely = 0, relwidth = 0.18, relheight = 0.07)
# delcares clear button 

settingsBtn = Button(window, text = configFile["settings-icon"], command = lambda: settings())
settingsBtn.place(relx = 0.9, rely = 0, relwidth = 0.1, relheight = 0.07)
# delcares settings button 

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
# maps tab to appropriate spacing

def paraComplete(arg):
    editor.insert(INSERT, "()")
    return 'break'
# inserts ()

def curlComplete(arg):
    editor.insert(INSERT, "{}")
    return 'break'
# inserts {}

def bracketComplete(arg):
    editor.insert(INSERT, "[]")
    return 'break'
# inserts []

def arrowComplete(arg):
    editor.insert(INSERT, "<>")
    return 'break'
# inserts <>

def dubQuoteComplete(arg):
    editor.insert(INSERT, '""')
    return 'break'
# inserts ""

def singQuoteComplete(arg):
    editor.insert(INSERT, "''")
    return 'break'
# inserts ''

def autoIndent(arg):
    if str(' ' * configFile["python-indent-spacing"]) in editor.get(INSERT):
        editor.insert(INSERT, "    ")
# will automaticly indent to the appropreat spacing 
# work in progess

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
# checks if auto complete is inabled 
# if so binds keys

editor.configure(background=styleSheet["bg-color"], foreground = styleSheet["font-color"])
editor.configure(insertbackground=styleSheet["curser-color"])
editor.configure(font = (styleSheet["font"], configFile["font-size"]), highlightthickness = 0, bd = 0)

settingsBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)

clearBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)

saveAsBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)

runBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)

saveBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)

openBtn.configure(background=styleSheet["button-color"], foreground = styleSheet["font-color"], highlightthickness = 0, bd = 0)
# configures buttons and text editor to match style 

autoSaveThread = threading.Thread(target = autoSave, name = "autosave1")
autoSaveThread.start()
# starts autosave thread

window.mainloop()







