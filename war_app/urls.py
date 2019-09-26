from django.urls import path
from . import views

urlpatterns = [

    # /moviewarehouse/war/
    path('', views.war, name='war'),

]