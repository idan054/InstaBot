from datetime import date, datetime
import shutil
import json
from xopen import xopen
import glob
import os

from Gadgets.console_design import bcolors

ready2Post_dict = {}
def setup_post(page_profile, thePost_files_name, post_counter):
    global ready2Post_dict

    json_xz_file = xopen(f'ThePost/{thePost_files_name}.json.xz').read()
    json_xz_file = json.loads(json_xz_file)
    pic_link = json_xz_file["node"]["display_url"] # String
    try:
        original_post_desc = open(f'ThePost/{thePost_files_name}.txt').read()
    except (ValueError, Exception):
        original_post_desc = "" # When desc unavailable

    def dict_editor():
        global ready2Post_dict
        ready2Post_dict.update({
            post_counter: {
                "page_profile": page_profile,
                "original_post_desc": original_post_desc,
                "pic_link": pic_link,
            }
          }
        )
        print(f"\n\n{bcolors.Blue}{bcolors.BOLD}"
              f"readyPost_dict = {ready2Post_dict}{bcolors.Normal}\n\n")
    dict_editor()

    # Delete ThePost folder
    # shutil.rmtree('ThePost') # Based on main.py
    # shutil.move(f"ThePost/{files_name}.jpg", f"ReadyPosts/post_{post_counter}.jpg")