from datetime import date, datetime
import shutil
import json
from xopen import xopen
import glob
import os

from Gadgets.console_design import bcolors
from Gadgets.jsonPrinter import json_printer

ready2Post_dict = {}
def setup_post(thePost_files_name, post_counter):
    global ready2Post_dict

    json_xz_file = xopen(f'ThePost/{thePost_files_name}.json.xz').read()
    json_xz_file = json.loads(json_xz_file)
    pic_link = json_xz_file["node"]["display_url"] # String
    username = json_xz_file["node"]["owner"]["username"]

    try:
        original_post_desc = open(f'ThePost/{thePost_files_name}.txt').read()
    except (ValueError, Exception):
        original_post_desc = "" # When desc unavailable

    def dict_editor():
        global ready2Post_dict
        ready2Post_dict.update({
            f"{post_counter}": {
                "page_profile": username,
                "original_post_desc": original_post_desc,
                "pic_link": pic_link,
            }
          }
        )
    dict_editor()

    print("ready2Post_dict:")
    json_printer(ready2Post_dict)
    return ready2Post_dict

    # Delete ThePost folder
    # shutil.rmtree('ThePost') # Based on main.py
    # shutil.move(f"ThePost/{files_name}.jpg", f"ReadyPosts/post_{post_counter}.jpg")