from django.db import models

# Create your models here.


class SearchFields(models.Model):
    search_topic = models.CharField(max_length = 100, unique=True, null = False)

    def __str__(self):
        return self.search_topic

    class Meta:
        verbose_name = "SearchField"
        verbose_name_plural = "SearchFields"

class Tweets(models.Model):
    topic = models.ForeignKey(SearchFields, on_delete=models.CASCADE)
    tweet_link = models.URLField(max_length=200, unique=True, null = False)
    tweet_id = models.CharField(max_length = 100, unique=True, null = False)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic.search_topic + ' - ' +self.tweet_link
    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"