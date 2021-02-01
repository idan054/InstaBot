import shutil
from instabot import Bot
import glob
import os

# map(os.path.basename... for file name only (not path)
picList = list(map(os.path.basename, glob.glob("ThePost/*jpg")))
# Full_path = glob.glob("..\ThePost\*jpg") #list of path files

files_name = picList[0]  # TODO Make it fit to also multi photo post and video

# Remove any ending AKA jpg, png, mp4
def ending_remover(theString):
    global files_name
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
files_name = ending_remover(files_name)
print(files_name)
