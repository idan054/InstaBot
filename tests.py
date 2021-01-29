from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
from time import sleep
import instaloader
# Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instascrape import *
from pandas.tests.tseries.frequencies.test_inference import day

# L = instaloader.Instaloader()
#
# posts = instaloader.Profile.from_username(L.context, "instagram").get_posts()
#
# SINCE = datetime(2021, 1, 20)
# UNTIL = datetime(2021, 1, 29)
#
# for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
#     print(post.date)
#     L.download_post(post, "instagram")



print("Start")
L = instaloader.Instaloader()

the_username = "spider.models"
profile_page = instaloader.Profile.from_username(L.context, the_username).get_posts()

# למרות שיש צורך רק באיבור הראשון ברשימה
# לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
for post in profile_page:
    # Not work for Private Account! (כי אין צורך להתחבר)
    # Takes time for multiple images/Videos
    L.download_post(post, target=the_username)  # שם התיקייה אליה ייוצאו הקבצים
    break