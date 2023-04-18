import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
import boto3
import datetime

# List of Twitter accounts to query
# accounts = ["seether", "mindassault", "Junkyardlipstick", "TheBlackCatBones", "Deadlineband1","FacingTheGallows", "aandklas_pta", "KobusDeKockJr", "PolarDustMusic", "deitysma", "dirty_moonshine", "shotgun_torii", "climatecontrol", "ReverseTheSands", "StateDeceiver", "TheDriftSA", "TheFakeLeatherCoats", "DevilSpeak", "terminatryx", "adorned_za", "Octainiumband", "Ruff_Majik", "TheBarStoolPreachersZA", "ForsakingFate", "Bulletscript", "choking", "SurdusBand", "redhelenband", "The_Heresy_SA", "theoutlaworchestra", "AmberLightChoices", "tokyolucyband", "climatecontro1", "Climate_Control", "desolation_band", "sonofhawkband", "KingOfTheHillZA", "CautionBoyBand", "Geraas_Platform", "The_Touch_SA", "TerminXband", "CrimsonHouseSA", "OneDaySkyBand", "TurbineZA", "SubMissionSA", "Black_Pistol", "meltdowners", "thefabledring", "RiddlebreakBand", "reveryza", "nuff_saidza"]
accounts = ["IliaZolas", "StBloodbrother"]

# Query parameters
most_recent_date = datetime.datetime.now().strftime('%Y-%m-%d')
seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
query = " OR ".join(["(from:{} since:{} until:{})".format(account, seven_days_ago, most_recent_date) for account in accounts])

# Scrape tweets
tweets = []
for account in accounts:
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if tweet.user.username == account:
            # Get the user ID for the given Twitter account
            user_id = tweet.user.id

            # Get the TwitterUserScraper object for the given user ID
            user_scraper = sntwitter.TwitterUserScraper(user_id)

            # Get the user object for the given user ID
            user = next(user_scraper.get_items())

            # Get the profile image URL for the given user object
            profile_pic_url = user.profileImageUrl if user else None

            print(f"Profile image URL for {account}: {profile_pic_url}")

            # Get the profile image URL for the given user object
            # profile_pic_url = user.profileImageUrl if user else None

            # print(f"Profile image URL for {account}: {profile_pic_url}")

            # Check for attached media
            # media_url = None
            # if tweet.media:
            #     for media in tweet.media:
            #         if media.type == "photo":
            #             media_url = media.fullUrl

            # Append tweet information to list
            tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.url])

            break

# Convert to DataFrame
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Tweet Link'])


# # Save to JSON
# json_data = df.to_json(orient='records')

# # Upload to S3 bucket
# s3 = boto3.resource('s3')
# bucket_name = 'your-bucket-name'
# object_name = 'tweets.json'
# s3.Object(bucket_name, object_name).put(Body=json_data)

print(df)