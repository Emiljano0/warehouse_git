from django.http import HttpResponse
from django.template import loader
from movies_app.models import Movies
from series_app.models import Series
from documentaries_app.models import Documentaries


def index(request):
    all_movies = Movies.objects.all()
    all_series = Series.objects.all()
    all_documentaries = Documentaries.objects.all()

    template = loader.get_template('overview/index.html')
    context = {
        'all_movies':all_movies,
        'all_series':all_series,
        'all_documentaries':all_documentaries,
    }

    return HttpResponse(template.render(context, request))
