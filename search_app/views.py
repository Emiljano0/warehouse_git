from django.shortcuts import render
from django.db.models import Q
from movies_app.models import Movies
from series_episodes_app.models import Series_Episodes
from documentaries_episodes_app.models import Documentaries_Episodes

def search_v(request):
    all_movies = Movies.objects.all()
    all_series_ep = Series_Episodes.objects.all()
    all_documentaries_ep = Documentaries_Episodes.objects.all()


    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query:
            # lookups_movies = Q(movie_title__icontains=query)
            lookups_series = Q(series_episode_title__icontains=query)
            lookups_documentaries = Q(documentary_episode_title__icontains=query)
            results_movies = Movies.objects.filter(movie_title__icontains=query)
            results_series = Series_Episodes.objects.filter(lookups_series).distinct()
            results_documentaries = Documentaries_Episodes.objects.filter(lookups_documentaries).distinct()
            context = {
                'all_movies': all_movies,
                'all_series_ep': all_series_ep,
                'all_documentaries_ep': all_documentaries_ep,
                'results_movies': results_movies,
                'results_series': results_series,
                'results_documentaries': results_documentaries,
                'submitbutton': submitbutton,
            }
            return render(request, 'overview/search.html',context)
        else:
            return render(request, 'overview/search.html')
    else:
        return render(request, 'overview/search.html')