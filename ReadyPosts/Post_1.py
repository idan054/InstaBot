# This is post "1"

upload_date = "2021-02-04"
upload_time = "11:51:33"
page_profile = "spider_modelsx"
post_desc = "caption_for_photo"
 
# Today's post credit: @spider_modelsx"
# Option A
pic_link = "https://instagram.fhfa1-1.fna.fbcdn.net/v/t51.2885-15/e35/143860877_325508472132218_4317617745678578269_n.jpg?_nc_ht=instagram.fhfa1-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=qQBqpzDS2h4AX_d87jS&tp=1&oh=d94bb588df0b6e3e85ad6156f5ec730c&oe=60455341"
# Option B
# Post1.jpg in this directory...

readyPost_dict = {
  "Post_1": {
    "page_profile": "spider_modelsx",
    "post_desc": "caption_for_photo",
    "pic_link": "https://instagram.fhfa1-1.fna.fbcdn.net/v/t51.2885-15/e35/143860877_325508472132218_4317617745678578269_n.jpg?_nc_ht=instagram.fhfa1-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=qQBqpzDS2h4AX_d87jS&tp=1&oh=d94bb588df0b6e3e85ad6156f5ec730c&oe=60455341"
  }
}

readyPost_dict.update(
  {post_counter: {
    "page_profile": page_profile,
    "post_desc": post_desc,
    "pic_link": pic_link
  }}
)
