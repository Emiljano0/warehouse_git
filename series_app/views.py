from django.http import Http404
from django.shortcuts import render
from .models import Series
from series_episodes_app.models import Series_Episodes


def series(request):
    all_series = Series.objects.all()
    return render(request, 'overview/series.html', {'all_series': all_series})


def episodes(request, episode_nr):
    try:
        series_ep = Series_Episodes.objects.get(pk=episode_nr)
    except Series_Episodes.DoesNotExist:
        raise Http404("Series Episode does not exist")
    return render(request, 'overview/detail_series.html', {'series_ep': series_ep})