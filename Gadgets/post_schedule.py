from datetime import datetime

import datetime
from itertools import cycle
myTime = datetime.datetime.now()
# print ("Current date and time : ")
# print (myTime.strftime("%d/%m/%Y %H:%M:%S"))
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
hours_string = input("Insert hours to upload posts on Upload Day. \nSo 14 = 14:00"
                     "\nseparate with comma only (,)") or "13, 16, 19"
hours_string = hours_string.replace(" ", "")  # Delete space
hours_list = hours_string.split(",")
hours_list = list(map(int, hours_list)) # ['1','2','3'] → [1,2,3]
hours_cycle = cycle(hours_list)
scheduled_posts_counter = 0
def post_schedule():
    global scheduled_posts_counter
    print(f"defIndex = {scheduled_posts_counter}")             # Current post / post per day
    myDay = datetime.datetime.now() + datetime.timedelta(days=int(scheduled_posts_counter / len(hours_list)))
    myDay = int(myDay.strftime("%d"))
    month = datetime.datetime.now() + datetime.timedelta(days=int(scheduled_posts_counter / len(hours_list)))
    month = int(month.strftime("%m"))
    year = datetime.datetime.now() + datetime.timedelta(days=int(scheduled_posts_counter / len(hours_list)))
    year = int(year.strftime("%Y"))

    hour = next(hours_cycle)
    # print(f"hour = {hour}")
    # for hour in hours_to_upload:
    custom_date_time = datetime.datetime(year=year, month=month, day=myDay, hour=hour,
                                         minute=00, second=00, microsecond=000000)
    print(custom_date_time)
    scheduled_posts_counter += 1
    return custom_date_time

time_to_post = post_schedule()

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