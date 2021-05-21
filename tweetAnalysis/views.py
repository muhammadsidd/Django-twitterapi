from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
import tweepy
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Tweeter
from .forms import CreateUserForm
# Create your views here.

class UserCreate(CreateView):
    model = Tweeter
    form_class = CreateUserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user:user_timeline')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserCreate, self).form_valid(form)

@login_required(login_url='login')
class Userlist(ListView):
    model = Tweeter
    context_object_name = 'tweeters'
    template_name = 'user_list.html'
    login_url = 'login'

def twitter_timeline(request):


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            consumer_key = ''
            consumer_secret = ''
            access_token = ''
            access_token_secret = ''
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            user = Tweeter.objects.get()
            api = tweepy.API(auth)
            api.user_timeline(user)

            public_tweets = api.home_timeline()

            return render(request, 'public_tweets.html', {'public_tweets': public_tweets})
    else:
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'register.html', context)

