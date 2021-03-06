import os
import glob
import shutil
import urllib.request
from instabot import Bot
from Gadgets.console_design import bcolors


# post_details = {'1': {'page_profile': 'spider_modelsx', 'original_post_desc': 'caption_for_photo\n  post credit: @spider_modelsx\n', 'pic_link': 'https://instagram.fhfa1-1.fna.fbcdn.net/v/t51.2885-15/e35/150869913_1104238106665113_7779651190563703574_n.jpg?_nc_ht=instagram.fhfa1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=M3mDKMVaRs4AX-He2tq&tp=1&oh=d3384e81734d3781f7efcb2b15c7e513&oe=605D198E'}}

global bot
def upload_post(insta_user, insta_pass,
                pic_link, original_post_desc, page_profile,
                # post_details
                ):
    global bot
    # print("use value post_details instead pic_link, original_post_desc, page_profile,")
    # pic_link = post_details["1"]["pic_link"],
    # page_profile = post_details["1"]["page_profile"],
    # original_post_desc = post_details["1"]["original_post_desc"],

    # 0. delete config folder to login & Transform pic_link to .jpg
    def clean_start():
        try:
            shutil.rmtree('config')  # Delete config folder
            print(f"{bcolors.Yellow}{bcolors.BOLD}config folder has been deleted...{bcolors.Normal}")
        except:
            print(f"{bcolors.Yellow}{bcolors.BOLD}config folder not found...{bcolors.Normal}")

        # Download to local from web
        urllib.request.urlretrieve(f"{pic_link}", "LastedPhoto.jpg")
    clean_start()

    # 1. Try logging 3 times
    def instaLogin():
        global bot
        whileLogin = 0
        print("Try login...")
        while whileLogin < 3:
            try:
                bot = Bot()
                bot.login(username=insta_user, password=insta_pass)
                print(f"{bcolors.Yellow}{bcolors.BOLD}Successfully logged in{bcolors.Normal}")
                break
            except (ValueError, Exception):
                print("Delete config file...")
                shutil.rmtree('config')  # Delete config folder
                whileLogin += 1
                print("except, whileLogin = ", whileLogin)
        else:
            print(f"{bcolors.Red}{bcolors.BOLD}")
            print("logging to user failed")
            print("Already tried 3 times")
            print(f"{bcolors.Normal}")
    instaLogin()

    # 2. Try upload post 3 times
    def actual_upload():
        whileUpload = 0
        print("Try upload...")
        while whileUpload < 1:
            try:
                bot.upload_photo("LastedPhoto.jpg",
                                 caption=f"""{original_post_desc}
                                 post credit: @{page_profile}""")

                print(f"{bcolors.Yellow}{bcolors.BOLD}Post Uploaded{bcolors.Normal}")
                print('Delete "LastedPhoto.jpg.REMOVE_ME"')
                os.remove('LastedPhoto.jpg.REMOVE_ME')
                break
            except ValueError as e:
                whileUpload +=1
                print("except, whileUpload = ", whileUpload)
        else:
            print(f"{bcolors.Red}{bcolors.BOLD}")
            print("Post upload fail")
            print("Already tried 3 times")
            print(f"{bcolors.Normal}")
    actual_upload()

# Example to upload
# username_and_pass = input("Insert username & pass to upload separate with comma (,)") or "spider_modelsx, Idan05423"
# username_and_pass = username_and_pass.replace(" ", "")  # Delete space
# username_and_pass_list = username_and_pass.split(",")
# _insta_user = username_and_pass_list[0]
# _insta_pass = username_and_pass_list[1]
# print(_insta_pass, "\n", _insta_user)

# upload_post(insta_user=_insta_user, insta_pass=_insta_pass,
#             pic_link="https://instagram.fhfa1-1.fna.fbcdn.net/v/t51.2885-15/e35/144500141_156835686242663_4678927599306287928_n.jpg?_nc_ht=instagram.fhfa1-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=2aScVLiiCacAX_eQpfK&tp=1&oh=6c7404bbd96c484931bc200633aa18b7&oe=60567E9E",
#             original_post_desc="caption_for_photo",
#             page_profile="spider_modelsx")