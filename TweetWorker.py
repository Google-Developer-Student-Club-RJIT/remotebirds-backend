from scrape import scrape_tweets
from API.models import SearchFields, Tweets

def process_tweets():

    available_fields= SearchFields.objects.all()
    for field in available_fields:
        print(field.search_topic)
        tweets = scrape_tweets(field.search_topic)
        for tweet in tweets:
            print(tweet)
            try:
                Tweets.objects.create(topic=field, tweet_link=tweet['url'], tweet_id=tweet['id'])
            except Exception as e:
                print(e)
                

    return True


