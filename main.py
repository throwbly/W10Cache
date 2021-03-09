from os import system, listdir
from listy import ls, clean

for value in ls: 
    system('cmd /c "attrib +h "%s""'%(ls[value]["zawartość"])) 
    system('cmd /c "attrib +h "%s""'%(ls[value]["folder"]))

for value in clean:
    system('cmd /c "del /f /a /q "%s""'%value)
    system('cmd /c "rd /s /q "%s""'%value)