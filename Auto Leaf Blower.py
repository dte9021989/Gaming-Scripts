import pyautogui as pag
import time

#Pause to let application switch
time.sleep(5)

#Main loop

while True:
    #Get screen size
    screenWidth, screenHeight = pag.size()

    #Set failsafe offset
    offset = 1

    #Move to upper left and go to upper right
    pag.moveTo(offset, offset)
    pag.dragTo(screenWidth - offset, offset, duration=0.5)

    #pause
    time.sleep(0.5)

    #Upper right to middle left
    pag.dragTo(offset, screenHeight / 2, duration=0.5)

    #Pause
    time.sleep(0.5)

    #Middle left to middle right
    pag.dragTo(screenWidth - offset, screenHeight / 2, duration=0.5)

    #Pause
    time.sleep(0.5)

    #Middle right to bottom left
    pag.dragTo(offset, screenHeight - offset, duration=0.5)

    #Pause
    time.sleep(0.5)

    #Bottom left to bottom right
    pag.dragTo(screenWidth - offset - offset, screenHeight - offset - offset, duration=0.5)

    #Pause at end of loop
    time.sleep(3)
