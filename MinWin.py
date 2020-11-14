import os, time, asyncio

def complate():
    time.sleep(1)
    os.system('cls')
    print('Cleaning complate.')
    time.sleep(1)
    os.system('cls')
    menu()

def net():
    os.system('cls')
    conf = input('Reset ipconfig (Y/N)? ')
    if (conf == 'Y' or conf == 'y'):
        os.system(r".\Scripts\net.bat")
        complate()
    else: menu()

def clndisc():
    os.system('cls')
    conf = input("1. Open windows disc.\n2. Open windows disk defragmentation.\n\nPodaj numer funkcji: ")
    if (conf == '1'):
        os.system('%windir%/system32/cleanmgr.exe')
        complate()
    elif (conf == '2'):
        os.system('%windir%/system32/dfrgui.exe')
        complate()
    else: menu()

def temp():
    os.system('cls')
    conf = input('Remove all temp files (Y/N)? ')
    if (conf == 'Y' or conf == 'y'):
        os.system(r'.\Scripts\cache.bat')
        complate()
    else: menu()

def WS():
    os.system(r'.\Scripts\ws.bat')
    complate()
    menu()

def Debloater():
    os.system('cls')
    print('1. Choose what programs you want to uninstall.')
    print('2. Remove All Bloatware.')
    print('3. Enter to back. \n')
    dec = input('Podaj numer funkcji: ')

    if (dec == '1'): os.system(r'.\path\gui.ps1')
    elif (dec == '2'):
        os.system('cls')
        confirm = input('Remove all bloatware (Y/N)? ')
        if (confirm == "Y" or confirm == "y"):
            os.system(r'.\path\removeallbloat.ps1')
        else: menu()
    else: menu()

def menu(): 
    os.system('cls')
    print("1. Clean all garbage.")
    print("2. Remove temp files.")
    print("3. Reset Network cache.")
    print("4. Reset/Fix Windows store.")
    print("5. Open windows disk clean/defrag.")
    print("6. Windows 10 Debloater. \n")

    dec = input("Podaj numer funkcji: ")
    if (dec == "1"):
        os.system('cls')
        conf4 = input("Remove all garbage (Y/N)? : ")
        if (conf4 == "Y" or conf4 == "y"):
            os.system(r".\Scripts\cache.bat")
            os.system(r".\Scripts\net.bat")
            complate()
        else: menu()
    elif (dec == "2"): temp()
    elif (dec == "3"): net()
    elif (dec == "4"): WS()
    elif (dec == "5"): clndisc()
    elif (dec == "6"): Debloater()
    else: menu()

menu()









































































