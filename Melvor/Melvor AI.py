import pyautogui as pag
import time
import melvor_config as c
print("Config file loaded ")



##################
# Main program   #
##################

#Ask user for input on what function they want
user_choice = input("Select number:\n"
                    "1. Harvest all crops\n"
                    "2. Apply compost\n"
                    "3. Plant crops\n"
                    "99. Exit\n")

# Convert user_choice to integer for comparison
try:
    user_choice = int(user_choice)
except ValueError:
    print("Please enter a valid number.")

#Perform function based on user input
if user_choice == 1:
    c.farming_harvest_all()
elif user_choice == 2:
    c.farming_apply_compost()
elif user_choice == 3:
    c.farming_allotments_plant_all()
elif user_choice == 99:
    print('Exiting ')