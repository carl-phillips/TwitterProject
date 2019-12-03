from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import TweetForm
from .tweets import get_tweets

def index(request):
    form = TweetForm()
    return render(request, 'polls/index.html', { 'form': form})

def gettweets(request):
    form = TweetForm(request.POST)
    if form.is_valid():
        search = form.cleaned_data['search_term']
        result_type = form.cleaned_data['result_type']
        date = form.cleaned_data['time_range']
        all_the_tweets = get_tweets(search, result_type, date)
        return render(request, 'polls/tweets.html', {'it': all_the_tweets})
    else:
        print("error")

