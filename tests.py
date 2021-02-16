sample = {
    "name": "interpolator",
    "children": [
      {"name": "ObjectInterpolator", "size": 1629},
      {"name": "PointInterpolator", "size": 1675},
      {"name": "RectangleInterpolator", "size": 2042}
     ]
}

import json
with open('posts_result.json', 'w') as json_file:
    json.dump(sample, json_file)