import snscrape.modules.twitter as twitterScraper
from langdetect import detect

job_board_list = [
    "RemoteTechJobs0",
    "zobjobsUS",
    "RemoteSonar",
    "RecruitngEdge",
    "CodingJobsIt",
    "jobscanCo",
    "JobHuntOrg",
    "justremoteco",
    "nodeskco",
    "weworkremotely",
    "jobmote",
    "WantRemoteJob",
    "daily_remote",
    "remoteworkhub",
    "workingnomads",
    "DevStartupJobs",
    "zobjobsGB",
    "growremotelyio",
    "jobsincrypto",
    "Rezoomex",
    "_remotify",
    "Up2staff",
    "zobjobsCA",
]

block_list = ["https://twitter.com/" + e for e in job_board_list]


def scrape(**kwargs):
    # query = f'{kwargs["query"]} since:2022-09-01 until:2022-09-31'
    query = f'{kwargs["query"]} since:{kwargs["start_date"]} until:{kwargs["end_date"]}'
    scraper = twitterScraper.TwitterSearchScraper(query)
    tweets = []
    max_count = 100
    for i, tweet in enumerate(scraper.get_items()):
        # print(max_count)
        if i == (max_count):
            break
        # print(i, tweet)
        # if str(tweet.user) not in block_list:
        bodies = tweet.content

        # checking the language
        language = detect(bodies)

        if (language == "en"):
            # bodies = ''.join(' ' + val.replace('\xa0', '').replace('\r\n', '').strip() for val in bodies)
            tweets.append({
                "id": str(tweet.id),
                "url": tweet.url,
                "content": bodies,
                "date": str(tweet.date)
            })
            
        else:
            max_count += 1

    return tweets


if __name__ == "__main__":
    # scrape("develoepr job remote")
    print(scrape('django'))
