import pyautogui as pag
import time
from food_recognition import get_numerical_value
import sys

#Global variable declaration
top_of_game_window = 2892,4
attack_menu_button = 2009,349
blank_spot_on_combat_screen = 2176,559
food_upper_left_corner = 2300,491
food_lower_right_corner = 2344,510
run_button = 3507,780
slayer_button = 2787,925

#Sleep timers
ls = 10
s = 1
ss = 0.25

######
# Main Logic
######

#Sleep at start of script
time.sleep(s)

#Click into game
pag.click(top_of_game_window)
time.sleep(ss)

#Click into combat screens
pag.click(attack_menu_button)
time.sleep(s)

#Start Slayer tasks
pag.click(slayer_button)

while True:
    # Call the OCR function
    number = get_numerical_value(food_upper_left_corner, food_lower_right_corner)

    # Use the number to influence the behavior of this script
    if number is not None:
        print("Number detected:", number)
    elif number is None:
        print('Out of food. Running from encounter ')
        pag.click(run_button)
        sys.exit()
    else:
        print("An error occurred")
    
    # Wait for X seconds before the next OCR
    time.sleep(1)  # Replace 10 with your desired number of seconds