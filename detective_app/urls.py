from django.urls import path
from . import views

urlpatterns = [

    # /moviewarehouse/detective/
    path('', views.detective, name='detective'),

]