import subprocess

from .wait import wait
import pyperclip


def press(key):
    """
    Press a specific key using xdotool, e.g., "Tab", "Escape", "ctrl+c", etc.
    """
    subprocess.run(["xdotool", "key", key])
    wait(2)


def press_enter():
    """
    Same as press_key("Return"); uses xdotool to press enter.
    """
    press("Return")


def paste_here(text):
    pyperclip.copy(text)
    press("ctrl+v")


def switch_to_last_workspace():
    """
    Switch to the last workspace using xdotool.
    """
    try:
        num = int(subprocess.check_output(['xdotool', 'get_num_desktops']).strip())
        subprocess.run(['xdotool', 'set_desktop', str(num - 1)])
        wait(2)
        return
    except Exception:
        pass
    
    try:
        output = subprocess.check_output(['wmctrl', '-d']).decode()
        num = len(output.splitlines())
        rightmost = num - 1
        subprocess.run(['wmctrl', '-s', str(rightmost)])
        wait(2)
        return
    except Exception:
        pass

    raise RuntimeError("Failed to switch to last workspace. Please check your desktop environment and xdotool installation.")
