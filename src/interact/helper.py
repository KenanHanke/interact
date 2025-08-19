#!/usr/bin/env python3

from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
from pathlib import Path

from .constants import SCREENSHOTS_FOLDER, SYSTEM_SCREENSHOTS_FOLDER
from . import screen


def main():
    SCREENSHOTS_FOLDER.mkdir(parents=True, exist_ok=True)
    for new_file in watch_new_files(SYSTEM_SCREENSHOTS_FOLDER):
        if new_file.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            screenshot_name = new_file.name
            new_file.rename(SCREENSHOTS_FOLDER / screenshot_name)
            sleep(0.5)  # allow time for screenshot UI to disappear
            if screen.click_if_exists(screenshot_name):
                print(f"Moved and clicked on screenshot: {screenshot_name}")
            else:
                print(f"Moved screenshot but could not click: {screenshot_name}")
        else:
            print(f"Skipped non-image file: {new_file.name}")


def watch_new_files(folder_path):
    """
    Generator that yields the full path of files as they appear in folder_path.
    """
    folder = Path(folder_path).resolve()
    if not folder.is_dir():
        raise ValueError(f"{folder_path} is not a valid directory")

    class NewFileHandler(FileSystemEventHandler):
        def __init__(self):
            self._new_files = []

        def on_created(self, event):
            # If the created item is a file (not a directory), append to the list
            if not event.is_directory:
                self._new_files.append(Path(event.src_path))

        def pop_new_files(self):
            files, self._new_files = self._new_files, []
            return files

    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(folder), recursive=False)
    observer.start()

    try:
        while True:
            # Get any newly created files and yield them
            for new_file in event_handler.pop_new_files():
                yield Path(new_file).resolve()
            sleep(0.1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
