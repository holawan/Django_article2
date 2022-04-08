from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from movies.forms import MovieForm
from .models import Movie
# Create your views here.
import requests
import random

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

def movie_recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
        'region' : 'KR',
        'language' : 'ko',
        'query' : title
    }
    response = requests.get(BASE_URL + path, params = params).json()
    print(response)
    if response['results'] == [] :
        return None
    # 여기에 코드를 작성합니다. 
    movie_id = response['results'][0]['id'] 
    
    BASE_URL_2 = 'https://api.themoviedb.org/3'
    path_2 = f'/movie/{movie_id}/recommendations'
    params_2 = {
        'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
        'language' : 'ko'
    }
    response2 = requests.get(BASE_URL_2 + path_2, params = params_2).json()
    # 여기에 코드를 작성합니다.  

    recommend = response2['results']
    recommend_list = []
    for movie in recommend :
        info = [movie['title'],movie['vote_average'],movie['release_date'],movie['overview'],movie['poster_path'],movie['id']]
        recommend_list.append(info)

    return recommend_list

def recommendations(request) :
    rec = random.choice(movie_recommendation('쇼생크 탈출'))
    print(rec)
    context = {
        'title' : rec[0],
        'vote_average' : round(rec[1],1),
        'release_date' : rec[2],
        'overview' : rec[3],
        'poster' : rec[4],
        'id' : rec[5]
    }
    return render(request,'movies/recommendation.html',context)

# @require_safe
# def detail(request,pk) :
#     movie = get_object_or_404(Movie,pk=pk)

#     context = {
#         'movie' :movie
#     }
#     return render(request,'movies/detail.html',context)