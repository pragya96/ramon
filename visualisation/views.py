from django.shortcuts import render
from django.views.generic.base import TemplateView
from forms import models


# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

    def get(self, request):
        articles = models.Article.objects.filter(status='R')
        args = {'articles': articles}
        return render(request, self.template_name, args)
