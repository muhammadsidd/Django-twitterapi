from django.contrib import messages
from django.shortcuts import render, redirect
import tweepy
from .models import Tweeter
from .forms import CreateUserForm
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

def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            #return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)