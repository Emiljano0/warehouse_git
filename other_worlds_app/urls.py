from django.urls import path
from . import views

urlpatterns = [

    # /moviewarehouse/other_worlds/
    path('', views.other_worlds, name='other_worlds'),

]