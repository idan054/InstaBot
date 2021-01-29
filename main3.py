from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
from time import sleep

import instaloader
# Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instascrape import *

print("Start")
L = instaloader.Instaloader()

# username = input("Paste profile username: ")
# the_username = "spider.models"
# another_username = "nike"
profile_user_list = [{"spider.models" : 0}, {"nike" : 0}, {"stabilo" : 0}]

# הגדרת מצב ראשוני
overall_post_count = 0
updated_post_count = 0
for current_profile in profile_user_list: # עבודה על המשתמש
    profile_page = instaloader.Profile.from_username(L.context, current_profile).get_posts()
    overall_post_count += profile_page.count
    updated_post_count += profile_page.count
print("overall_post is " + str(overall_post_count))

# profile_page = instaloader.Profile.from_username(L.context, the_username).get_posts()
# post_counter = profile_page.count
# static_post_counter = profile_page.count # הגדר כמות פוסטים ראשונית

def new_post_checker():
    global post_counter
    global profile_page
    global updated_post_count

    while overall_post_count == updated_post_count:  # ראשונית = עדכנית
        print("No new post yet..."), sleep(0.2)
        print("Start new While!"), sleep(0.2)
        print("overall is " + str(overall_post_count) + " updated is " + str(updated_post_count) + "\n")
        sleep(3)
        updated_post_count = 0 # ה while לא עוצר מפני שהסבב אינו נגמר
        for current_profile in profile_user_list:  # עבודה על המשתמש
            print("Updating updated_post_count...")
            print("Calculate new user...")
            profile_page = instaloader.Profile.from_username(L.context, current_profile).get_posts()
            updated_post_count += profile_page.count

    else:
        print("\n New post Found!")
        print("---------------------- \n overall_post_count != updated_post_count")
        print(" overall_post_count is " + str(overall_post_count))
        print(" updated_post_count is " + str(updated_post_count) + "\n ----------------------")
new_post_checker()



def download_lasted_post():
    # למרות שיש צורך רק באיבור הראשון ברשימה
    # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
    for post in profile_page:
        # Not work for Private Account! (כי אין צורך להתחבר)
        # Takes time for multiple images/Videos
        L.download_post(post, target="the_username")  # שם התיקייה אליה ייוצאו הקבצים
        break
download_lasted_post()