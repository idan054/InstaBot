from datetime import date, datetime
import shutil
import json
from xopen import xopen
import glob
import os

# Remove any ending AKA jpg, png, mp4
def ending_remover(theString):
    erase_letters = False
    for letter in theString:
        if erase_letters:
            # print(f"Im will be deleted: {letter}")
            theString = theString.replace(letter, "")

        if not letter == ".":
            continue
        else:  # When dot. found
            erase_letters = True
            # print(f"Im will be deleted: {letter}")
            theString = theString.replace(letter, "")
    return theString
    # To use: some_string = ending_remover(some_string)

def name_finder():
    # file_name = map(os.path.basename...
    picList = list(map(os.path.basename, glob.glob("ThePost/*txt")))  # List
    # full_path = glob.glob("..\ThePost\*jpg") #list of path files
    full_pic_name = picList[0]  # String #TODO Make it fit to also multi photo post and video

    _files_name = ending_remover(full_pic_name)
    print(f"files_name : {_files_name}")
    return _files_name