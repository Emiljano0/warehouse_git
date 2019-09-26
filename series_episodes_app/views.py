from django.http import Http404
from django.shortcuts import render
from .models import Series_Episodes


def series_episodes(request, series_ttl):
    try:
        all_series_ep = Series_Episodes.objects.filter(series_episode_series_title=series_ttl)
    except Series_Episodes.DoesNotExist:
        raise Http404("Episode does not exist")
    return render(request, 'overview/series_episodes.html', {'all_series_ep': all_series_ep})


def detail_series_episodes(request, episode_nr):
    try:
        series_ep = Series_Episodes.objects.get(pk=episode_nr)
    except Series_Episodes.DoesNotExist:
        raise Http404("Series Episode does not exist")
    return render(request, 'overview/detail_series.html', {'series_ep': series_ep})
