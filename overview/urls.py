from django.urls import include, path
from . import views

urlpatterns = [

    # /moviewarehouse/
    path('', views.index, name='index'),

    # /moviewarehouse/movies/
    path('movies/', include('movies_app.urls')),

    # /moviewarehouse/series/
    path('series/', include('series_app.urls')),

    # /moviewarehouse/series_episodes/
    path('series_episodes/', include('series_episodes_app.urls')),

    # /moviewarehouse/documentaries/
    path('documentaries/', include('documentaries_app.urls')),

    # /moviewarehouse/documentaries_episodes/
    path('documentaries_episodes/', include('documentaries_episodes_app.urls')),

    # /moviewarehouse/detective/
    path('detective/', include('detective_app.urls')),

    # /moviewarehouse/other_worlds/
    path('other_worlds/', include('other_worlds_app.urls')),

    # /moviewarehouse/romantic/
    path('romantic/', include('romantic_app.urls')),

    # /moviewarehouse/war/
    path('war/', include('war_app.urls')),

    # /moviewarehouse/search/
    path('search/', include('search_app.urls')),

]