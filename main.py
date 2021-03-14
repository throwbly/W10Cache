from os import system
from sources import reg

def winmenu():
    from sources import ls
    for key in ls:
        for path in ls[key]:
            system(f'cmd /c "attrib +R +S +H "{path}""')

def clean():
    from sources import toClean
    for path in toClean:
        system(f'cmd /c "del /f /a /q "{path}"')
        system(f'cmd /c "rd /s /q "{path}""')

def removedesktop():
    hoho = "powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}' -Force -Verbose"
    system(f'cmd /c "{hoho}" ')
#removedesktop()

def restoredesktop():
    hoho = "powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}'"
    system(f'cmd /c "{hoho}"')
#restoredesktop()

def removeall():
    for names in reg:
        for path in reg[names]:
            regpath = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
            system(f'cmd /c "{regpath}"')
#removeall()

def restoreall():
    for names in reg:
        for path in reg[names]:
            regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
            system(f'cmd /c "{regpath}"')

def FileExplorer():
    system('CLS')
    option = int(input('1. Hide File Explorer Folders\n2. Show File Explorer Folders'))
    if option == 1:
        system('cls')
        test = int(input("1. Desktop\n2. Documents\n3. Video\n4. Pictures\n5. Downloads\n6. Music"))

        if test == 1:
            for path in reg['Desktop']:
                removeReg = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
                system(f'cmd /c "{removeReg}"')
            FileExplorer()

        elif test == 2:
            for path in reg['Documents']:
                removeReg = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
                system(f'cmd /c "{removeReg}"')
            FileExplorer()

        elif test == 3:
            for path in reg['Video']:
                removeReg = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
                system(f'cmd /c "{removeReg}"')
            FileExplorer()

        elif test == 4:
            for path in reg['Pictures']:
                removeReg = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
                system(f'cmd /c "{removeReg}"')
            FileExplorer()

        elif test == 5:
            for path in reg['Downloads']:
                removeReg = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
                system(f'cmd /c "{removeReg}"')
            FileExplorer()

        elif test == 6:
            for path in reg['Music']:
                removeReg = f"powershell Remove-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}' -Force -Verbose"
                system(f'cmd /c "{removeReg}"')
            FileExplorer()


    elif option == 2:
        system('cls')
        test = int(input("1. Desktop\n2. Documents\n3. Video\n4. Pictures\n5. Downloads\n6. Music"))

        if test == 1:
            for path in reg['Desktop']:
                regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
                system(f'cmd /c "{regpath}"')
            FileExplorer()

        elif test == 2:
            for path in reg['Documents']:
                regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
                system(f'cmd /c "{regpath}"')
        
        elif test == 3:
            for path in reg['Video']:
                regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
                system(f'cmd /c "{regpath}"')

        elif test == 4:
            for path in reg['Pictures']:
                regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
                system(f'cmd /c "{regpath}"')
        
        elif test == 5:
            for path in reg['Downloads']:
                regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
                system(f'cmd /c "{regpath}"')

        elif test == 6:
            for path in reg['Music']:
                regpath = f"powershell New-Item -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\{path}'"
                system(f'cmd /c "{regpath}"')

def menu():
    system('CLS')
    Menu = int(input('1. File Explorer Folders'))
    if Menu == 1:
        FileExplorer()
        
menu()

