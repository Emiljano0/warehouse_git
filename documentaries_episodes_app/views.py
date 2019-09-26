from django.http import Http404
from django.shortcuts import render
from .models import Documentaries_Episodes


def documentaries_episodes(request, documentaries_ttl):
    try:
        all_documentaries_ep = Documentaries_Episodes.objects.filter\
            (documentary_episode_documentaries_title=documentaries_ttl)
    except Documentaries_Episodes.DoesNotExist:
        raise Http404("Episode does not exist")
    return render(request, 'overview/documentaries_episodes.html', {'all_documentaries_ep': all_documentaries_ep})


def documentaries_episode_detail(request, documentaries_nr):
    try:
        documentaries_ep = Documentaries_Episodes.objects.get(pk=documentaries_nr)
    except Documentaries_Episodes.DoesNotExist:
        raise Http404("Documentaries Episode does not exist")
    return render(request, 'overview/detail_documentaries.html', {'documentaries_ep': documentaries_ep})