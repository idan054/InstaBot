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
the_username = "spider.models"

profile_page = instaloader.Profile.from_username(L.context, the_username).get_posts()
post_counter = profile_page.count
static_post_counter = profile_page.count # הגדר כמות פוסטים ראשונית

def new_post_checker():
    global post_counter
    global profile_page

    while static_post_counter == post_counter:  # ראשונית = עדכנית
        sleep(3)
        profile_page = instaloader.Profile.from_username(L.context, the_username).get_posts()
        post_counter = profile_page.count
        print("No new post yet...")
new_post_checker()

print("\n New post Found!")
print("---------------------- \n static_post_counter != post_counter")
print(" static_post_counter is " + str(static_post_counter))
print(" post_counter is " + str(post_counter) + "\n ----------------------")

def download_lasted_post():
    # למרות שיש צורך רק באיבור הראשון ברשימה
    # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
    for post in profile_page:
        # Not work for Private Account! (כי אין צורך להתחבר)
        # Takes time for multiple images/Videos
        L.download_post(post, target=the_username)  # שם התיקייה אליה ייוצאו הקבצים
        break
download_lasted_post()

