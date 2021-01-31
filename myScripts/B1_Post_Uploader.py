from instabot import Bot
import glob
import os

def post_uploader(credit_user):
    picList = list(
        map(os.path.basename, glob.glob("ThePost/*jpg")))  # map(os.path.basename... for file name only (not path)
    # Full path
    # filesPath = glob.glob("..\ThePost\*jpg") #list of path files

    InstaPic = picList[0]  # TODO Make it fit to also multi photo post and video
    print(InstaPic)

    bot = Bot()
    bot.login(username="spider_modelsx", password="Idan05423")
    bot.upload_photo(f"ThePost/{InstaPic}", caption=f"credit for today's post: \n @{credit_user}")