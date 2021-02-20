import schedule
import time

from Gadgets.console_design import bcolors

def schedule_job(someDay, someTime, someDef):

    if someDay == "sunday":
        schedule.every().sunday.at(someTime).do(someDef)
    elif someDay == "monday":
        schedule.every().monday.at(someTime).do(someDef)
    elif someDay == "tuesday":
        schedule.every().tuesday.at(someTime).do(someDef)
    elif someDay == "wednesday":
        schedule.every().wednesday.at(someTime).do(someDef)
    elif someDay == "thursday":
        schedule.every().thursday.at(someTime).do(someDef)
    elif someDay == "friday":
        schedule.every().friday.at(someTime).do(someDef)
    elif someDay == "saturday":
        schedule.every().saturday.at(someTime).do(someDef)

    # def still_listening():
    #     print(f"{bcolors.BOLD}Still listening for scheduled jobs...{bcolors.Normal}")
    # schedule.every(3).seconds.do(still_listening)


## Example
# def job():
#     print("Im doing my job...")

# jobs_schedule(someDay="saturday",
#             someTime="23:31",
#             someDef=job)

