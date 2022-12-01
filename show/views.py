from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.views import generic

def hello_world(request):
    return HttpResponse('Hello World')


class TvShowView(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()

#id
class TvShowDetailView(generic.DetailView):
    template_name = 'movies.html'

    def get_object(self, **kwargs):
        tvshow_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tvshow_id)