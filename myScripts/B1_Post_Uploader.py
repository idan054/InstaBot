import shutil
from instabot import Bot
import glob
import os

def actual_upload(credit_user, delete_post_folder):
    picList = list(map(os.path.basename, glob.glob("ThePost/*jpg")))  # map(os.path.basename... for file name only (not path)
    # Full path
    # filesPath = glob.glob("..\ThePost\*jpg") #list of path files
    InstaPic = picList[0]  # TODO Make it fit to also multi photo post and video
    print(InstaPic)

    is_upload = False
    whileIndex = 0
    while not is_upload:
        whileIndex += 1
        print("Try Upload...")
        try:
            bot = Bot()
            bot.login(username="spider_modelsx", password="Idan05423")
            bot.upload_photo(f"ThePost/{InstaPic}", caption=f"credit for today's post: \n @{credit_user}")

            print("Post Uploaded")
            is_upload = True
            if delete_post_folder: shutil.rmtree('ThePost')  # Delete ThePost folder

        except:  # To fix urlgen common error
            shutil.rmtree('config')  # Delete config folder
            # is_upload still False (repeat while ↺)
        if whileIndex == 5:
            print("Post upload fail")
            print("Already tried 5 times")
            break
