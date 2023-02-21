import tweepy

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(
    "YOUR_CONSUMER_KEY",
    "YOUR_CONSUMER_SECRET",
    "YOUR_ACCESS_TOKEN",
    "YOUR_ACCESS_TOKEN_SECRET"
)

api = tweepy.API(auth)

# Open the text file containing the tweets
with open('tweets.txt', 'r') as file:
    tweets = file.readlines()

# Send the tweets
for tweet in tweets:
    api.update_status(tweet)

print("Tweets have been sent successfully.")
