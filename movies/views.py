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
            return redirect('movies:detail')
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

def update(request,pk) :
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST' :
        form = MovieForm(request.POST,instance=movie)

        if form.is_valid() :
            form = form.save()
            return redirect('movies:detail',movie.pk)
    else :
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form':form,
    }

    return render(request, 'movies/update.html',context)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method=='POST' :
        movie.delete()
        movie.save
        return render(request,'movies:index')
    return render(request,'movies:detail',movie.pk)