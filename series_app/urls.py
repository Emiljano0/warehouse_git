from django.urls import include, path
from . import views

app_name = 'series_app'

urlpatterns = [

    # /moviewarehouse/series/
    path('', views.series, name='series'),

    # /moviewarehouse/series/TrueDetective/
    path('<series_ttl>/', include('series_episodes_app.urls')),

]