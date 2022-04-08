from django import forms
from .models import Movie




class MovieForm(forms.ModelForm) :
    GENRE_A = 'comedy'
    GENRE_B = 'horror'
    GENRE_C = 'romance'

    GENRE_CHOICES = [
        (GENRE_A,'코미디'),
        (GENRE_B,'공포'),
        (GENRE_C,'로맨스')
    ] 

    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.Select()
    )
    class Meta :
        model = Movie 

        fields = '__all__'