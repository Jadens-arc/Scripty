
# Scripty:

An Open-Source IDE for ChromeOS by Jaden Arceneaux
  
  
# Keyboard Shortcuts:
  - Compile and Execute Code:
  
        Alt - r
  
  
  - Save Code:
  
        Alt - s
  
  
# Requirements:

  - Python3(and its built-in moduals)
  
  - Tkinter
  
  - Linux(not tested for Windows or MacOS)
  
  - Java
  
  - C++


# Usage:
  
    cd Scripty
  
    python3 Scripty.py [your file]
  
  ![](images/IMAGE3.png)
  
# Tips:

### Installing Dependacies:
  
  Scripty will automaticly install Tkinter but will not install Java or C++

### Easy Running:

  Change directories into your root directory

      $ cd ~

  Start editing your .bashrc file

      $ nano .bashrc

  Scroll to the bottom and add an alias for python3 scripty.py

      alias scripty="python3 Scripty.py"

  Now you can just say *Scripty [your file]* instead of the full command

      $ Scripty [your file]
  
# Settings:
Setting | Function
------------ | -------------
bg-color | Background color of the editor (in hexadecimal or by name)
font-color | Color of text in the editor (in hexadecimal or by name)
button-color | Color of buttons in the editor (in hexadecimal or by name)
font | Font of the editor
font-size | Font size of the editor
curser-color | The color of your curser (in hexadecimal or by name)
line-wrap | Determines whether text will wrap to new line when it reaches the edge of the screen
line-wrap-type | Determines whether the entire word will wrap or just the overflowing character (WORD or CHAR)
auto-save | Toggle for automatic saving
auto-save-interval | Determines the frequency(in seconds) a save will occur
python-indent-spacing | Determines the indent spacing for Python code
java-indent-spacing | Determines the indent spacing for Java code
cpp-indent-spacing | Determines the indent spacing for C++ code
default-indent-spacing | Demermines the indent spacing for any programming language not listed above
auto-indent | **WORK IN PROGRESS** Toggle for auto indent
settings-icon | Icon used for the settings button
run-shortcut | Keyboard shorcut for compliling and exicuting code
save-shortcut | Keyboard shortcut for saving code
auto-complete | Toggle for smart completion of code
run-lock | Toggle for run lock which disables editing of code while code is running
clear-on-run | Toggle for clearing terminal when program is ran
compilers | **WORK IN PROGRESS**  Specifies the commands used to run code for certain languages

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk4MTkzNTk4Niw0NTkwMzY4ODcsMTQ3MT
g1MzI5NF19
-->
