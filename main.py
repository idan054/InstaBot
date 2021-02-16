# from instascrape import * # Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instabot import Bot # urlgen Error Fix: Delete config or pip uninstall - install...
# Fix Tab/Space Errors: py -m tabnanny main.py # main.py as example
# fix Directory/file error: "../" refer to the def *runner* location run()

import os
import shutil
import json
from Gadgets.console_design import bcolors
from myScripts.A1_Setup_usernames import setup_usernames
from myScripts.A2_New_post_downloader import actual_downloader
from myScripts.A3_Files_name_finder import name_finder
from myScripts.A4_Post_Shedule import setup_hours2post, next_custom_date_time  # , setup_days2post
from myScripts.A5_Setup_post_details import setup_post
from myScripts.B1_Post_Uploader import actual_upload

if __name__ == '__main__':
    print(f"{bcolors.Yellow}Start{bcolors.Normal}")

    global usernames_list, hours2post_list, \
        hours2post_cycle, slow_mode, postPicker

    ## Get dynamic data from user
    # usernames, time to upload, slow mode and which post to upload
    def get_details():
        global usernames_list, hours2post_list, \
            hours2post_cycle, slow_mode, postPicker

        usernames_list = setup_usernames()

        hours2post_list, hours2post_cycle = setup_hours2post()

        postPicker = input("Which post (relate to lasted) will be downloaded?\nDefault is 3rd. ") or 3
        postPicker = int(postPicker)

        slow_mode = input("Turn on slow mode (5 minutes wait between loops)?\Default is Y. (Y/n)") or True
        if slow_mode == "Y" or slow_mode == "y":
            slow_mode = True
        else:
            slow_mode = False

        return usernames_list, hours2post_list, hours2post_cycle, postPicker, slow_mode
    get_details()

    ## Track requested pages and export posts to json
    # The json include time to upload the post
    def pages_tracker():
        post_index = 0
        while 1 == 1:
            # if post_index != 0:
            print(f'{bcolors.Yellow}{bcolors.BOLD}'
                  f'posts in the list = {post_index} (AKA post_index)'
                  f'{bcolors.Normal}')

            # 2 looking for new posts & Download when found.
            _finalUserName = actual_downloader(profiles2check=usernames_list,
                                               postPicker=postPicker,        # refer to lasted post (the 1st lasted might make more rights problems...)
                                               slow_mode=slow_mode)          # Wait 5 minutes between loops

            # 3 Get name of ThePost files
            _files_name = name_finder() #AKA "2021-01-29_10-15-52_UTC"

            # 4 Make a datetime to post
            _time_to_post = next_custom_date_time(hours2post_list, hours2post_cycle, post_index)
            print(_time_to_post)

            # 4 fetch files to dict (dictionary list) and delete ThePost folder
            setup_post(page_profile=_finalUserName,
                       files_name=_files_name,
                       post_counter=post_index+1, # Start from 1
                       time_to_post=_time_to_post)
            post_index += 1 # Start from 0
    pages_tracker()

    # actual_upload is inside def of post_upload who able to schedule and use the details files (post_1.py, 2021-01-30_22-05-44_UTC.jpg)
    # actual_upload(credit_user=_finalUserName, delete_post_folder=False)
    # Trying 5 times with While loop, who delete config folder + try upload post again

    # How it should work...
    ## if dict datetime == current time -> upload this post
    ## else ->  keep working...
    print("Done.")
