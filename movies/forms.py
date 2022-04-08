from django import forms
from .models import Movie

class MovieForm(forms.ModelFrom) :

    class Meta :
        model = Movie 

        fields = '__all__'