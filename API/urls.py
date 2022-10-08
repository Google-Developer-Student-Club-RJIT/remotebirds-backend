from django.urls import path
from .views import GetTweets

urlpatterns = [
    path('', GetTweets.as_view()),
]
