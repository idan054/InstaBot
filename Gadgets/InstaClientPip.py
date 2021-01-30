# Full Details: https://github.com/chris-greening/instascrape & https://github.com/chris-greening/instascrape/wiki/Scraped-data-points
# from instascrape import *

# Instantiate the scraper objects

google_profile = Profile('https://www.instagram.com/stabilo/')
google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
google_hashtag = Hashtag('https://www.instagram.com/explore/tags/google/')

# Scrape their respective data
google_profile.scrape()
google_post.scrape()
google_hashtag.scrape()

print(google_profile.is_private)
print(google_profile.posts)
print(google_post['hashtags'])
print(google_hashtag.amount_of_posts)