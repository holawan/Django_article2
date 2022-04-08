from django.shortcuts import render,redirect

from movies.forms import MovieForm
from .models import Movie
# Create your views here.
def index(request) :
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)


#Create html 만들기 

def create(request) :
    if request.method == 'POST' :
        form = MovieForm(request.POST)

        if form.is_valid() :
            movie = form.save()
            return redirect('movies:index',movie.pk)
    else :
        form = MovieForm()
    context = {
        'form':form,
    }

    return render(request, 'movies/create.html',context)

    