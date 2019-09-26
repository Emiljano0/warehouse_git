from django.urls import include, path
from . import views

app_name = 'series_episodes_app'

urlpatterns = [

    # /moviewarehouse/series/TrueDetective/
    path('', views.series_episodes, name='series_episodes'),

    # /moviewarehouse/series_episodes/11/
    path('<episode_nr>/', views.detail_series_episodes, name='detail_series_episodes'),

]