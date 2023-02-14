import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

fromdir = "C:/Users/localuser/Downloads"
todir="C:/Users/localuser/Downloads/downloaded_files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path) 
        for key,value in dir_tree.items():
            if extension in value:
                fileName=os.path.basename(event.src_path)
                print("downloaded ",fileName)
                path1=fromdir+"/"+fileName
                path2=todir+"/"+key
                path3=todir+"/"+key+"/"+fileName
                time.sleep(3)
                if os.path.exists(todir+"/"+key):
                    if os.path.exists(path2):
                        print("moving",+fileName+"...")
                        shutil.move(path1,path3)
                        time.sleep(1)
                    else:
                        print("making directory")
                        os.makedirs(path2)
                        print("moving",+fileName+"...")
                        shutil.move(path1,path3)
                        time.sleep(1)
    #name,extension=os.path.splitext(event.src_path)
# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, fromdir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("dont touch the keyboard or i leak your address")
    observer.stop()