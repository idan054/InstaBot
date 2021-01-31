from instapy_cli import client

# region LOGIN-DEFAULT

# from instapy_cli import client
# username = 'spider_modelsx'
# password = 'Idan05423'
# with client(username, password) as cli:
    # do stuffs with cli
    # ig = cli.api()
    # print(ig.current_user())

# endregion LOGIN-DEFAULT-

# region LOGIN-COOKIE-MAKER

from instapy_cli import client

username = 'spider_modelsx'
password = 'Idan05423'
cookie_file = 'COOKIE_FOR_USER.json' # default: `USERNAME_ig.json`

with client(username, password, cookie_file=cookie_file, write_cookie_file=True) as cli:
    # get string cookies
    cookies = cli.get_cookie()
    print(type(cookies)) # == str
    print(cookies)
    # do stuffs with cli
    ig = cli.api()
    me = ig.current_user()
    print(me)

# endregion

# region LOGIN-USING-COOKIE
# from instapy_cli import client
#
# username = 'USERNAME'
# password = 'PASSWORD'
# cookie = '{COOKIE_STRING_JSON_OBJ}'
#
# with client(username, password, cookie=cookie) as cli:
#     get string cookies
    # cookies = cli.get_cookie()
    # print(type(cookies)) # == str
    # print(cookies)
    # do stuffs with cli
    # ig = cli.api()
    # me = ig.current_user()
    # print(me)
# region LOGIN-USING-COOKIE

# username = 'spider_modelsx'
# password = 'Idan05423'
# image = '/instagram/2021-01-29_22-06-08_UTC.jpg'
# text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'
#
# with client(username, password) as cli:
#     cli.upload(image, text)

from InstagramAPI import InstagramAPI

api = InstagramAPI("spider_modelsx", "Idan05423")
api.login() # login
api.tagFeed("cat") # get media list by tag #cat
media_id = api.LastJson # last response JSON
api.like(media_id["ranked_items"][0]["pk"]) # like first media
api.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers

# username = 'spider_modelsx' #your username
# password = 'Idan05423' #your password
# image = '/instagram/2021-01-29_22-06-08_UTC.jpg' #here you can put the image directory
# text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'
# with client(username, password) as cli:
#     cli.upload(image, text)
