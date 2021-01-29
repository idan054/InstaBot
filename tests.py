user_input = input("Paste page usernames, separate with comma only (,)")
user_input = user_input.replace(" ", "") # Delete space
page_user_list = user_input.split(",")

# List of strings
# page_user_list = ["nike", "dainwalker", "_trash_baby"]

# List of ints
post_counters = []
for item in page_user_list:
	post_counters.append(
		{
			"static": 0,
			"updated": 0
		},
	)
# print(post_counters)

# Create a zip object from two lists
full_page = zip(page_user_list, post_counters)
dict_page_counters = dict(full_page)

value_1 = 1
value_2 = 2

# my_dict = {
# 	"my_key": {
# 		"key_1": value_1,
# 		"key_2": value_2
# 	}
# }
# print (my_dict["my_key"]["key_1"])  # This will print value_1
# print (my_dict["my_key"]["key_2"])  # This will print value_2

profile_user_list = {
    # Key = profile name #Value = post count
	"spider.models": {
		"static": 0,
		"updated": 0
	},
	"nike": {
		"static": 0,
		"updated": 0
	},
	"stabilo": {
		"static": 0,
		"updated": 0
	}
}
# print (profile_user_list["nike"]["updated"])
# print (profile_user_list["stabilo"]["updated"])