from django import forms

class TweetForm(forms.Form):
    search_term = forms.CharField(label='Search:', max_length=100)
    CHOICES = (('recent', 'Recent'),('popular', 'Popular'))
    result_type = forms.ChoiceField(choices=CHOICES)
    time_range = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
