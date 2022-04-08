from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from movies.forms import MovieForm
from .models import Movie
# Create your views here.


@require_safe
def index(request) :
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies
    }
    return render(request,'movies/index.html',context)


#Create html 만들기 
@require_http_methods(['GET','POST'])
def create(request) :
    if request.method == 'POST' :
        form = MovieForm(request.POST)

        if form.is_valid() :
            movie = form.save()
            return redirect('movies:detail',movie.pk )
    else :
        form = MovieForm()
    context = {
        'form':form,
    }

    return render(request, 'movies/create.html',context)

@require_safe
def detail(request,pk) :
    movie = get_object_or_404(Movie,pk=pk)

    context = {
        'movie' :movie
    }
    return render(request,'movies/detail.html',context)

    
@require_http_methods(['GET','POST'])
def update(request,pk) :
    movie = get_object_or_404(Movie,pk=pk)
    if request.method == 'POST' :
        form = MovieForm(request.POST,instance=movie)

        if form.is_valid() :
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else :
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form':form
    }

    return render(request, 'movies/update.html',context)

@require_POST
def delete(request,pk):
    if request.method == 'POST' :
        #POST형태로 해당 영화의 Primary key가 전달되면  
        movie = get_object_or_404(Movie,pk=pk)
        #게시글을 삭제한다. 
        movie.delete()
    return redirect('movies:index')