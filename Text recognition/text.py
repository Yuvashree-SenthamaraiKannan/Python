import cv2
import easyocr
import time
import pygetwindow as gw
from PIL import ImageGrab

# Function to check if a given text is present in the OCR output
def is_text_present(ocr_output, expected_text):
    for result in ocr_output:
        text = result[1]
        if expected_text.lower() in text.lower():
            return True
    return False

# Function to find and return the Chrome window if visible
def find_chrome_window():
    chrome_windows = [win for win in gw.getWindowsWithTitle('Google Chrome') if win.visible]
    return chrome_windows[0] if chrome_windows else None


# Function to wait for webpage to load (adjust as needed)
def wait_for_webpage_load():
    time.sleep(5)

# Function to take screenshot of Chrome window displaying a specific website
def take_website_screenshot(url):
    chrome_window = find_chrome_window()

    if chrome_window:
        chrome_window.activate()
        wait_for_webpage_load()
        left, top, right, bottom = chrome_window.left, chrome_window.top, chrome_window.right, chrome_window.bottom

        # Calculate the actual size of the Chrome window (excluding borders)
        chrome_window_width = right - left
        chrome_window_height = bottom - top

        # Take screenshot using Pillow's ImageGrab
        screenshot = ImageGrab.grab(bbox=(left, top, left + chrome_window_width, top + chrome_window_height))

        # Save the screenshot
        screenshot.save("screenshot.png")

        print("Screenshot saved successfully.")
    else:
        print("No visible Chrome window found.")


# Example usage
if __name__ == "__main__":
    url_to_capture = "https://www.redbus.in/"  # Replace with the URL you want to capture
    take_website_screenshot(url_to_capture)


# Load the screenshot image
screenshot_path = 'screenshot.png'
screenshot = cv2.imread(screenshot_path)

# Perform OCR on the screenshot
reader = easyocr.Reader(['en'])
ocr_results = reader.readtext(screenshot)

# Expected text to compare against
expected_text = "India's No. 1 Online Bus Ticket Booking Site"

# Check if the expected text is present in the OCR results
text_found = is_text_present(ocr_results, expected_text)

# Output the result
if text_found:
    print(f"Expected text '{expected_text}' found in the screenshot.")
else:
    print(f"Expected text '{expected_text}' not found in the screenshot.")



"""
output :

C:\Users\ykannan\PycharmProjects\Pratice\.venv\Scripts\python.exe C:\Users\ykannan\PycharmProjects\Pratice\text.py 
Screenshot saved successfully.
Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.
Expected text 'India's No. 1 Online Bus Ticket Booking Site' found in the screenshot.

Process finished with exit code 0

"""