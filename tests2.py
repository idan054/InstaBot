import json
from xopen import xopen

json_xz_file = xopen(f'ThePost/2021-02-18_09-15-36_UTC.json.xz').read()
json_xz_file = json.loads(json_xz_file)
x = dict(json_xz_file)
print(x["node"]["owner"]["username"])