from datetime import date, datetime
import shutil
import json
from xopen import xopen
import glob
import os

from Gadgets.console_design import bcolors

readyPost_dict = {}
def setup_post(page_profile, files_name, post_counter, time_to_post):
    global readyPost_dict
    # try: os.mkdir('ReadyPosts')
    # except: print("Directory already exist")

    # txt_file = open(f'ThePost/{files_name}.txt').read()

    json_xz_file = xopen(f'ThePost/{files_name}.json.xz').read()
    json_xz_file = json.loads(json_xz_file)
    pic_link = json_xz_file["node"]["display_url"] # String
    time_to_post_float = datetime.timestamp(time_to_post)
    time_to_post_string = time_to_post.strftime("%d/%m/%Y %H:%M:%S")
    try:
        original_post_desc = open(f'ThePost/{files_name}.txt').read()
    except:
        original_post_desc = "" # When desc unavailable

    def dict_editor():
        global readyPost_dict
        readyPost_dict.update({
            post_counter: {
                "page_profile": page_profile,
                "original_post_desc": original_post_desc,
                "pic_link": pic_link,
                "time_to_post_string": time_to_post_string,
                "time_to_post_float": time_to_post_float
            }
          }
        )
        print(f"\n\n{bcolors.Blue}{bcolors.BOLD}"
              f"readyPost_dict = {readyPost_dict}{bcolors.Normal}\n\n")
    dict_editor()

    shutil.rmtree('ThePost') # Based on main.py
    # shutil.move(f"ThePost/{files_name}.jpg", f"ReadyPosts/post_{post_counter}.jpg")

    # Export dict to json
    with open('posts_result.json', 'w') as json_file:
        json.dump(readyPost_dict, json_file)
