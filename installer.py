import os
os.system('sudo apt-get install python3-tk')
os.system('git clone https://github.com/Jadens-arc/scripty')
with open('.bashrc', 'r') as extRead:
    extRead = extRead.read()
    if 'alias scripty="python3 scripty.py"' not in extRead:
        with open('.bashrc', 'a') as extWrite:
            extWrite.write('alias scripty="python3 scripty.py"')
os.system('rm installer.py')








