# Interact

Requires `xdotool` and `xclip`

## Installation

```bash
pip install git+https://github.com/KenanHanke/interact@main
```

## Usage

```python
# Same as `from interact import *`
from interact import keyboard, screen, wait

keyboard.press("ctrl+n")
keyboard.press_enter()
keyboard.paste_here("Hello, World!")
keyboard.switch_to_last_workspace()

screen.click("image.png")
screen.click_if_exists("button.png")
screen.is_visible("element.png")

wait(5)  # Waits 5 to 6 seconds
```

The `screen` submodule expects a `screenshots` directory in the current working directory.
The click functions click the center of the first occurrence of the image on the screen.

You can also run `python -m interact.helper` directly in order to monitor the
`~/Pictures/Screenshots` directory, automatically move new screenshots to
`./screenshots`, and try to click them right away. The use case for this is
creating a new UI interaction script, as this tests right away if the
screenshots are correct and clickable.

The `wait` function sleeps between 100% and 120% of the total seconds given,
which can help avoid detection by anti-bot systems.
