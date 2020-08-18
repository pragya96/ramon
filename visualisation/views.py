from django.shortcuts import render
from django.views.generic.base import TemplateView
from djgeojson.views import GeoJSONLayerView
from forms import models


# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

    def get(self, request):
        articles = models.Article.objects.filter(status='R')
        locations = models.Location.objects.filter(status='R')
        buildings = models.Building.objects.filter(status='R')
        args = {'articles': articles, 'locations': locations, 'buildings': buildings}
        return render(request, self.template_name, args)


class MapLayer(GeoJSONLayerView):

    def get_queryset(self):
        context = models.Location.objects.filter(status='R')
        return context
