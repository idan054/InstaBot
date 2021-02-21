import json
from Gadgets.console_design import bcolors

# Todo לבדוק ולעדכן בהתאם, מה קורה אם יש (') בתיאור המקורי של הפוסט
def json_printer(the_dict):
    print(f"{bcolors.Blue}{bcolors.BOLD}"
          f"Json view:"
          f"{bcolors.Normal}")
    # JSON VIEW -  Replace (') to (") for good Json file
    the_dist_as_json = str(the_dict).replace("\'", "\"")

    try:
        the_dist_as_json = json.loads(the_dist_as_json)
    except ValueError as e:
        e = str(e)
        if "Expecting" in e:
            print(f"{bcolors.Red}Error. Make sure (') not character in the_dict{bcolors.Normal}")
            return

    the_dist_as_json = json.dumps(the_dist_as_json, indent=2)
    print(the_dist_as_json)
