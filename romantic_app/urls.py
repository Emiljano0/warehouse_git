from django.urls import path
from . import views

urlpatterns = [

    # /moviewarehouse/romantic/
    path('', views.romantic, name='romantic'),

]