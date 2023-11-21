import pyautogui as pag
import time

#Tab locations
mining_tab = 1999,945
farming_tab = 2025,655

#Button locations
farming_allotments = 2441,269
farming_herbs = 2913,277
farming_trees = 3445,264
farming_harvest_all_button = 2492,365
farming_apply_compost_button = 2713,360

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

def goto_farming_tab():
    #Click into game and select farming tab
    print('Selecting Farming Tab ')
    time.sleep(ss)
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_tab)

def farming_harvest_all():
    #Harvesting all crops via Harvest All button
    print("Harvesting all crops ")
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_allotments)
    time.sleep(ss)
    pag.click(farming_harvest_all_button)
    time.sleep(ss)
    pag.click(farming_herbs)
    time.sleep(ss)
    pag.click(farming_harvest_all_button)
    time.sleep(ss)
    pag.click(farming_trees)
    time.sleep(ss)
    pag.click(farming_harvest_all_button)

def farming_apply_compost():
    #Harvesting all crops via Harvest All button
    print("Applying compost ")
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_allotments)
    time.sleep(ss)
    pag.click(farming_apply_compost_button)
    time.sleep(ss)
    pag.click(farming_herbs)
    time.sleep(ss)
    pag.click(farming_apply_compost_button)
    time.sleep(ss)
    pag.click(farming_trees)
    time.sleep(ss)
    pag.click(farming_apply_compost_button)