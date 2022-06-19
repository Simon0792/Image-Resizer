'''
Image resizer. This program resizes images at 1600x1600 and 1000x1000 while respecting their ratio
Written by simone onorato
19/07/2021
Kingston, Ontario
For questions or support contact me at simon.onorato@queensu.ca
all right reserved.
'''

import time
from img_resizer import cleanUp, startResWebsite, startResAmzEbay
import os
import platform

#Clear screen from data
def clearScreen():
    opsystem = platform.system()
    if opsystem == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# MAIN MENU
def main():
    clearScreen()
    run = True
    while run is True:
        print('K-RESIZER (V.1.0)')
        print('----------------------------------------')
        print('Written by Simone Onorato')
        print('for Kinglon Baby Design')
        print('Last Update 08/08/2021')
        print()
        print('''
            $$$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  
            $$  __$$\ $$  _____|$$  __$$\ \_$$  _|\____$$  |$$  _____|$$  __$$\ 
            $$ |  $$ |$$ |      $$ /  \__|  $$ |      $$  / $$ |      $$ |  $$ |
            $$$$$$$  |$$$$$\    \$$$$$$\    $$ |     $$  /  $$$$$\    $$$$$$$  |
            $$  __$$< $$  __|    \____$$\   $$ |    $$  /   $$  __|   $$  __$$< 
            $$ |  $$ |$$ |      $$\   $$ |  $$ |   $$  /    $$ |      $$ |  $$ |
            $$ |  $$ |$$$$$$$$\ \$$$$$$  |$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$ |  $$ |
            \__|  \__|\________| \______/ \______|\________|\________|\__|  \__|''')
        print()
        print()
        print()
        print()
        print()
        print('Please chose one of the following options:')
        print('--------------------------------------------')
        print()
        print('● Resize images for Amazon/Ebay and Woocommerce --- 1')
        print('● Exit -------------------------------------------- 0')
        print()
        userChoice = str(input('Enter your choice: '))

        if userChoice == '1':
            clearScreen()
            print()
            print()
            print('Choice: Resize images for all platforms')
            print('Starting image resizing for Amazon and Ebay')
            startResAmzEbay()
            print()
            print('Amazon and Ebay resizing complete')
            print()
            print('Starting image resizing for Woocommerce')
            startResWebsite()
            print()
            print('Woocommerce Resize complete')
            print('All resizing complete.')
            input('Press Enter to Continue...')
            clearScreen()

        elif userChoice == '0':
            print()
            print()
            run=False
            print('Exiting')
            time.sleep(2)

        elif userChoice == '':
            clearScreen()

        else:
            print('Invalid choice')
            time.sleep(2)
            clearScreen()

main()