from mss import mss
from mss.tools import to_png

# Coordinates
food_upper_left_corner = 2300,491
food_lower_right_corner = 2344,510

def capture_and_save_screenshot(filename):
    with mss() as sct:
        # Define the screen part to capture
        monitor = {
            "top": food_upper_left_corner[1], 
            "left": food_upper_left_corner[0], 
            "width": food_lower_right_corner[0] - food_upper_left_corner[0], 
            "height": food_lower_right_corner[1] - food_upper_left_corner[1]
        }
        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        to_png(sct_img.rgb, sct_img.size, output=filename)

# Example usage
capture_and_save_screenshot("screenshot.png")
