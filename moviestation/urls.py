from django.urls import path

from . import views

app_name = 'moviestation'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('movie_details/<int:movie_id>', views.movie_detail, name='movie'),
    path('genre/<str:genre>', views.movie_genre, name='movie_genre'),
    path('addmovie', views.addmovie, name='addmovie'),
    path('search', views.search, name='search'),
]