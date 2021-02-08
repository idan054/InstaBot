# from instascrape import * # Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
from instabot import Bot # urlgen Error Fix: Delete config or pip uninstall - install...
# Fix Tab/Space Errors: py -m tabnanny main.py # main.py as example
# fix Directory/file error: "../" refer to the def *runner* location run()

import os
import shutil

from Gadgets.console_design import bcolors
from myScripts.A2_New_post_downloader import actual_downloader
from myScripts.A1_Setup_usernames import setup_usernames
# Part A - Setup, Searching, Download
from myScripts.A3_Files_name_finder import name_finder
from myScripts.A5_Setup_post_details import setup_post
from myScripts.B1_Post_Uploader import actual_upload

if __name__ == '__main__':
    print(f"{bcolors.Yellow}Start{bcolors.Normal}")
    # downloaded_posts = 0
    # while downloaded_posts != 3...
    #     if... downloaded_posts += 1

    # 1 User Input usernames of Instagram Pages
    _profile_user_list = setup_usernames()

    _postPicker = input("Which post (relate to lasted) will be downloaded?\nDefault is 3rd. ") or 3
    _postPicker = int(_postPicker)

    slow_mode = input("Turn on slow mode (5 minutes wait between loops)?\Default is Y. (Y/n)") or True
    if slow_mode == "Y" or slow_mode == "y":
        slow_mode = True
    else: slow_mode = False

    def post_downloader():
        post_index = 0
        while 1 == 1:
            # if post_index != 0:
            print(f'{bcolors.Yellow}{bcolors.BOLD}'
                  f'posts in the list = {post_index} (AKA post_index)'
                  f'{bcolors.Normal}')

            # 2 looking for new posts & Download when found.
            _finalUserName = actual_downloader(profiles2check=_profile_user_list,
                                               postPicker=_postPicker,  # refer to lasted post (the 1st lasted might make more rights problems...)
                                               slow_mode=slow_mode)          # Wait 5 minutes between loops

            # 3 Get name of ThePost files
            _files_name = name_finder() #AKA "2021-01-29_10-15-52_UTC"

            # 4 fetch files to dict (dictionary list) and delete ThePost folder
            setup_post(page_profile=_finalUserName,
                       files_name=_files_name,
                       post_counter=post_index+1)  ## Start from 1
            post_index += 1 ## Start from 0
    post_downloader()

    #acttual_upload is inside def of post_upload who able to schedule and use the details files (post_1.py, 2021-01-30_22-05-44_UTC.jpg)
    # actual_upload(credit_user=_finalUserName, delete_post_folder=False)
    # Trying 5 times with While loop, who delete config folder + try upload post again

    print("Done.")
