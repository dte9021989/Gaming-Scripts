import pyautogui as pag
import time

#Set global sleep variable
s = 0.25

#Set target pixel and color
target_pixel = (1284,684)
target_color = (130,130,130)

#Delay before clicking back into the game
time.sleep(1)
pag.click(target_pixel)

#Define function
def condense_inventory():
    time.sleep(s)
    pag.keyDown("d")
    pag.click(1053,358) #Click weapon
    time.sleep(s)
    pag.click(1006,311) #Click helmet
    time.sleep(s)
    pag.click(1002,361) #Click chest
    time.sleep(s)
    pag.click(1001,412) #Click pants
    time.sleep(s)
    pag.click(1006,459) #Click boots
    time.sleep(s)
    pag.click(955,317) #Click amulet
    time.sleep(s)
    pag.click(960,362) #Click talisman
    time.sleep(s)
    pag.click(927,740) #Click talisman in inventory
    time.sleep(s)
    pag.click(871,728) #Click forest pendant in inventory
    time.sleep(s)
    pag.keyUp("d")

def apply_boosts():
    time.sleep(s)
    pag.keyDown("a")
    pag.click(1053,358) #Click weapon
    time.sleep(s)
    pag.click(1006,311) #Click helmet
    time.sleep(s)
    pag.click(1002,361) #Click chest
    time.sleep(s)
    pag.click(1001,412) #Click pants
    time.sleep(s)
    pag.click(1006,459) #Click boots
    time.sleep(s)
    pag.click(955,317) #Click amulet
    time.sleep(s)
    pag.click(960,362) #Click talisman
    time.sleep(s)
    pag.keyUp("a")

#Main logic loop
#Loop indefinitely
while True:
    #Check if target pixel is not the color
    if not pag.pixelMatchesColor(target_pixel[0], target_pixel[1], target_color):
        print("Condensing Inventory ")
        condense_inventory()
        time.sleep(1)
        print("Applying boosts ")
        apply_boosts()
        time.sleep(1)
    else:
        print("Waiting 10 minutes ")
        time.sleep(300)
        print("5 minutes remianing ")
        time.sleep(240)
        print("60 seconds left ")
        time.sleep(60)