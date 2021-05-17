from django.shortcuts import render
import tweepy
from .models import Tweeter
# Create your views here.

def user_timeline(request):
    consumer_key = ''
    consumer_secret =''
    access_token=''
    access_token_secret=''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    user = Tweeter.objects.get('')
    api = tweepy.API(auth)
    api.user_timeline(user)

    public_tweets = api.home_timeline()

    return render(request, 'public_tweets.html', {'public_tweets': public_tweets})