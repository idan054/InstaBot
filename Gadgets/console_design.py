import sys
from time import sleep


# from termcolor import colored #Another option
class bcolors:
    White = '\033[97m'
    Purple = '\033[95m'
    Blue = '\033[94m'
    Yellow = '\033[93m'
    Green = '\033[92m'
    Red = '\033[91m'
    Grey = '\033[90m'

    Normal = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# print(f'{bcolors.Green}User "{bcolors.BOLD}Arik{bcolors.Normal}{bcolors.Green}" Added!{bcolors.Normal}')

def update_progress(time_unit, total, length=20, fg=f""
            f"{bcolors.Blue}{bcolors.BOLD}•", bg=f"{bcolors.White}•", decimals=0):
    progress = 100 * (time_unit / float(total))
    blocks = int(length * time_unit // total)
    bar = fg * blocks + bg * (length - blocks)
    sys.stderr.write(f"{bcolors.White}\r[{bar}] {progress:.{decimals}f}%") #{count}/60
    sys.stderr.flush()

# Example
# loading bar of 1 minute

# for sec in range(0, 60):
#     sleep(1)
#     update_progress(sec, 60)