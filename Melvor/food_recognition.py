# OCR_Script.py

from mss import mss
from PIL import ImageOps, Image
import pytesseract

# Set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update as necessary

def capture_and_preprocess(food_upper_left_corner, food_lower_right_corner):
    with mss() as sct:
        monitor = {
            "top": food_upper_left_corner[1], 
            "left": food_upper_left_corner[0], 
            "width": food_lower_right_corner[0] - food_upper_left_corner[0], 
            "height": food_lower_right_corner[1] - food_upper_left_corner[1]
        }
        sct_img = sct.grab(monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)

    img = img.convert('L')
    img = ImageOps.invert(img)
    img = img.point(lambda x: 0 if x < 128 else 255)
    return img

def get_numerical_value(food_upper_left_corner, food_lower_right_corner):
    img = capture_and_preprocess(food_upper_left_corner, food_lower_right_corner)
    text = pytesseract.image_to_string(img, config='--psm 6 outputbase digits')

    try:
        number = int(''.join(filter(str.isdigit, text)))
        return number
    except ValueError:
        return None

# Example coordinates
# food_upper_left_corner = (2293, 457)
# food_lower_right_corner = (2342, 486)

# Example call
# print("Extracted Number:", get_numerical_value(food_upper_left_corner, food_lower_right_corner))
