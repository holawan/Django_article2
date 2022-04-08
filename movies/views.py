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
    if request.method == 'POST' :
        #POST형태로 해당 영화의 Primary key가 전달되면  
        movie = Movie.objects.get(pk=pk)
        #게시글을 삭제한다. 
        movie.delete()
    return redirect('movies:index')