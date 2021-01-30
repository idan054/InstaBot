from datetime import datetime
from itertools import dropwhile, takewhile
from datetime import date, timedelta
from time import sleep
import instaloader
# Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instascrape import *
# Tab Checker: py -m tabnanny main.py # main.py as example

def download_lasted_post(userFolder):

    if start_download:  # = True
        # למרות שיש צורך רק באיבור הראשון ברשימה
        # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
        for post in profile_page:
            # Not work for Private Account! (כי אין צורך להתחבר)
            # Takes time for multiple images/Videos
            L.download_post(post, target=userFolder)  # שם התיקייה אליה ייוצאו הקבצים
            break  # כדי שיוריד רק פוסט 1 (את העדכני ביותר)
        print("lasted post downloaded")

print("Start")
L = instaloader.Instaloader()
# Login or load session
# L.login("spider_modelsx", "Idan05423")        # (login)
L.load_session_from_file("spider_modelsx")

global profile_user_list
global post_counter
global profile_page
global start_download

def username_maker():
    """"Setup the Instagram pages based user Input"""
    global profile_user_list

    # region Static Template

    # profile_user_list = {
    #     # Key = profile name #Value = post count
    # 	"spider.models": {
    # 		"static": 0,
    # 		"updated": 0
    # 	},
    # 	"nike": {
    # 		"static": 0,
    # 		"updated": 0
    # 	},
    # 	"stabilo": {
    # 		"static": 0,
    # 		"updated": 0
    # 	}
    # }
    # # print (profile_user_list["nike"]["updated"])
    # print (profile_user_list["stabilo"]["updated"])
    # print(profile_user_list)

    # endregion Static Template

    user_input = input("Paste page usernames, separate with comma only (,)")
    user_input = user_input.replace(" ", "")  # Delete space
    page_user_list = user_input.split(",")

    # List of strings
    # page_user_list = ["nike", "dainwalker", "_trash_baby"]

    # List of ints
    post_counters = []
    for _ in page_user_list:
        post_counters.append(
            {
                "static": 0,
                "updated": 0
            },
        )
    # print(post_counters)

    # Create a zip object from two lists
    full_page = zip(page_user_list, post_counters)
    profile_user_list = dict(full_page)
    print(profile_user_list)
    # return profile_user_list
username_maker()

def auto_new_post_downloader():
    """"Looking for new post on Instagram pages based username_maker() pre set"""

    global profile_user_list
    global post_counter
    global profile_page
    global start_download

    start_download = False
    while_index = 0
    # while Loop until post downloaded
    while not start_download:  # while start_download = False
        print(f"current loop: {while_index}")
        for current_username, post_counter in profile_user_list.items():
            # מידע על הפוסטים עבור המשתמש הנוכחי בלולאת פור
            print(f'Start for loop "{current_username}"')
            if while_index == 0:
                # הגדר כמות פוסטים ראשונית בסבב while הראשון בלבד
                profile_page = instaloader.Profile.from_username(L.context, current_username).get_posts()
                post_counter["static"] = profile_page.count
                print('» post_counter["static"] is ' + str(post_counter["static"]) + " « ")
                pass
            else:
                print(' --- post_counter["static"] is ' + str(post_counter["static"]) + " --- ")

            # print("start new_post_checker")
            def new_post_checker():
                global post_counter
                global profile_page
                global start_download
                sleep(1)
                # עדכון של המידע על הפוסטים לאחר המתנה
                profile_page = instaloader.Profile.from_username(L.context, current_username).get_posts()
                post_counter["updated"] = profile_page.count

                # print(' post_counter["static"] is ' + str(post_counter["static"]))
                print('  post_counter["updated"] is ' + str(post_counter["updated"]))
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

                    # if בתוך הלולאה לשימוש בערכים
                    if start_download: # is True
                        download_lasted_post(current_username)

            # if for stop for loop
            if start_download:
                break

            new_post_checker()
            # print(f'Done for loop "{current_username}"' )

        while_index += 1
auto_new_post_downloader()

# async def async_test():
#     await auto_new_post_downloader()
#     print("Finish?")
