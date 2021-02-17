import shutil
from instabot import Bot
import glob
import os

from Gadgets.console_design import bcolors


username_and_pass = input("Insert username & pass to upload separate with comma (,)") or "spider_modelsx, Idan05423"
username_and_pass = username_and_pass.replace(" ", "")  # Delete space
username_and_pass_list = username_and_pass.split(",")
_insta_user = username_and_pass_list[0]
_insta_pass = username_and_pass_list[1]
print(_insta_pass, "\n", _insta_user)

def actual_upload(insta_user, insta_pass, pic_link,
                  original_post_desc,
                  page_profile):
    is_upload = False
    whileIndex = 0
    while not is_upload:
        whileIndex += 1
        print(f"Try Upload ({whileIndex})...")
        try:
            bot = Bot()
            bot.login(username=insta_user, password=insta_pass)
            bot.upload_photo(pic_link,
                             caption=f"""
                             {original_post_desc}
                             credit for today's post: @{page_profile}""")

            print(f"{bcolors.Yellow}{bcolors.BOLD}Post Uploaded{bcolors.Normal}")
            is_upload = True

        except:  # To fix urlgen common error
            shutil.rmtree('config')  # Delete config folder
                # is_upload still False (repeat while loop ↺)
        if whileIndex == 5:
            print(f"{bcolors.Red}{bcolors.BOLD}")
            print("Post upload fail")
            print("Already tried 5 times")
            print(f"{bcolors.Normal}")
            break

actual_upload(insta_user=_insta_user, insta_pass=_insta_pass,
              pic_link="https://instagram.fhfa1-1.fna.fbcdn.net/v/t51.2885-15/e35/144500141_156835686242663_4678927599306287928_n.jpg?_nc_ht=instagram.fhfa1-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=2aScVLiiCacAX_eQpfK&tp=1&oh=6c7404bbd96c484931bc200633aa18b7&oe=60567E9E",
              original_post_desc="caption_for_photo",
              page_profile="spider_modelsx")
