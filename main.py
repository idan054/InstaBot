# from myScripts.newPostChecker import setupPagesUsers, new_post_checker
import instaloader

print("Start")
L = instaloader.Instaloader()
# Login or load session
# L.login("spider_modelsx", "Idan05423")        # (login)
L.load_session_from_file("spider_modelsx")

#1 User Input usernames of Instagram Pages
# setupPagesUsers()

#2 Python keep looking for new posts in all the Insta pages
# new_post_checker(L)

#3