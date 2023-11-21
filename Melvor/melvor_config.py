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
farming_plant_all_button = 3237,369
farming_crop_plant_button = 2942,450

#Crop seed locations
potato = 2665,189
onion = 2665,233
cabbage = 2665,276
tomato = 2665,316
sweetcorn = 2665,362
strawberry = 2665,413
cherry = 2665,455
watermelon = 2665,500
#snape_grass = 2665,
#carrot = 2665,

#Sleep timers
s = 1
ms = 0.5
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

def plant_action():
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_tab)
    time.sleep(ss)
    pag.click(farming_allotments)
    time.sleep(ss)
    pag.click(farming_plant_all_button)

def farming_allotments_plant_all():
    plant_choice = input("Select number:\n"
                         "1. Potato\n"
                         "2. Onion\n"
                         "3. Cabbage\n"
                         "4. Tomato\n"
                         "5. Sweetcorn\n"
                         "6. Strawberry\n"
                         "7. Cherry\n"
                         "8. Watermelon\n"
                         "9. Snape Grass\n"
                         "10. Carrot\n")
    # Convert user_choice to integer for comparison
    try:
        plant_choice = int(plant_choice)
    except ValueError:
        print("Please enter a valid number.")
    plant_action()
    if plant_choice == 1:
        print("Planting Potoates")
        time.sleep(ms)
        pag.click(potato)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 2:
        print("Planting Onions")
        time.sleep(ms)
        pag.click(onion)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 3:
        print("Planting Cabbages")
        time.sleep(ms)
        pag.click(cabbage)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 4:
        print("Planting Tomatoes")
        time.sleep(ms)
        pag.click(tomato)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 5:
        print("Planting Sweetcorn")
        time.sleep(ms)
        pag.click(sweetcorn)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 6:
        print("Planting Strawberries")
        time.sleep(ms)
        pag.click(strawberry)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 7:
        print("Planting Cherries")
        time.sleep(ms)
        pag.click(cherry)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    elif plant_choice == 8:
        print("Planting Watermelons")
        time.sleep(ms)
        pag.click(watermelon)
        time.sleep(ms)
        pag.click(farming_crop_plant_button)
    # elif plant_choice == 9:
    #     print("Planting Snape Grass")
    #     time.sleep(ms)
    #     pag.click(snape_grass)
    #     time.sleep(ms)
    #     pag.click(farming_crop_plant_button)
    # elif plant_choice == 10:
    #     print("Planting Carrots")
    #     time.sleep(ms)
    #     pag.click(carrot)
    #     time.sleep(ms)
    #     pag.click(farming_crop_plant_button)
    else:
        print("An error with planting has occurred ")