

# Scripty:
An Open-Source IDE for ChromeOS by Jaden Arceneaux. This project was created due to a distinct lack of good IDEs for ChromeOS. The goal of Scripty is to supplement this problem. Scripty takes advantage of the built-in Linux sandbox in Chrome Books to provide the best coding experience on ChromeOS.

# Requirements:
  - Python3
  - Tkinter (will automatically install on run)
  - OS (built in Python module)
  - JSON (built in Python module)
  - Sys (built in Python module)
  - Time (built in Python module)
  - Threading  (built in Python module)
  - Linux (not tested for Windows or macOS)
  - Java
  - C++

# Usage:
```
cd Scripty
python3 Scripty.py
or
python3 Scripty.py [Your File]
```
This will then bring up a window for you to select a file

![](https://i.postimg.cc/wTGGmr2s/Screenshot-2019-12-05-at-8-08-37-PM.png)

Projects you create will be stored in the /Projects/ directory

These projects will be gitignored by default 

# Tips:

### Keyboard Shortcuts:
- Compile and Execute Code:
```
Alt - r
```
- Save Code:
```
Alt - s
```

### Installing Dependencies:
Scripty will automatically install Tkinter but will not install Java or C++

### Easy Running:
Change directories into your root directory
```
$ cd ~
```
Start editing your .bashrc file
```
$ nano .bashrc
```
Scroll to the bottom and add an alias for python3 scripty.py
```
alias scripty="python3 Scripty.py"
```
Now you can just say *Scripty [your file]* instead of the full command
```
$ Scripty [your file]
```

# Settings:
Setting | Function
------------ | -------------
Theme | Changes the theme(color scheme) of the editor
font-size | Font size of the editor
line-wrap | Determines whether the text will wrap to a new line when it reaches the edge of the screen
line-wrap-type | Determines whether the entire word will wrap or just the overflowing character (WORD or CHAR)
auto-save | Toggle for automatic saving
auto-save-interval | Determines the frequency(in seconds) a save will occur
python-indent-spacing | Determines the indent spacing for Python code
java-indent-spacing | Determines the indent spacing for Java code
cpp-indent-spacing | Determines the indent spacing for C++ code
default-indent-spacing | Determines the indent spacing for any programming language not listed above
auto-indent | **WORK IN PROGRESS** Toggle for auto-indent
settings-icon | Icon used for the settings button
run-shortcut | Keyboard shortcut for compiling and executing code
save-shortcut | Keyboard shortcut for saving code
auto-complete | Toggle for smart completion of code
run-lock | Toggle for the run lock which disables editing of code while code is running
clear-on-run | Toggle for clearing terminal when a program is ran

# Themes:
## Available Themes:

 - Watermelon
 - Light-Mode
 - Dark-Mode
 - Red
 - Blue
 - Green
 - Off-White
 - Purple
 - Dark-blue
 - McLaren
 - Coral
 - Panda

## Creating a Theme:
**Themes must be in JSON format and must be saved in the Themes folder.**

**The names of these files must be completely lower case.**
```
ex. Scripty/Settings/Themes$ nano mytheme.json
```

**Themes must follow this template**
```json
{
    "bg-color": "[Color]",
    "font-color": "[Color]",
    "button-color": "[Color]",
    "font": "[Font]",
    "curser-color": "[Color]"
}
```
Setting | Function
------------ | -------------
curser-color | The color of your curser (in hexadecimal or by name)
bg-color | Background color of the editor (in hexadecimal or by name)
font-color | Color of text in the editor (in hexadecimal or by name)
button-color | Color of buttons in the editor (in hexadecimal or by name)
font | Font of the editor

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc2ODExMjUwLC0xMDA3OTE4Mzk5LC0yND
UyMzMwNTYsLTM2NjMzODc2NywtMjEyMDgwNzU0OCwtODk5NjIx
NjY2LC0yMDgyNDcxNDEyLDEyNjkzOTA0OTEsMTk4MTkzNTk4Ni
w0NTkwMzY4ODcsMTQ3MTg1MzI5NF19
-->
