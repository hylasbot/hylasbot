# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time, os

#enter the corresponding information from your Twitter application management:
CONSUMER_KEY = 'OepvOuxpSb2Uh2b9fdMdHLJCA' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'g63m7m95SJbL1Y6fOSExp6qFhzb1gotR7yIdcmavvRXW1DcZL8' #keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '1119844861383979009-0kpPYMEPrrdjnLlbkTCvx3hV15reBc' #keep the quotes, replace this with your access token
ACCESS_SECRET = 'yNYmM16ngTWHT3iiIz6TwjsRT4WsP87Gv2PgBMBN0TLHS' #keep the quotes, replace this with your access token secret


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# access Twitter!
api = tweepy.API(auth)

# open our content file and read each line
os.chdir('content')

# for each line in our contents file, lets tweet that line out except when we hit a error
for content_image in os.listdir('.'):
        api.update_with_media(content_image)
        time.sleep(90)
