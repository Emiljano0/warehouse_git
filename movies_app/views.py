from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from .models import Movies


def movies(request):
    all_movies = Movies.objects.all()

    paginator = Paginator(all_movies, 8)  # Show 5 movies per page

    page = request.GET.get('page')

    try:
        pag_movies = paginator.page(page)
    except PageNotAnInteger:
        pag_movies = paginator.page(1)
    except EmptyPage:
        pag_movies = paginator.page(paginator.num_pages)

    context = {
        'all_movies': all_movies,
        'pag_movies': pag_movies,
    }

    return render(request, 'overview/movies.html', context)


def detail_movies(request, movie_id):
    try:
        movie = Movies.objects.get(pk=movie_id)
    except Movies.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'overview/detail_movies.html', {'movie':movie})