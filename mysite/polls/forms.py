from django import forms
from bootstrap_datepicker_plus import DatePickerInput
import datetime

class TweetForm(forms.Form):
    search_term = forms.CharField(label='Search:', max_length=100)
    CHOICES = (('recent', 'Recent'),('popular', 'Popular'))
    result_type = forms.ChoiceField(choices=CHOICES)
    date = forms.DateField(initial=datetime.date.today, widget=DatePickerInput(format='%Y-%m-%d'))
