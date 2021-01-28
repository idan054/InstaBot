from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
import instaloader
# Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instascrape import *

print("Start")
L = instaloader.Instaloader()

profile_page = instaloader.Profile.from_username(L.context, "nike").get_posts()
print(profile_page.count)

# למרות שיש צורך רק באיבור הראשון ברשימה
# לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
for post in profile_page:
    # Not work for Private Account! (כי אין צורך להתחבר)
    L.download_post(post, target='Nike') # שם התיקייה אליה ייוצאו הקבצים
    break

