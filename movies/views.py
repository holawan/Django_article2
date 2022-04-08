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
            form = form.save()
            return redirect('movies:index')
    else :
        form = MovieForm()
    context = {
        'form':form,
    }

    return render(request, 'movies/create.html',context)

#Detail 만들기
def detail(request,pk) :
    movie = Movie.objects.get(pk=pk) 

    context = {
        'movie' :movie
    }
    return render(request,'movies/detail.html',context)
