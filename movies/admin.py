from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin) :
    # admin 페이지에서는 영화 기본 정보 보여주기 
    list_display = ('title','genre','audience','score')

admin.site.register(Movie,MovieAdmin)