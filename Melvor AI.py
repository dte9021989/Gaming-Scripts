import pyautogui as pag
import time

#Tab locations
mining_tab = 1999,945

#Button locations


#Sleep timers
s = 1
ss = 0.25

#Function definition
def goto_mining_tab():
    #Click into game and select mining tab
    print('Selecting Mining Tab ')
    time.sleep(ss)
    pag.click(mining_tab)
    time.sleep(ss)
    pag.click(mining_tab)

#Main program

#Sleep program for CPU catch up
time.sleep(s)

goto_mining_tab()
