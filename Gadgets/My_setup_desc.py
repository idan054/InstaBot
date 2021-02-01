from Gadgets.console_colors import bcolors

# A4 - <- הכנת תיאור: האשטגים קיימים יחולצו -> תיאור מקור נקי
# -> מילות מפתח מבוססת למידה מכונה -> שורת תיוג קבועה בתיאור - A4

txt_file = open(f'../ThePost/2021-01-30_22-05-44_UTC.txt').read()
print(f"{txt_file} \nToday's post credit: @author")

hashtag_list = []
taggedUsers_list = []
#S Not in use Def, Extract hashtags and users tags
def tags_xtract():
    word_list = txt_file.split()
    # print(word_list)
    for word in word_list:
        if word[0] == "#":
            hashtag_list.append(word)
        elif word[0] == "@":
            taggedUsers_list.append(word)
    print(f"{bcolors.BOLD}Hashtags: {bcolors.Normal}")
    print(*hashtag_list)
    print(f"{bcolors.BOLD}Tagged Users: {bcolors.Normal}")
    print(*taggedUsers_list)
    print() # As \n

#S Not in use Def, Remove hashtags from desc (based tags_xtract())
def clean_desc():
   new_txt_file = txt_file
   for tag in hashtag_list:
       # print("A")
       new_txt_file =  new_txt_file.replace(tag, "")
   print(new_txt_file)

# for word in txt_file:
    # print(word)