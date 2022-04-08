from django.urls import path
from . import views
urlpatterns = [
    # 전체 영화 목록 페이지 조회
    path('',views.index,name='index'),
]