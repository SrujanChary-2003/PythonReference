from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    # output= ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', { 
        'movies': movies
    })

def detail(request, movie_id):
    # try:
    #     movie= Movie.objects.get(pk=movie_id)
    #     # return HttpResponse(movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html',{'movie':movie})