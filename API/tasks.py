import os
from celery import shared_task
from .models import *
from scrape import scrape_tweets
import snscrape.modules.twitter as twitterScraper
from langdetect import detect


@shared_task(bind=True)

def process_tweets_task(self):
    # available_fields= SearchFields.objects.all()
    topic = 'ReactJS'
    # tweets = scrape_tweets(topic)
    # for tweet in tweets:
    #     try:
    #         Tweets.objects.create(topic=topic, tweet_link=tweet['url'], tweet_id=tweet['id'])
    #         return "Success"
    #     except Exception as e:
    #         print(e)
    #         print(tweet.get('id'))
    #         return "Failed"
    
    scraper = twitterScraper.TwitterSearchScraper(topic)
    topic = SearchFields.objects.get(search_topic=topic)
    tweets = []
    max_count = 0
    for i, tweet in enumerate(scraper.get_items()):
        # print(max_count)
        # print(i, tweet)
        # if str(tweet.user) not in block_list:
        if i == 20:
            break
        bodies = tweet.content

        # checking the language
        language = detect(bodies)

        if (language == "en"):
            try:
                Tweets.objects.create(topic=topic, tweet_link=tweet.url, tweet_id=str(tweet.id))
                print("Success")
                max_count+=1
            except Exception as e:
                print(e)
                print("failed",tweet.id)

            
    return max_count