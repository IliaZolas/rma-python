import snscrape.modules.twitter as sntwitter
import requests
from bs4 import BeautifulSoup

# Define the Twitter username for which to get the profile image URL
username = "IliaZolas"

# Get the user ID for the given Twitter account
user_id = next(sntwitter.TwitterSearchScraper(f"from:{username}").get_items()).user.id
print('User id is ', user_id)

# Build the profile URL
profile_url = f"https://twitter.com/{username}"

# Send a GET request to the profile URL and extract the HTML content
response = requests.get(profile_url)
html_content = response.text

# Parse the HTML content using BeautifulSoup and extract the profile picture URL
soup = BeautifulSoup(html_content, 'html.parser')
profile_pic_url = soup.find('img', {'class': 'css-9pa8cd'})

print('Profile picture URL is', profile_pic_url)






# import snscrape.modules.twitter as sntwitter

# # Define the Twitter username for which to get the profile image URL
# username = "IliaZolas"

# # Get the user ID for the given Twitter account
# user_id = next(sntwitter.TwitterSearchScraper(f"from:{username}").get_items()).user.id
# print('User id is ', user_id)

# # Get the TwitterUserScraper object for the given user ID
# user_scraper = sntwitter.TwitterUserScraper(user_id)
# print('User scraper for', username,':',user_scraper)

# # Get the user object for the given user ID
# user = next(user_scraper.get_items())
# print('User object is', user)

# # Get the profile image URL for the given user object
# profile_pic_urls = user.profileImageUrl if user else None
# print(f"Profile image URLs for {username}: {profile_pic_urls}")

# # # Get the profile image URL for the given user object
# # profile_pic_url = user.profileImageUrl if user else None

# # print("Profile image URL for {username}: {profile_pic_url}")