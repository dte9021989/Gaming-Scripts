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

####
# Main program
####

#Ask user for input on what function they want
user_choice = input("Select number:\n"
                    "1. Harvest all crops\n"
                    "99. Exit\n")

# Convert user_choice to integer for comparison
try:
    user_choice = int(user_choice)
except ValueError:
    print("Please enter a valid number.")

#Perform function based on user input
if user_choice == 1:
    print('Harvesting all crops ')
    farming_harvest_all()
elif user_choice == 99:
    print('Exiting ')