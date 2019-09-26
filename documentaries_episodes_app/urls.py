from django.urls import path
from . import views

app_name = 'documentaries_episodes_app'

urlpatterns = [

    # /moviewarehouse/documentaries/Cosmos/
    path('', views.documentaries_episodes, name='documentaries_episodes'),

    # /moviewarehouse/documentaries_episodes/55/
    path('<documentaries_nr>/', views.documentaries_episode_detail, name='documentaries_episode_detail'),

]
