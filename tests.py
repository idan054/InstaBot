from Gadgets.jsonPrinter import json_printer

ready2Post_dict = {'1': {'page_profile': 'spider_modelsx', 'original_post_desc': "caption_for_photo\n  post credit: @spider_modelsx\n", 'pic_link': 'https://instagram.fhfa1-1.fna.fbcdn.net/v/t51.2885-15/e35/150869913_1104238106665113_7779651190563703574_n.jpg?_nc_ht=instagram.fhfa1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=M3mDKMVaRs4AX-He2tq&tp=1&oh=d3384e81734d3781f7efcb2b15c7e513&oe=605D198E'}}

print("Upload 1st post in ready2Post_dict")
# upload_post(insta_user="spider_modelsx",
#             insta_pass="Idan05423",
#             page_profile=posts_dict["1"]["page_profile"],
#             original_post_desc=posts_dict["1"]["original_post_desc"],
#             pic_link=posts_dict["1"]["pic_link"],
#             )
uploaded_post_dict = {}
uploaded_post_dict.update({
    f"1": {
        "page_profile": ready2Post_dict["1"]["page_profile"],
        "original_post_desc": ready2Post_dict["1"]["original_post_desc"],
        "pic_link": ready2Post_dict["1"]["pic_link"],
    }
  }
)
print("\n uploaded_post_dict:")
json_printer(uploaded_post_dict)
del ready2Post_dict["1"]
print("current post removed from ready2Post_dict")
