import time
import schedule
from Gadgets.console_design import bcolors


def still_listening():
    print(f"{bcolors.BOLD}Always listening for scheduled jobs...{bcolors.Normal}")
schedule.every(3).seconds.do(still_listening)


## Example
# def job():
#     print("Im doing my job...")

# jobs_schedule(someDay="saturday",
#             someTime="23:31",
#             someDef=job)


while True:
    # run_pending
    schedule.run_pending()
    time.sleep(1)
