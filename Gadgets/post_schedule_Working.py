from datetime import datetime
import datetime
from itertools import cycle

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
print(*days2Post_list, sep="\n")


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
time_to_post = next_custom_date_time()
print(time_to_post)

#Todo PART 3 - Coming soon...
# Should return class<datetime> filtered by selected date