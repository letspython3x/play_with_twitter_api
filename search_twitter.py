import requests
from requests_oauthlib import OAuth1

# Let's define consumer and access keys and secrets for getting access to Twitter API through your application
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


def search_tweets(str_to_match, count_of_tweets=10):
    search_url = 'https://api.twitter.com/1.1/search/tweets.json'
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
    params = {
        "count": count_of_tweets,
        "lang": 'en',
        "q": str_to_match
    }
    res = requests.get(search_url, auth=auth, params=params)

    if res.status_code == 200:
        tweets = res.json()
        print("#" * 10 + "Tweets That match query (%s) are present below:" % str_to_match)

        for num, tweet in enumerate(tweets['statuses']):
            print()
            print('Tweet )#{0}\t{1}\n{2}\n'.format(num + 1, tweet['created_at'], tweet['text']))
    else:
        print("Something went wrong, Status Code ", res.status_code)


if __name__ == "__main__":
    pattern = "@ScienceNews"
    search_tweets(str_to_match=pattern)

    pattern = "#Munk101"
    search_tweets(str_to_match=pattern)
