from django.urls import path
from . import views

urlpatterns = [

    # /moviewarehouse/search/
    path('', views.search_v, name='search'),

]