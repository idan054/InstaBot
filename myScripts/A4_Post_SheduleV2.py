import datetime

from itertools import cycle

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
def setup_hours2post():
    hours_string = input("Insert hours (by Order) to upload posts on Upload Day. \nSo 14 = 14:00"
                         "\nseparate with comma only (,)") or "13, 16, 19"
    hours_string = hours_string.replace(" ", "")  # Delete space
    _hours2Post_list = hours_string.split(",")
    _hours2Post_list = list(map(int, _hours2Post_list))  # ['1','2','3'] → [1,2,3]
    return _hours2Post_list

hours2Post_list =  setup_hours2post()
print("hours2Post_list:")
print(*hours2Post_list, sep=" | ")

def setup_time2post():
    hours2Post_dict = {}
    forIndex = 1
    for hour in hours2Post_list: # Until end of list...
        hours2Post_dict[f"post_{forIndex}"] =  f"{hour}:00"
        forIndex += 1
        # hours2Post_dict.update({
        #     "hour2Post": f"{hour}:00"
        # }
    # )
    # print(hours2Post_dict)

    time2post_dict = {}
    forIndex = 1
    for day in days2Post_list:
        time2post_dict[day] = hours2Post_dict
        forIndex += 1

    # print(time2post_dict)
    # Replace ' to " for good Json file
    # print(str(time2post_dict).replace("\'", "\""))

    return time2post_dict