from datetime import datetime

import datetime
from itertools import cycle

from Gadgets.console_design import bcolors

myTime = datetime.datetime.now()
# print ("Current date and time : ")
print (myTime.strftime("%d/%m/%Y %H:%M:%S"))
# print (myTime.strftime("%A"))
day = datetime.date.today() + datetime.timedelta(days=1)
print(day)

# whileIndex = 0
# while whileIndex != 50:
#     day = datetime.date.today() + datetime.timedelta(days=whileIndex)
#     if day.strftime("%A") == "Sunday":
#         print(day.strftime("%d/%m/%Y"))
#     whileIndex +=1

# whileIndex = 0
# while whileIndex != 24:
#     print(whileIndex)
    # day = datetime.datetime.now() + datetime.timedelta(hours=whileIndex)
    # if day.strftime("%H") == "13":
    #     print(day.strftime("%d/%m/%Y %H:%M:%S"))
    # whileIndex +=1

# Date and time as datetime Class
final_upload_list = []

## PART 1
# Make a list of days to post
def setup_days2post():
    days2Post = input("Insert days to upload posts (by Order). \nSo 1 = Sunday"
                      "\nseparate with comma only (,)") or "1, 3, 4"
    days2Post = days2Post.replace(" ", "")  # Delete space
    int_days2Post_list = days2Post.split(",")
    int_days2Post_list = list(map(int, int_days2Post_list))  # ['1','2','3'] → [1,2,3]
    _days2Post_list = []
    for _int in int_days2Post_list:
        saturday = datetime.datetime(year=2021, month=1, day=30, hour=0,
                                     minute=00, second=00, microsecond=000000)  # AKA 0
        day2Post = saturday + datetime.timedelta(days=_int)
        _days2Post_list.append(day2Post.strftime("%A"))
    return _days2Post_list
days2Post_list = setup_days2post()
print("days2Post_list:")
print(*days2Post_list, sep=" | ")


## PART 2
# Create options of time_to_post based on selected hours ↓
hours_string = input("Insert hours (by Order) to upload posts on Upload Day. \nSo 14 = 14:00"
                     "\nseparate with comma only (,)") or "13, 16, 19"
hours_string = hours_string.replace(" ", "")  # Delete space
hours_list = hours_string.split(",")
hours_list = list(map(int, hours_list)) # ['1','2','3'] → [1,2,3]
hours_cycle = cycle(hours_list)
# posts_counter = 0
offset_days = 0
def next_custom_date_time():
    global offset_days
    # print(f"posts_counter = {posts_counter}")             # Current post / post per day
    _day_datetime = datetime.datetime.now() + datetime.timedelta(
        days=int(offset_days / len(hours_list)))
    _day = int(_day_datetime.strftime("%d"))
    month = datetime.datetime.now() + datetime.timedelta(
        days=int(offset_days / len(hours_list)))
    month = int(month.strftime("%m"))
    year = datetime.datetime.now() + datetime.timedelta(
        days=int(offset_days / len(hours_list)))
    year = int(year.strftime("%Y"))

    hour = next(hours_cycle)
    # print(f"hour = {hour}")
    # for hour in hours_to_upload:

    # print("days2Post_list")
    # print(days2Post_list)

    custom_date_time = datetime.datetime(year=year, month=month, day=_day, hour=hour,
                                         minute=00, second=00, microsecond=000000)
    # print(f"custom_date_time (time_to_post in global) =\n"
    #       f"{custom_date_time}\n")

    offset_days += 1
    return custom_date_time
# time_to_post.strftime("%d/%m/%Y %H:%M:%S")

## PART 3 - Not working yet!!
# Should return class<datetime> filtered by selected date
# Filter time_to_post based selected days (in part 1)
time_to_post = next_custom_date_time()
def day_filter():
    global time_to_post
    global offset_days
    while True:
        if time_to_post.strftime("%A") in days2Post_list:
            offset_days += 1
            break # Break while loop
        else:
            time_to_post = next_custom_date_time()
    return time_to_post
time_to_post2 = day_filter()
print(time_to_post2.strftime("%d/%m/%Y %H:%M:%S"))
print(time_to_post2.strftime("%A"))

print("[")
print(*final_upload_list, sep="\n")
print("]")

# print(datetime_object.strftime("%A"))
#1 Sunday
#2 Monday
#3 Tuesday
#4 Wednesday
#5 Thursday
#6 Friday
#7 Saturday

# upload_date = input("Which days to upload? (1 = Sunday) use comma (,)")
# hours_in_day = [12,13,14,15,
#                 16,17,18,19,
#                 20,21,22,22]
# posts_per_day = input("How much posts in a day?") or 3
# posts_per_day = int(posts_per_day)
# posts_per_day = 12/posts_per_day

# print(hours_in_day[::posts_per_day])

# posts_per_day = 4
# upload_time = 12/4 # = 3

# upload_dates = {{"Tuesday":[14,16,18]}}

# post_counters = {}
# for item in page_user_list:  # Until end of list...
#     print(item)
    # post_counters.update({
    #     item: {
    #         "static": 0,
    #         "updated": 0
    #     },
    # }
    # )
# print(post_counters)

## pip Schedule

import schedule
import time


def upload_example():
    print("Get post[0] from dict")
    print("Upload post[0]")
    print("Append post[0] to uploaded list")
    print("Remover post[0] from dict")

schedule.every(10).minutes.do(upload_example)
schedule.every().hour.do(upload_example)
schedule.every().day.at("10:30").do(upload_example)
schedule.every(5).to(10).minutes.do(upload_example)
schedule.every().monday.do(upload_example)
schedule.every().wednesday.at("12:46").do(upload_example)
schedule.every().minute.at(":17").do(upload_example)

while True:
    schedule.run_pending()
    time.sleep(1)