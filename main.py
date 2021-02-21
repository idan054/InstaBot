# from instascrape import * # Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instabot import Bot # urlgen Error Fix: Delete config or pip uninstall - install...
# Fix Tab/Space Errors: py -m tabnanny main.py # main.py as example
# fix Directory/file error: "../" refer to the def *runner* location run()

from Gadgets.console_design import bcolors
from Gadgets.jsonPrinter import json_printer
from myScripts.A1_Setup_usernames import setup_usernames
from myScripts.A2_New_post_downloader import actual_downloader
from myScripts.A3_Files_name_finder import name_finder
from myScripts.A5_setup_post_details2 import setup_post
from myScripts.B1_Post_Uploader import upload_post

if __name__ == '__main__':
    print(f"{bcolors.Yellow}Start{bcolors.Normal}")

    global usernames_list, time2post_dict, postPicker, slow_mode

    ## 1 Get dynamic data from user
    # usernames_list, time2post_dict, postPicker, slow_mode
    def get_details():
        global usernames_list, time2post_dict, postPicker, slow_mode

        usernames_list = setup_usernames()

        from Gadgets.SheduleScripts.S1_Time2Post import setup_time2post
        # setup_days2post() + setup_hours2post() Runs from import
        time2post_dict = setup_time2post()
        json_printer(time2post_dict)

        postPicker = input("Which post (relate to lasted) will be downloaded?\nDefault is 3rd. ") or 3
        postPicker = int(postPicker)

        slow_mode = input("Turn on slow mode (5 minutes wait between loops)?\Default is Y. (Y/n)") or True
        if slow_mode == "Y" or slow_mode == "y":
            slow_mode = True
        else:
            slow_mode = False

        # return usernames_list, time2post_dict, postPicker, slow_mode
    get_details()

    ## 2 Track requested pages and export posts details to dict
    def pages_tracker():
        post_index = 0
        while 1 == 1:
            # if post_index != 0:
            print(f'{bcolors.Yellow}{bcolors.BOLD}'
                  f'posts in the list = {post_index} (AKA post_index)'
                  f'{bcolors.Normal}')

            ## 2 looking for new posts & Download when found.
            actual_downloader(profiles2check=usernames_list,
                               postPicker=postPicker,        # refer to lasted post (the 1st lasted might make more rights problems...)
                               slow_mode=slow_mode)          # Wait 5 minutes between loops

            ## 3 Get name of ThePost files
            _thePost_files_name = name_finder() # AKA "2021-01-29_10-15-52_UTC"

            ## 5 fetch files to dict (dictionary list) and delete ThePost folder
            ready2Post_dict = setup_post(
                       thePost_files_name=_thePost_files_name,
                       post_counter=post_index+1) # Start from 1

            post_index += 1 # Start from 0

            print("Upload 1st post in ready2Post_dict")
            upload_post(insta_user="spider_modelsx",
                        insta_pass="Idan05423",
                        page_profile=ready2Post_dict["1"]["page_profile"],
                        original_post_desc=ready2Post_dict["1"]["original_post_desc"],
                        pic_link=ready2Post_dict["1"]["pic_link"],
                            )
            uploaded_post_dict = {}
            uploaded_post_dict.update({
                f"1": {
                    "page_profile": ready2Post_dict["1"]["page_profile"],
                    "original_post_desc": ready2Post_dict["1"]["original_post_desc"],
                    "pic_link": ready2Post_dict["1"]["pic_link"],
                }
            }
            )
            print("\n uploaded_post_dict:")
            json_printer(uploaded_post_dict)
            del ready2Post_dict["1"]
            print(f"current post removed from ready2Post_dict")


            # schedule_job(someDay=current_day,
            #              someTime=current_hour,
            #              someDef=post_uploader(post details...))
    pages_tracker()

    # actual_upload is inside def of post_upload who able to schedule and use the details files (post_1.py, 2021-01-30_22-05-44_UTC.jpg)
    # actual_upload(credit_user=_finalUserName, delete_post_folder=False)
    # Trying 5 times with While loop, who delete config folder + try upload post again

    # How it should work...
    ## if dict datetime == current time -> upload this post
    ## else ->  keep working...
    print("Done.")
