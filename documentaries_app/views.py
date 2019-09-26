from django.http import Http404
from django.shortcuts import render
from .models import Documentaries
from documentaries_episodes_app.models import Documentaries_Episodes


def documentaries(request):
    all_documentaries = Documentaries.objects.all()
    return render(request, 'overview/documentaries.html', {'all_documentaries': all_documentaries})


def documentaries_episodes(request, episode_nr):
    try:
        series_ep = Documentaries_Episodes.objects.get(pk=episode_nr)
    except Documentaries_Episodes.DoesNotExist:
        raise Http404("Series Episode does not exist")
    return render(request, 'overview/detail_series.html', {'series_ep': series_ep})