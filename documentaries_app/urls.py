from django.urls import include, path
from . import views

app_name = 'documentaries_app'

urlpatterns = [

    # /moviewarehouse/documentaries/
    path('', views.documentaries, name='documentaries'),

    # /moviewarehouse/documentaries/Cosmos/
    path('<documentaries_ttl>/', include('documentaries_episodes_app.urls')),

]