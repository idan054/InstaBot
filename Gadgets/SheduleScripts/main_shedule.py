import time
import schedule
from Gadgets.console_design import bcolors
from Gadgets.SheduleScripts.S1_Time2Post import setup_time2post, setup_hours2post, setup_days2post
from Gadgets.SheduleScripts.S2_JobsSchedule import schedule_job



# print(str(time2post_dict["Days"].keys()).lower())

def job():
    print("Im doing my job...")

# def schedule_posts(days2Post_list, hours2Post_list, someDef ):
def schedule_posts():
    for day in days2Post_list:
        current_day = str(day).lower()
        # print(current_day)

        for hour in hours2Post_list:
            current_hour = f"{hour}:00"
            # print(current_hour)

            schedule_job(someDay=current_day,
                         someTime=current_hour,
                         someDef=job)
            print(f"post scheduled for every{bcolors.BOLD}{current_day}, {current_hour} {bcolors.Normal}")
schedule_posts()

while True:
    ## looking for pending
    schedule.run_pending()
    time.sleep(1)