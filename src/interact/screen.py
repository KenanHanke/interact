import pyautogui
from .wait import wait
from .constants import SCREENSHOTS_FOLDER



def click(screenshot_name):
    screenshot_path = SCREENSHOTS_FOLDER / screenshot_name
    screenshot_center = pyautogui.locateCenterOnScreen(str(screenshot_path), confidence=0.95)
    pyautogui.moveTo(*screenshot_center)
    wait(0.2)
    pyautogui.click(*screenshot_center)
    wait(2)


def click_if_exists(screenshot_name):
    try:
        click(screenshot_name)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def is_visible(screenshot_name):
    screenshot_path = SCREENSHOTS_FOLDER / screenshot_name
    try:
        return pyautogui.locateOnScreen(str(screenshot_path), confidence=0.95) is not None
    except pyautogui.ImageNotFoundException:
        return False
