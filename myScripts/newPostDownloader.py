# Fix Error ImportError: cannot import name:
# Use Variables in the Def instead trying import variable from one file to another with the def

# global profile_user_list
# global post_counter
# global profile_page
# global start_download
# global L


def download_lasted_post(
        current_username,
        start_download,
        profile_page,
        L ):
# def download_lasted_post():
    print("start download_lasted_post()")

    if start_download:  # = True
        # למרות שיש צורך רק באיבור הראשון ברשימה
        # לא ניתן לוותר על הלולאה (ולהשתמש בערך כרשימה[0])
        for post in profile_page:
            # Not work for Private Account! (כי אין צורך להתחבר)
            # Takes time for multiple images/Videos
            L.download_post(post, target=current_username)  # שם התיקייה אליה ייוצאו הקבצים
            break  # כדי שיוריד רק פוסט 1 (את העדכני ביותר)
        print("lasted post downloaded")