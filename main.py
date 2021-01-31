# from instascrape import * # Full Details: https://github.com/chris-greening/instascrape And https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# Fix Tab/Space Errors: py -m tabnanny main.py # main.py as example
from myScripts.B_New_post_downloader import new_post_downloader
from myScripts.A_Setup_usernames import setup_usernames

# 1 User Input usernames of Instagram Pages
_profile_user_list = setup_usernames()

#2 looking for new posts & Download when found.
_start_download, _finalUserName = new_post_downloader(_profile_user_list)

print("••••••••••••••••••••••")
print(">> start_download is " + str(_start_download))
print(">> finalUserName is " + str(_finalUserName))
