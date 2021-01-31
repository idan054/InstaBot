# from instascrape import * # Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# Fix Tab/Space Errors: py -m tabnanny main.py # main.py as example
import shutil
from instabot import Bot # urlgen Error Fix: Delete config or pip uninstall - install...
from myScripts.A2_New_post_downloader import new_post_downloader
from myScripts.A1_Setup_usernames import setup_usernames

# Part A - Setup, Searching, Download
from myScripts.B1_Post_Uploader import post_uploader

if __name__ == '__main__':
    print("Start")

    # 1 User Input usernames of Instagram Pages
    _profile_user_list = setup_usernames()

    # 2 looking for new posts & Download when found.
    _finalUserName = new_post_downloader(profiles2check=_profile_user_list, postPicker=3)
    # postPicker means Which post to download refer to lasted post (lasted might make more rights problems...)

    # global is_upload
    is_upload = False
    def aggressive_post_upload():
        global is_upload
        print("Try Upload...")
        try:
            post_uploader(credit_user=_finalUserName)
            is_upload = True
            shutil.rmtree('ThePost')  # Delete ThePost folder
        except:
            shutil.rmtree('config')  # Delete config folder
            is_upload = False
    while not is_upload: aggressive_post_upload()

    print("Done")
