from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
from time import sleep

import instaloader
# Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instascrape import *

print("Start")
L = instaloader.Instaloader()
start_download = False
# profile_user_list = {
#   # "current_username" | "post_counter" (השמות בלולאת פור)
#     "spider.models" : [0, 0], # Static, Updated
#     "nike" : [0, 0],
#     "stabilo" : [0, 0],
# }

profile_user_list = {
    # Key = profile name #Value = post count
	"spider.models": {
		"static": 0,
		"updated": 0
	},
	"nike": {
		"static": 0,
		"updated": 0
	},
	"stabilo": {
		"static": 0,
		"updated": 0
	}
}
# print (profile_user_list["nike"]["updated"])
# print (profile_user_list["stabilo"]["updated"])

# user_index = 0
for current_username, post_counter in profile_user_list.items():
    # מידע על הפוסטים עבור המשתמש הנוכחי בלולאת פור
    print(f'Start for loop "{current_username}"')
    profile_page = instaloader.Profile.from_username(L.context, current_username).get_posts()
    # הגדר כמות פוסטים ראשונית
    post_counter["static"] = profile_page.count

    def new_post_checker():
        global post_counter
        global profile_page
        global start_download
        sleep(3)
        # עדכון של המידע על הפוסטים לאחר המתנה
        profile_page = instaloader.Profile.from_username(L.context, current_username).get_posts()
        post_counter["updated"] = profile_page.count

        print(' post_counter["static"] is ' + str(post_counter["static"]))
        print(' post_counter["updated"] is ' + str(post_counter["updated"]))
        print("----------------------")
        # בודק אם נוסף פוסט חדש
        if post_counter["static"] == post_counter["updated"]:
            print("No new post yet...")
        else:
            print("\n New post Found!")
            print('---------------------- \n post_counter["static"] != post_counter["updated"]')
            print(' post_counter["static"] is ' + str(post_counter["static"]))
            print(' post_counter["updated"] is ' + str(post_counter["updated"]) + "\n ----------------------")
            start_download = True
    new_post_checker()
    print(f'Done for loop "{current_username}"' )

def download_lasted_post():
    global start_download
    if start_download: # = True
        # למרות שיש צורך רק באיבור הראשון ברשימה
        # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
        for post in profile_page:
            # Not work for Private Account! (כי אין צורך להתחבר)
            # Takes time for multiple images/Videos
            L.download_post(post, target=current_username)  # שם התיקייה אליה ייוצאו הקבצים
            break
download_lasted_post()