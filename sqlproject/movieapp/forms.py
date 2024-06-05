from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'year', 'length']

class ReportForm(forms.Form):
    user_id = forms.CharField(label = 'User ID', max_length=100)
    #movie_name = forms.CharField(label = 'Movie Name', max_length=100)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
    sort_by = forms.ChoiceField(label = 'Sort By', choices = 
    [('date_watched', 'Date Watched'), 
    ('rating', 'Rating'), 
    ('release_year_asc', 'Release Year (Ascending)'), 
    ('release_year_desc', 'Release Year (Descending)')])

class UpdateMovieLogForm(forms.Form):
    log_id = forms.IntegerField(label='Log ID')
    new_rating = forms.IntegerField(label='New Rating')
