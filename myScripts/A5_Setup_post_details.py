from datetime import date, datetime
import shutil
import json
from xopen import xopen
import glob
import os

def setup_post(page_profile, files_name, order_ReadyPost):
    try: os.mkdir('ReadyPosts')
    except: print("Directory already exist")

    Upload_date = date.today()
    Upload_time = datetime.now().strftime("%H:%M:%S") # 16:31:59
    next_minute = str(int(Upload_time[3:5]) + 1)
    Upload_time = Upload_time.replace(Upload_time[3:5], next_minute)

    txt_file = open(f'ThePost/{files_name}.txt').read()

    json_xz_file = xopen(f'ThePost/{files_name}.json.xz').read()
    json_xz_file = json.loads(json_xz_file)
    pic_link = json_xz_file["node"]["display_url"] # String

    txt_file = open(f'ThePost/{files_name}.txt').read()
    post_desc = f"{txt_file} \nToday's post credit: @{page_profile}"

    # Includes: Date, Time, Desc, username
    def file_creator():
        """Includes: Date, Time, Desc, username(page_profile),"""

        file = open(f"ReadyPosts/Post_{order_ReadyPost}.py", "w")

        file.write(f'# This is post "{order_ReadyPost}"\n\n')
        file.write(f'upload_date = "{Upload_date}"\n')
        file.write(f'upload_time = "{Upload_time}"\n')
        file.write(f'page_profile = "{page_profile}"\n')
        file.write(f'post_desc = "{post_desc}"\n')
        file.write(f"# Option A\n")
        file.write(f'pic_link = "{pic_link}"\n')
        file.write(f"# Option B\n")
        file.write(f"# Post{order_ReadyPost}.jpg in this directory...\n")

        file.close()
    file_creator()

    shutil.move(f"ThePost/{files_name}.jpg", f"ReadyPosts/post_{order_ReadyPost}.jpg")