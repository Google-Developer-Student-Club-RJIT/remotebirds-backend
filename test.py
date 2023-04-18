import snscrape.modules.twitter as twitterScraper
import time



def scrape(query):
    # query = f'{kwargs["query"]} since:2022-09-01 until:2022-09-31'
    # query = f'{kwargs["query"]} since:{kwargs["start_date"]} until:{kwargs["end_date"]}'
    scraper = twitterScraper.TwitterSearchScraper(query)
    tweets = []
    max_count = 10
    for i, tweet in enumerate(scraper.get_items()):
        # print(max_count)
        if i == (max_count):
            break
        # print(i, tweet)
        # if str(tweet.user) not in block_list:
        bodies = tweet.content
        # bodies = ''.join(' ' + val.replace('\xa0', '').replace('\r\n', '').strip() for val in bodies)
        tweets.append({
            "id": str(tweet.id),
            "url": tweet.url,
            "content": bodies,
            "date": str(tweet.date)
        })
        # else:
        #     max_count += 1
    return tweets


if __name__ == "__main__":
    while True:
        time.sleep(10)
    # scrape("develoepr job remote")
        print(scrape('django'))