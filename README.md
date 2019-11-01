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
  
  - Linux(not tested for Windows or Mac)
  
  - Java
  
  - C++


# Usage:
  
    cd scripty
  
    python3 scripty.py [your file]
  
  ![](images/IMAGE3.png)
  
# Tips:
### Easy Running:

  Change directories into your root directory

      cd ~
  
  Start editing your .bashrc file
  
      nano .bashrc
      
  Scroll to the bottom and add an alias for python3 scripty.py
      
      alias scripty="python3 scripty.py"
      
  Now you can just say *scripty [your file]* instead of the full command
  
      scripty [your file]
  
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
auto-indent | Toggle for auto indent
settings-icon | Icon used for the settings button
run-shortcut | Keyboard shorcut for compliling and exicuting code
save-shortcut | Keyboard shortcut for saving code
auto-complete | Toggle for smart completion of code
run-lock | Toggle for run lock which disables editing of code while code is running



