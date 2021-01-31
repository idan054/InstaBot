from time import sleep
import instaloader

from myScripts.A_Setup_usernames import setup_usernames

global post_counter
global profile_page
global start_download
global current_username

print("Start")
L = instaloader.Instaloader()
# Login or load session
# L.login("spider_modelsx", "Idan05423")        # (login)
L.load_session_from_file("spider_modelsx")

def new_post_downloader(profile_user_list):
    """"Looking for new post on Instagram pages based username_maker() pre set"""

    global post_counter
    global profile_page
    global start_download
    global current_username

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
                    def download_lasted_post(userFolder):
                        # global finalUserName
                        if start_download:  # = True
                            # למרות שיש צורך רק באיבור הראשון ברשימה
                            # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
                            for post in profile_page:
                                # Not work for Private Account! (כי אין צורך להתחבר)
                                # Takes time for multiple images/Videos
                                L.download_post(post, target=userFolder)  # שם התיקייה אליה ייוצאו הקבצים
                                break  # כדי שיוריד רק פוסט 1 (את העדכני ביותר)
                            print("lasted post downloaded")
                            return userFolder
                    download_lasted_post(current_username)
            new_post_checker()
            # if to stop FOR loop
            if start_download:  break
        # if to stop WHILE loop
        if start_download:  break

        while_index += 1

    print("start_download is " + str(start_download))
    return start_download, current_username
