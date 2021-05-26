from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_downloaded):
            src = folder_downloaded + "/" + filename
            new_destination = new_destination + "/" + filename
            os.rename(src, new_destination)

folder_downloaded = "/Users/karee/Downloads"
new_destination = "/Users/karee/Desktop"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_downloaded, recursive = True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
