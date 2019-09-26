from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from movies_app.models import Movies
from series_episodes_app.models import Series_Episodes
from documentaries_episodes_app.models import Documentaries_Episodes

def war(request):
    all_movies = Movies.objects.all()
    all_series_ep = Series_Episodes.objects.all()
    all_documentaries_ep = Documentaries_Episodes.objects.all()

    template = loader.get_template('overview/war.html')
    context = {
        'all_movies':all_movies,
        'all_series_ep':all_series_ep,
        'all_documentaries_ep':all_documentaries_ep,
    }

    return HttpResponse(template.render(context, request))