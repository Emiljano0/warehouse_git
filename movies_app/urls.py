from django.urls import path
from . import views

app_name= 'movies_app'

urlpatterns = [

    # /moviewarehouse/movies/
    path('', views.movies, name='movies'),

    # /moviewarehouse/movies/77/
    path('<movie_id>/', views.detail_movies, name='detail_movies'),

]
