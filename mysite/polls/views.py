from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
import datetime
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
        date = form.cleaned_data['date']
        if isinstance(date, datetime.date):
            all_the_tweets = get_tweets(search, result_type, date)
            return render(request, 'polls/tweets.html', {'all_tweets': all_the_tweets})
        else:
            return render(request, 'polls/index.html', {'error': 'Please enter a valid date'})