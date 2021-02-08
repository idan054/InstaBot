from time import sleep
import instaloader
from Gadgets.console_design import bcolors, update_progress

from myScripts.A1_Setup_usernames import setup_usernames

global post_counter
global profile_page
global start_download
global current_username

# print("Start")
L = instaloader.Instaloader()
# Login or load session
# L.login("spider_modelsx", "Idan05423")        # (login)
L.load_session_from_file("spider_modelsx")

def actual_downloader(profiles2check, postPicker, slow_mode):
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
        if slow_mode: print(f"{bcolors.Yellow}Slow mode is ON!{bcolors.Normal}")
        if slow_mode and while_index != 0:
            # sleep(5*60)
            for sec in range(0, 60*5):
                sleep(1)
                update_progress(sec, 60*5)

        for current_username, post_counter in profiles2check.items():
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
                    print(f"\n {bcolors.Yellow}{bcolors.BOLD}New post Found!{bcolors.Normal}")
                    print('---------------------- \n post_counter["static"] != post_counter["updated"]')
                    print(' post_counter["static"] is ' + str(post_counter["static"]))
                    print(' post_counter["updated"] is ' + str(post_counter["updated"]) + "\n ----------------------")
                    start_download = True

                    # if בתוך הלולאה לשימוש בערכים
                    def download_lasted_post():
                        # global profile_page
                        # print("profile_page is")
                        # print(profile_page)

                        if start_download:  # = True
                            # למרות שיש צורך רק באיבור הראשון ברשימה
                            # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
                            forIndex = 1
                            for post in profile_page:
                                #S Not work for Private Account! (כי אין צורך להתחבר)
                                #S Takes time for multiple images/Videos
                                if forIndex != postPicker:  # כל מה שלא..
                                    # print(f"forIndex != postPicker"
                                    #       f"\n {forIndex} != {postPicker}")
                                    forIndex += 1 # So 3rd (example) recent post will download and not lasted post
                                elif forIndex == postPicker:
                                    print(f"{bcolors.Yellow}{bcolors.BOLD}"
                                          f"download the {postPicker}th lasted post...{bcolors.Normal}")
                                    # print(post.url)
                                    L.download_post(post, target="ThePost")  # שם התיקייה אליה ייוצאו הקבצים
                                    break

                            print(f"ThePost downloaded")
                    download_lasted_post()
            new_post_checker()
            # if to stop FOR loop
            if start_download:  break
        # if to stop WHILE loop
        if start_download:  break

        while_index += 1

    # print("start_download is " + str(start_download))
    print("-----------------")
    return current_username
