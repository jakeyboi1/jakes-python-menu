import os, keyboard, time

def updateMenu(title, options, selectedOption):
    os.system('cls') #Clearing the console
    whiteBackround = '\33[7m'
    clearColor = '\033[0m'
    print(title + '\n')
    index = 0
    for option in options:
        if index == selectedOption:
            print(whiteBackround + option + clearColor)
        else:
            print(option)
        
        index += 1


def createMenu(title, options):
    updateMenu(title, options, 0)
    selectedOption = 0
    while True:
        key = keyboard.read_key()
        if key == "down":
            selectedOption += 1
            updateMenu(title, options, selectedOption)
        elif key == "up":
            selectedOption -= 1
            updateMenu(title, options, selectedOption)
        elif key == "enter":
            return options[selectedOption]
        
        time.sleep(.2)