import tweepy
import time

auth = tweepy.OAuthHandler('JD0VargXAlAGDa8QpVPruC38g', 'jAAnXVNUJFkkgZXx3TyyRLiHvUZeuVYu4VDfpJ6C4mg0vFCKVf')
auth.set_access_token('1065624990-spWIcf4pSnJTM2uR6QjbLsDJEHw0Zf9uCD5ws90', 'UT2GhL9dhcq4PeZvWWqOqL8YRRahXLqr2M8yxxu8TjxWE')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break




#follow back
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
# 	if follower.name == 'RΛMIN NΛSIBOV':
# 		print(follower.name)
# 		follower.follow()
# 		break