from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.gis.geos import Point
from django.contrib import messages
from django.http import HttpResponseRedirect
from forms import models
from forms import forms


OLD_MADRID = {
    False: 0,
    True: 1,
    None: 2,
}


# Create your views here.
class Articles(TemplateView):
    template_name = "tables/home.html"

    def get(self, request):
        data = models.Article.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Occupations(TemplateView):
    template_name = "tables/occupations.html"

    def get(self, request):
        data = models.Occupation.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Relations(TemplateView):
    template_name = "tables/relations.html"

    def get(self, request):
        data = models.Relation.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class People(TemplateView):
    template_name = "tables/people.html"

    def get(self, request):
        data = models.Person.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class LocationTypes(TemplateView):
    template_name = "tables/location-types.html"

    def get(self, request):
        data = models.LocationType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Locations(TemplateView):
    template_name = "tables/locations.html"

    def get(self, request):
        data = models.Location.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class BuildingTypes(TemplateView):
    template_name = "tables/building-types.html"

    def get(self, request):
        data = models.BuildingType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Buildings(TemplateView):
    template_name = "tables/buildings.html"

    def get(self, request):
        data = models.Building.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class TypesOfFormat(TemplateView):
    template_name = "tables/types-of-format.html"

    def get(self, request):
        data = models.TypeOfFormat.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class FormatOfTexts(TemplateView):
    template_name = "tables/text-formats.html"

    def get(self, request):
        data = models.FormatOfText.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class PersonalMemories(TemplateView):
    template_name = "tables/personal-memories.html"

    def get(self, request):
        data = models.PersonalMemory.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class HistoricalPeriods(TemplateView):
    template_name = "tables/historical-periods.html"

    def get(self, request):
        data = models.HistoricalPeriod.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class HistoricalMemories(TemplateView):
    template_name = "tables/historical-memories.html"

    def get(self, request):
        data = models.HistoricalMemory.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class PoliticsPeriods(TemplateView):
    template_name = "tables/politics-periods.html"

    def get(self, request):
        data = models.PoliticsPeriod.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Politics(TemplateView):
    template_name = "tables/politics.html"

    def get(self, request):
        data = models.Politics.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Architectures(TemplateView):
    template_name = "tables/architectures.html"

    def get(self, request):
        data = models.Architecture.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Urbanism(TemplateView):
    template_name = "tables/urbanism.html"

    def get(self, request):
        data = models.Urbanism.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ArtCategories(TemplateView):
    template_name = "tables/art-categories.html"

    def get(self, request):
        data = models.ArtCategory.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ArtTypes(TemplateView):
    template_name = "tables/art-types.html"

    def get(self, request):
        data = models.ArtType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ArtStyles(TemplateView):
    template_name = "tables/art-styles.html"

    def get(self, request):
        data = models.ArtStyle.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ArtisticMovements(TemplateView):
    template_name = "tables/artistic-movements.html"

    def get(self, request):
        data = models.ArtisticMovement.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Arts(TemplateView):
    template_name = "tables/arts.html"

    def get(self, request):
        data = models.Art.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class CulturalLives(TemplateView):
    template_name = "tables/cultural-lives.html"

    def get(self, request):
        data = models.CulturalLife.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class AestheticMovements(TemplateView):
    template_name = "tables/aesthetic-movements.html"

    def get(self, request):
        data = models.AestheticMovement.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Aesthetics(TemplateView):
    template_name = "tables/aesthetics.html"

    def get(self, request):
        data = models.Aesthetic.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class LiteraryMovements(TemplateView):
    template_name = "tables/literary-movements.html"

    def get(self, request):
        data = models.LiteraryMovement.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class LiteraryGenres(TemplateView):
    template_name = "tables/literary-genres.html"

    def get(self, request):
        data = models.LiteraryGenre.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Literature(TemplateView):
    template_name = "tables/literature.html"

    def get(self, request):
        data = models.Literature.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class PopularCultures(TemplateView):
    template_name = "tables/popular-cultures.html"

    def get(self, request):
        data = models.PopularCulture.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Entertainment(TemplateView):
    template_name = "tables/entertainment.html"

    def get(self, request):
        data = models.Entertainment.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class MediaTypes(TemplateView):
    template_name = "tables/media-types.html"

    def get(self, request):
        data = models.MediaType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Media(TemplateView):
    template_name = "tables/media.html"

    def get(self, request):
        data = models.Media.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class LeisureTypes(TemplateView):
    template_name = "tables/leisure-types.html"

    def get(self, request):
        data = models.LeisureType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Leisure(TemplateView):
    template_name = "tables/leisure.html"

    def get(self, request):
        data = models.Leisure.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Fashion(TemplateView):
    template_name = "tables/fashion.html"

    def get(self, request):
        data = models.Fashion.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Consumerism(TemplateView):
    template_name = "tables/consumerism.html"

    def get(self, request):
        data = models.Consumerism.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class TypesOfScience(TemplateView):
    template_name = "tables/types-of-science.html"

    def get(self, request):
        data = models.TypeOfScience.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Sciences(TemplateView):
    template_name = "tables/sciences.html"

    def get(self, request):
        data = models.Science.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Objects(TemplateView):
    template_name = "tables/objects.html"

    def get(self, request):
        data = models.ObjectsMentioned.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


# FORMS ###############################################################################################################


class NewArticles(CreateView):
    template_name = "new/new-articles.html"
    model = models.Article
    form_class = forms.ArticleForm

    def get_context_data(self, **kwargs):
        context = super(NewArticles, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('articles')


class NewOccupations(CreateView):
    template_name = "new/new-occupations.html"
    model = models.Occupation
    form_class = forms.OccupationForm
    success_url = reverse_lazy('occupations')

    def get_context_data(self, **kwargs):
        context = super(NewOccupations, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewRelations(CreateView):
    template_name = "new/new-relations.html"
    model = models.Relation
    form_class = forms.RelationForm
    success_url = reverse_lazy('relations')

    def get_context_data(self, **kwargs):
        context = super(NewRelations, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewPeople(CreateView):
    template_name = "new/new-people.html"
    model = models.Person
    form_class = forms.PersonForm

    def get_context_data(self, **kwargs):
        context = super(NewPeople, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('people')


class NewLocationType(CreateView):
    template_name = "new/new-location-type.html"
    model = models.LocationType
    form_class = forms.LocationTypeForm
    success_url = reverse_lazy('location-types')

    def get_context_data(self, **kwargs):
        context = super(NewLocationType, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewLocations(CreateView):
    template_name = "new/new-locations.html"
    model = models.Location
    form_class = forms.LocationForm
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super(NewLocations, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        pnt = form.cleaned_data['geom']
        pnt.transform(4326)
        self.object.geom = pnt
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# class NewLocations(TemplateView):
#     template_name = "new/new-locations.html"
#
#     def get(self, request, **kwargs):
#         if 'id' in kwargs:
#             instance = models.Location.objects.get(pk=kwargs['id'])
#             form = forms.LocationForm(instance=instance, initial=handle_initial_status(instance.status, request.user))
#             title = "Edit"
#         else:
#             form = forms.LocationForm()
#             title = "New"
#         args = {'form': form, 'title': title}
#         return render(request, self.template_name, args)
#
#     def post(self, request, **kwargs):
#         form = forms.LocationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['geom'])
#             pnt = Point(form.cleaned_data['geom'].coords[0], form.cleaned_data['geom'].coords[1], srid=4326)
#             print(pnt)
#             if 'id' in kwargs:
#                 models.Location.objects.filter(pk=kwargs['id']).update(name=form.cleaned_data['name'],
#                                                                        type=form.cleaned_data['type'],
#                                                                        geom=pnt,
#                                                                        old_madrid=form.cleaned_data['old_madrid'],
#                                                                        status=handle_status(request.user,
#                                                                                             form.cleaned_data['complete']))
#             else:
#                 location = models.Location(name=form.cleaned_data['name'],
#                                            type=form.cleaned_data['type'],
#                                            geom=pnt,
#                                            old_madrid=form.cleaned_data['old_madrid'],
#                                            status=handle_status(request.user, form.cleaned_data['complete']))
#                 # location.save()
#
#             # Redirect the page if user clicked on one of the plus buttons
#             if 'new_page' in request.POST:
#                 return redirect(reverse('{}'.format(request.POST['new_page'])))
#             else:
#                 return redirect(reverse('locations'))
#
#         messages.error(request, form.errors)
#         args = {'form': form}
#         return render(request, self.template_name, args)


class NewBuildingType(CreateView):
    template_name = "new/new-building-types.html"
    model = models.BuildingType
    form_class = forms.BuildingTypeForm
    success_url = reverse_lazy('building-types')

    def get_context_data(self, **kwargs):
        context = super(NewBuildingType, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewBuildings(CreateView):
    template_name = "new/new-buildings.html"
    model = models.Building
    form_class = forms.BuildingForm
    success_url = reverse_lazy('buildings')

    def get_context_data(self, **kwargs):
        context = super(NewBuildings, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        pnt = form.cleaned_data['geom']
        pnt.transform(4326)
        self.object.geom = pnt
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# class NewBuildings(TemplateView):
#     template_name = "new/new-buildings.html"
#
#     def get(self, request, **kwargs):
#         if 'id' in kwargs:
#             instance = models.Building.objects.get(pk=kwargs['id'])
#             form = forms.BuildingForm(instance=instance, initial=handle_initial_status(instance.status, request.user))
#             title = "Edit"
#         else:
#             form = forms.BuildingForm()
#             title = "New"
#         args = {'form': form, 'title': title}
#         return render(request, self.template_name, args)
#
#     def post(self, request, **kwargs):
#         form = forms.BuildingForm(request.POST)
#         if form.is_valid():
#             pnt = Point(form.cleaned_data['geom'].coords[0], form.cleaned_data['geom'].coords[1])
#             if 'id' in kwargs:
#                 models.Building.objects.filter(pk=kwargs['id']).update(name=form.cleaned_data['name'],
#                                                                        type=form.cleaned_data['type'],
#                                                                        location=form.cleaned_data['location'],
#                                                                        geom=pnt,
#                                                                        old_madrid=form.cleaned_data['old_madrid'],
#                                                                        status=handle_status(request.user,
#                                                                                             form.cleaned_data['complete']))
#             else:
#                 building = models.Building(name=form.cleaned_data['name'],
#                                            type=form.cleaned_data['type'],
#                                            location=form.cleaned_data['location'],
#                                            geom=pnt,
#                                            old_madrid=form.cleaned_data['old_madrid'],
#                                            status=handle_status(request.user, form.cleaned_data['complete']))
#                 building.save()
#
#             # Redirect the page if user clicked on one of the plus buttons
#             if 'new_page' in request.POST:
#                 return redirect(reverse('{}'.format(request.POST['new_page'])))
#             else:
#                 return redirect(reverse('buildings'))
#
#         messages.error(request, form.errors)
#         args = {'form': form}
#         return render(request, self.template_name, args)


class NewTypesOfFormat(CreateView):
    template_name = "new/new-types-of-format.html"
    model = models.TypeOfFormat
    form_class = forms.TypeOfFormatForm
    success_url = reverse_lazy('types-of-format')

    def get_context_data(self, **kwargs):
        context = super(NewTypesOfFormat, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewFormatOfTexts(CreateView):
    template_name = "new/new-text-formats.html"
    model = models.FormatOfText
    form_class = forms.FormatOfTextForm

    def get_context_data(self, **kwargs):
        context = super(NewFormatOfTexts, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('text-formats')


class NewPersonalMemories(CreateView):
    template_name = "new/new-personal-memories.html"
    model = models.PersonalMemory
    form_class = forms.PersonalMemoryForm

    def get_context_data(self, **kwargs):
        context = super(NewPersonalMemories, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('personal-memories')


class NewHistoricalPeriods(CreateView):
    template_name = "new/new-historical-periods.html"
    model = models.HistoricalPeriod
    form_class = forms.HistoricalPeriodForm
    success_url = reverse_lazy('historical-periods')

    def get_context_data(self, **kwargs):
        context = super(NewHistoricalPeriods, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewHistoricalMemories(CreateView):
    template_name = "new/new-historical-memories.html"
    model = models.HistoricalMemory
    form_class = forms.HistoricalMemoryForm

    def get_context_data(self, **kwargs):
        context = super(NewHistoricalMemories, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('historical-memories')


class NewPoliticsPeriod(CreateView):
    template_name = "new/new-politics-periods.html"
    model = models.PoliticsPeriod
    form_class = forms.PoliticsPeriodForm
    success_url = reverse_lazy('politics-periods')

    def get_context_data(self, **kwargs):
        context = super(NewPoliticsPeriod, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewPolitics(CreateView):
    template_name = "new/new-politics.html"
    model = models.Politics
    form_class = forms.PoliticsForm

    def get_context_data(self, **kwargs):
        context = super(NewPolitics, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('politics')


class NewArchitectures(CreateView):
    template_name = "new/new-architectures.html"
    model = models.Architecture
    form_class = forms.ArchitectureForm

    def get_context_data(self, **kwargs):
        context = super(NewArchitectures, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('architectures')


class NewUrbanism(CreateView):
    template_name = "new/new-urbanism.html"
    model = models.Urbanism
    form_class = forms.UrbanismForm
    success_url = reverse_lazy('urbanism')

    def get_context_data(self, **kwargs):
        context = super(NewUrbanism, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewArtCategories(CreateView):
    template_name = "new/new-art-categories.html"
    model = models.ArtCategory
    form_class = forms.ArtCategoryForm
    success_url = reverse_lazy('art-categories')

    def get_context_data(self, **kwargs):
        context = super(NewArtCategories, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewArtTypes(CreateView):
    template_name = "new/new-art-types.html"
    model = models.ArtType
    form_class = forms.ArtTypeForm

    def get_context_data(self, **kwargs):
        context = super(NewArtTypes, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('art-types')


class NewArtStyles(CreateView):
    template_name = "new/new-art-styles.html"
    model = models.ArtStyle
    form_class = forms.ArtStyleForm
    success_url = reverse_lazy('art-styles')

    def get_context_data(self, **kwargs):
        context = super(NewArtStyles, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewArtisticMovements(CreateView):
    template_name = "new/new-artistic-movements.html"
    model = models.ArtisticMovement
    form_class = forms.ArtisticMovementForm
    success_url = reverse_lazy('artistic-movements')

    def get_context_data(self, **kwargs):
        context = super(NewArtisticMovements, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewArts(CreateView):
    template_name = "new/new-arts.html"
    model = models.Art
    form_class = forms.ArtForm

    def get_context_data(self, **kwargs):
        context = super(NewArts, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('arts')


class NewCulturalLives(CreateView):
    template_name = "new/new-cultural-lives.html"
    model = models.CulturalLife
    form_class = forms.CulturalLifeForm
    success_url = reverse_lazy('cultural-lives')

    def get_context_data(self, **kwargs):
        context = super(NewCulturalLives, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewAestheticMovements(CreateView):
    template_name = "new/new-aesthetic-movements.html"
    model = models.AestheticMovement
    form_class = forms.AestheticMovementForm
    success_url = reverse_lazy('aesthetic-movements')

    def get_context_data(self, **kwargs):
        context = super(NewAestheticMovements, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewAesthetics(CreateView):
    template_name = "new/new-aesthetics.html"
    model = models.Aesthetic
    form_class = forms.AestheticForm

    def get_context_data(self, **kwargs):
        context = super(NewAesthetics, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('aesthetics')


class NewLiteraryMovements(CreateView):
    template_name = "new/new-literary-movements.html"
    model = models.LiteraryMovement
    form_class = forms.LiteraryMovementForm
    success_url = reverse_lazy('literary-movements')

    def get_context_data(self, **kwargs):
        context = super(NewLiteraryMovements, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewLiteraryGenres(CreateView):
    template_name = "new/new-literary-genres.html"
    model = models.LiteraryGenre
    form_class = forms.LiteraryGenreForm
    success_url = reverse_lazy('literary-genres')

    def get_context_data(self, **kwargs):
        context = super(NewLiteraryGenres, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewLiterature(CreateView):
    template_name = "new/new-literature.html"
    model = models.Literature
    form_class = forms.LiteratureForm

    def get_context_data(self, **kwargs):
        context = super(NewLiterature, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('literature')


class NewPopularCultures(CreateView):
    template_name = "new/new-popular-cultures.html"
    model = models.PopularCulture
    form_class = forms.PopularCultureForm

    def get_context_data(self, **kwargs):
        context = super(NewPopularCultures, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('popular-cultures')


class NewEntertainment(CreateView):
    template_name = "new/new-entertainment.html"
    model = models.Entertainment
    form_class = forms.EntertainmentForm
    success_url = reverse_lazy('entertainment')

    def get_context_data(self, **kwargs):
        context = super(NewEntertainment, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewMediaTypes(CreateView):
    template_name = "new/new-media-types.html"
    model = models.MediaType
    form_class = forms.MediaTypeForm
    success_url = reverse_lazy('media-types')

    def get_context_data(self, **kwargs):
        context = super(NewMediaTypes, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewMedia(CreateView):
    template_name = "new/new-media.html"
    model = models.Media
    form_class = forms.MediaForm

    def get_context_data(self, **kwargs):
        context = super(NewMedia, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('media')


class NewLeisureTypes(CreateView):
    template_name = "new/new-leisure-types.html"
    model = models.LeisureType
    form_class = forms.LeisureTypeForm
    success_url = reverse_lazy('leisure-types')

    def get_context_data(self, **kwargs):
        context = super(NewLeisureTypes, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewLeisure(CreateView):
    template_name = "new/new-leisure.html"
    model = models.Leisure
    form_class = forms.LeisureForm

    def get_context_data(self, **kwargs):
        context = super(NewLeisure, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('leisure')


class NewFashion(CreateView):
    template_name = "new/new-fashion.html"
    model = models.Fashion
    form_class = forms.FashionForm
    success_url = reverse_lazy('fashion')

    def get_context_data(self, **kwargs):
        context = super(NewFashion, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewConsumerism(CreateView):
    template_name = "new/new-consumerism.html"
    model = models.Consumerism
    form_class = forms.ConsumerismForm

    def get_context_data(self, **kwargs):
        context = super(NewConsumerism, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('consumerism')


class NewTypesOfScience(CreateView):
    template_name = "new/new-types-of-science.html"
    model = models.TypeOfScience
    form_class = forms.TypeOfScienceForm
    success_url = reverse_lazy('types-of-science')

    def get_context_data(self, **kwargs):
        context = super(NewTypesOfScience, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewSciences(CreateView):
    template_name = "new/new-sciences.html"
    model = models.Science
    form_class = forms.ScienceForm
    success_url = reverse_lazy('sciences')

    def get_context_data(self, **kwargs):
        context = super(NewSciences, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewObjects(CreateView):
    template_name = "new/new-objects.html"
    model = models.ObjectsMentioned
    form_class = forms.ObjectsMentionedForm

    def get_context_data(self, **kwargs):
        context = super(NewObjects, self).get_context_data(**kwargs)
        context['title'] = "New"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('objects')


# Edit Methods ########################################################################################################


class EditArticles(UpdateView):
    template_name = "new/new-articles.html"
    model = models.Article
    form_class = forms.ArticleForm

    def get_context_data(self, **kwargs):
        context = super(EditArticles, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('articles')


class EditOccupations(UpdateView):
    template_name = "new/new-occupations.html"
    model = models.Occupation
    form_class = forms.OccupationForm
    success_url = reverse_lazy('occupations')

    def get_context_data(self, **kwargs):
        context = super(EditOccupations, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditRelations(UpdateView):
    template_name = "new/new-relations.html"
    model = models.Relation
    form_class = forms.RelationForm
    success_url = reverse_lazy('relations')

    def get_context_data(self, **kwargs):
        context = super(EditRelations, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditPeople(UpdateView):
    template_name = "new/new-people.html"
    model = models.Person
    form_class = forms.PersonForm

    def get_context_data(self, **kwargs):
        context = super(EditPeople, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('people')


class EditLocationType(UpdateView):
    template_name = "new/new-location-type.html"
    model = models.LocationType
    form_class = forms.LocationTypeForm
    success_url = reverse_lazy('location-types')

    def get_context_data(self, **kwargs):
        context = super(EditLocationType, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditLocations(UpdateView):
    template_name = "new/new-locations.html"
    model = models.Location
    form_class = forms.LocationForm
    success_url = reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super(EditLocations, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        initial_dict = handle_initial_status(self.object.status, self.request.user)
        if initial_dict:
            initial_dict["old_madrid"] = OLD_MADRID.get(self.object.old_madrid)
        else:
            initial_dict = {'old_madrid': OLD_MADRID.get(self.object.old_madrid)}
        return initial_dict

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        pnt = form.cleaned_data['geom']
        pnt.transform(4326)
        self.object.geom = pnt
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditBuildingType(UpdateView):
    template_name = "new/new-building-types.html"
    model = models.BuildingType
    form_class = forms.BuildingTypeForm
    success_url = reverse_lazy('building-types')

    def get_context_data(self, **kwargs):
        context = super(EditBuildingType, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditBuildings(UpdateView):
    template_name = "new/new-buildings.html"
    model = models.Building
    form_class = forms.BuildingForm
    success_url = reverse_lazy('buildings')

    def get_context_data(self, **kwargs):
        context = super(EditBuildings, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        initial_dict = handle_initial_status(self.object.status, self.request.user)
        if initial_dict:
            initial_dict["old_madrid"] = OLD_MADRID.get(self.object.old_madrid)
        else:
            initial_dict = {'old_madrid': OLD_MADRID.get(self.object.old_madrid)}
        return initial_dict

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        pnt = form.cleaned_data['geom']
        pnt.transform(4326)
        self.object.geom = pnt
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditTypesOfFormat(UpdateView):
    template_name = "new/new-types-of-format.html"
    model = models.TypeOfFormat
    form_class = forms.TypeOfFormatForm
    success_url = reverse_lazy('types-of-format')

    def get_context_data(self, **kwargs):
        context = super(EditTypesOfFormat, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditFormatOfTexts(UpdateView):
    template_name = "new/new-text-formats.html"
    model = models.FormatOfText
    form_class = forms.FormatOfTextForm

    def get_context_data(self, **kwargs):
        context = super(EditFormatOfTexts, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('text-formats')


class EditPersonalMemories(UpdateView):
    template_name = "new/new-personal-memories.html"
    model = models.PersonalMemory
    form_class = forms.PersonalMemoryForm

    def get_context_data(self, **kwargs):
        context = super(EditPersonalMemories, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('personal-memories')


class EditHistoricalPeriods(UpdateView):
    template_name = "new/new-historical-periods.html"
    model = models.HistoricalPeriod
    form_class = forms.HistoricalPeriodForm
    success_url = reverse_lazy('historical-periods')

    def get_context_data(self, **kwargs):
        context = super(EditHistoricalPeriods, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditHistoricalMemories(UpdateView):
    template_name = "new/new-historical-memories.html"
    model = models.HistoricalMemory
    form_class = forms.HistoricalMemoryForm

    def get_context_data(self, **kwargs):
        context = super(EditHistoricalMemories, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('historical-memories')


class EditPoliticsPeriod(UpdateView):
    template_name = "new/new-politics-periods.html"
    model = models.PoliticsPeriod
    form_class = forms.PoliticsPeriodForm
    success_url = reverse_lazy('politics-periods')

    def get_context_data(self, **kwargs):
        context = super(EditPoliticsPeriod, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditPolitics(UpdateView):
    template_name = "new/new-politics.html"
    model = models.Politics
    form_class = forms.PoliticsForm

    def get_context_data(self, **kwargs):
        context = super(EditPolitics, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('politics')


class EditArchitectures(UpdateView):
    template_name = "new/new-architectures.html"
    model = models.Architecture
    form_class = forms.ArchitectureForm

    def get_context_data(self, **kwargs):
        context = super(EditArchitectures, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('architectures')


class EditUrbanism(UpdateView):
    template_name = "new/new-urbanism.html"
    model = models.Urbanism
    form_class = forms.UrbanismForm
    success_url = reverse_lazy('urbanism')

    def get_context_data(self, **kwargs):
        context = super(EditUrbanism, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditArtCategories(UpdateView):
    template_name = "new/new-art-categories.html"
    model = models.ArtCategory
    form_class = forms.ArtCategoryForm
    success_url = reverse_lazy('art-categories')

    def get_context_data(self, **kwargs):
        context = super(EditArtCategories, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditArtTypes(UpdateView):
    template_name = "new/new-art-types.html"
    model = models.ArtType
    form_class = forms.ArtTypeForm

    def get_context_data(self, **kwargs):
        context = super(EditArtTypes, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('art-types')


class EditArtStyles(UpdateView):
    template_name = "new/new-art-styles.html"
    model = models.ArtStyle
    form_class = forms.ArtStyleForm
    success_url = reverse_lazy('art-styles')

    def get_context_data(self, **kwargs):
        context = super(EditArtStyles, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditArtisticMovements(UpdateView):
    template_name = "new/new-artistic-movements.html"
    model = models.ArtisticMovement
    form_class = forms.ArtisticMovementForm
    success_url = reverse_lazy('artistic-movements')

    def get_context_data(self, **kwargs):
        context = super(EditArtisticMovements, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditArts(UpdateView):
    template_name = "new/new-arts.html"
    model = models.Art
    form_class = forms.ArtForm

    def get_context_data(self, **kwargs):
        context = super(EditArts, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('arts')


class EditCulturalLives(UpdateView):
    template_name = "new/new-cultural-lives.html"
    model = models.CulturalLife
    form_class = forms.CulturalLifeForm
    success_url = reverse_lazy('cultural-lives')

    def get_context_data(self, **kwargs):
        context = super(EditCulturalLives, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditAestheticMovements(UpdateView):
    template_name = "new/new-aesthetic-movements.html"
    model = models.AestheticMovement
    form_class = forms.AestheticMovementForm
    success_url = reverse_lazy('aesthetic-movements')

    def get_context_data(self, **kwargs):
        context = super(EditAestheticMovements, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditAesthetics(UpdateView):
    template_name = "new/new-aesthetics.html"
    model = models.Aesthetic
    form_class = forms.AestheticForm

    def get_context_data(self, **kwargs):
        context = super(EditAesthetics, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('aesthetics')


class EditLiteraryMovements(UpdateView):
    template_name = "new/new-literary-movements.html"
    model = models.LiteraryMovement
    form_class = forms.LiteraryMovementForm
    success_url = reverse_lazy('literary-movements')

    def get_context_data(self, **kwargs):
        context = super(EditLiteraryMovements, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditLiteraryGenres(UpdateView):
    template_name = "new/new-literary-genres.html"
    model = models.LiteraryGenre
    form_class = forms.LiteraryGenreForm
    success_url = reverse_lazy('literary-genres')

    def get_context_data(self, **kwargs):
        context = super(EditLiteraryGenres, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditLiterature(UpdateView):
    template_name = "new/new-literature.html"
    model = models.Literature
    form_class = forms.LiteratureForm

    def get_context_data(self, **kwargs):
        context = super(EditLiterature, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('literature')


class EditPopularCultures(UpdateView):
    template_name = "new/new-popular-cultures.html"
    model = models.PopularCulture
    form_class = forms.PopularCultureForm

    def get_context_data(self, **kwargs):
        context = super(EditPopularCultures, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('popular-cultures')


class EditEntertainment(UpdateView):
    template_name = "new/new-entertainment.html"
    model = models.Entertainment
    form_class = forms.EntertainmentForm
    success_url = reverse_lazy('entertainment')

    def get_context_data(self, **kwargs):
        context = super(EditEntertainment, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditMediaTypes(UpdateView):
    template_name = "new/new-media-types.html"
    model = models.MediaType
    form_class = forms.MediaTypeForm
    success_url = reverse_lazy('media-types')

    def get_context_data(self, **kwargs):
        context = super(EditMediaTypes, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditMedia(UpdateView):
    template_name = "new/new-media.html"
    model = models.Media
    form_class = forms.MediaForm

    def get_context_data(self, **kwargs):
        context = super(EditMedia, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('media')


class EditLeisureTypes(UpdateView):
    template_name = "new/new-leisure-types.html"
    model = models.LeisureType
    form_class = forms.LeisureTypeForm
    success_url = reverse_lazy('leisure-types')

    def get_context_data(self, **kwargs):
        context = super(EditLeisureTypes, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditLeisure(UpdateView):
    template_name = "new/new-leisure.html"
    model = models.Leisure
    form_class = forms.LeisureForm

    def get_context_data(self, **kwargs):
        context = super(EditLeisure, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('leisure')


class EditFashion(UpdateView):
    template_name = "new/new-fashion.html"
    model = models.Fashion
    form_class = forms.FashionForm
    success_url = reverse_lazy('fashion')

    def get_context_data(self, **kwargs):
        context = super(EditFashion, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditConsumerism(UpdateView):
    template_name = "new/new-consumerism.html"
    model = models.Consumerism
    form_class = forms.ConsumerismForm

    def get_context_data(self, **kwargs):
        context = super(EditConsumerism, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('consumerism')


class EditTypesOfScience(UpdateView):
    template_name = "new/new-types-of-science.html"
    model = models.TypeOfScience
    form_class = forms.TypeOfScienceForm
    success_url = reverse_lazy('types-of-science')

    def get_context_data(self, **kwargs):
        context = super(EditTypesOfScience, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditSciences(UpdateView):
    template_name = "new/new-sciences.html"
    model = models.Science
    form_class = forms.ScienceForm
    success_url = reverse_lazy('sciences')

    def get_context_data(self, **kwargs):
        context = super(EditSciences, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class EditObjects(UpdateView):
    template_name = "new/new-objects.html"
    model = models.ObjectsMentioned
    form_class = forms.ObjectsMentionedForm

    def get_context_data(self, **kwargs):
        context = super(EditObjects, self).get_context_data(**kwargs)
        context['title'] = "Edit"
        return context

    def get_initial(self):
        return handle_initial_status(self.object.status, self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = handle_status(self.request.user, form.cleaned_data['complete'])
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.POST.get("new_page"):
            return reverse_lazy('{}'.format(self.request.POST.get("new_page")))
        else:
            return reverse_lazy('objects')


# Delete Methods ######################################################################################################


class DeleteArticles(TemplateView):

    def get(self, request, id):
        models.Article.objects.filter(id=id).delete()
        return redirect(reverse('articles'))


class DeleteOccupations(TemplateView):

    def get(self, request, id):
        models.Occupation.objects.filter(id=id).delete()
        return redirect(reverse('occupations'))


class DeleteRelations(TemplateView):

    def get(self, request, id):
        models.Relation.objects.filter(id=id).delete()
        return redirect(reverse('relations'))


class DeletePeople(TemplateView):

    def get(self, request, id):
        models.Person.objects.filter(id=id).delete()
        return redirect(reverse('people'))


class DeleteLocationTypes(TemplateView):

    def get(self, request, id):
        models.LocationType.objects.filter(id=id).delete()
        return redirect(reverse('location-types'))


class DeleteLocation(TemplateView):

    def get(self, request, id):
        models.Location.objects.filter(id=id).delete()
        return redirect(reverse('locations'))


class DeleteBuildingTypes(TemplateView):

    def get(self, request, id):
        models.BuildingType.objects.filter(id=id).delete()
        return redirect(reverse('building-types'))


class DeleteBuildings(TemplateView):

    def get(self, request, id):
        models.Building.objects.filter(id=id).delete()
        return redirect(reverse('buildings'))


class DeleteTypesOfFormat(TemplateView):

    def get(self, request, id):
        models.TypeOfFormat.objects.filter(id=id).delete()
        return redirect(reverse('types-of-format'))


class DeleteFormatOfTexts(TemplateView):

    def get(self, request, id):
        models.FormatOfText.objects.filter(id=id).delete()
        return redirect(reverse('text-formats'))


class DeletePersonalMemories(TemplateView):

    def get(self, request, id):
        models.PersonalMemory.objects.filter(id=id).delete()
        return redirect(reverse('personal-memories'))


class DeleteHistoricalPeriods(TemplateView):

    def get(self, request, id):
        models.HistoricalPeriod.objects.filter(id=id).delete()
        return redirect(reverse('historical-periods'))


class DeleteHistoricalMemories(TemplateView):

    def get(self, request, id):
        models.HistoricalMemory.objects.filter(id=id).delete()
        return redirect(reverse('historical-memories'))


class DeletePoliticsPeriod(TemplateView):

    def get(self, request, id):
        models.PoliticsPeriod.objects.filter(id=id).delete()
        return redirect(reverse('politics-periods'))


class DeletePolitics(TemplateView):

    def get(self, request, id):
        models.Politics.objects.filter(id=id).delete()
        return redirect(reverse('politics'))


class DeleteArchitectures(TemplateView):

    def get(self, request, id):
        models.Architecture.objects.filter(id=id).delete()
        return redirect(reverse('architectures'))


class DeleteUrbanism(TemplateView):

    def get(self, request, id):
        models.Urbanism.objects.filter(id=id).delete()
        return redirect(reverse('urbanism'))


class DeleteArtCategories(TemplateView):

    def get(self, request, id):
        models.ArtCategory.objects.filter(id=id).delete()
        return redirect(reverse('art-categories'))


class DeleteArtTypes(TemplateView):

    def get(self, request, id):
        models.ArtType.objects.filter(id=id).delete()
        return redirect(reverse('art-types'))


class DeleteArtStyles(TemplateView):

    def get(self, request, id):
        models.ArtStyle.objects.filter(id=id).delete()
        return redirect(reverse('art-styles'))


class DeleteArtisticMovements(TemplateView):

    def get(self, request, id):
        models.ArtisticMovement.objects.filter(id=id).delete()
        return redirect(reverse('artistic-movements'))


class DeleteArts(TemplateView):

    def get(self, request, id):
        models.Art.objects.filter(id=id).delete()
        return redirect(reverse('arts'))


class DeleteCulturalLives(TemplateView):

    def get(self, request, id):
        models.CulturalLife.objects.filter(id=id).delete()
        return redirect(reverse('cultural-lives'))


class DeleteAestheticMovements(TemplateView):

    def get(self, request, id):
        models.AestheticMovement.objects.filter(id=id).delete()
        return redirect(reverse('aesthetic-movements'))


class DeleteAesthetics(TemplateView):

    def get(self, request, id):
        models.Aesthetic.objects.filter(id=id).delete()
        return redirect(reverse('aesthetics'))


class DeleteLiteraryMovements(TemplateView):

    def get(self, request, id):
        models.LiteraryMovement.objects.filter(id=id).delete()
        return redirect(reverse('literary-movements'))


class DeleteLiteraryGenres(TemplateView):

    def get(self, request, id):
        models.LiteraryGenre.objects.filter(id=id).delete()
        return redirect(reverse('literary-genres'))


class DeleteLiterature(TemplateView):

    def get(self, request, id):
        models.Literature.objects.filter(id=id).delete()
        return redirect(reverse('literature'))


class DeletePopularCultures(TemplateView):

    def get(self, request, id):
        models.PopularCulture.objects.filter(id=id).delete()
        return redirect(reverse('popular-cultures'))


class DeleteEntertainment(TemplateView):

    def get(self, request, id):
        models.Entertainment.objects.filter(id=id).delete()
        return redirect(reverse('entertainment'))


class DeleteMediaTypes(TemplateView):

    def get(self, request, id):
        models.MediaType.objects.filter(id=id).delete()
        return redirect(reverse('media-types'))


class DeleteMedia(TemplateView):

    def get(self, request, id):
        models.Media.objects.filter(id=id).delete()
        return redirect(reverse('media'))


class DeleteLeisureTypes(TemplateView):

    def get(self, request, id):
        models.LeisureType.objects.filter(id=id).delete()
        return redirect(reverse('leisure-types'))


class DeleteLeisure(TemplateView):

    def get(self, request, id):
        models.Leisure.objects.filter(id=id).delete()
        return redirect(reverse('leisure'))


class DeleteFashion(TemplateView):

    def get(self, request, id):
        models.Fashion.objects.filter(id=id).delete()
        return redirect(reverse('fashion'))


class DeleteConsumerism(TemplateView):

    def get(self, request, id):
        models.Consumerism.objects.filter(id=id).delete()
        return redirect(reverse('consumerism'))


class DeleteTypesOfScience(TemplateView):

    def get(self, request, id):
        models.TypeOfScience.objects.filter(id=id).delete()
        return redirect(reverse('types-of-science'))


class DeleteSciences(TemplateView):

    def get(self, request, id):
        models.Science.objects.filter(id=id).delete()
        return redirect(reverse('sciences'))


class DeleteObjects(TemplateView):

    def get(self, request, id):
        models.ObjectsMentioned.objects.filter(id=id).delete()
        return redirect(reverse('objects'))


def load_art_types(request):
    category_id = request.GET.get('category')
    types = models.ArtType.objects.filter(category_id=category_id, status='R')
    return render(request, 'new/art_type_dropdown_list_options.html', {'types': types})


def load_text_format(request):
    type_of_format_id = request.GET.get('type_of_format')
    text_format = models.FormatOfText.objects.filter(type_id=type_of_format_id, status='R')
    return render(request, 'new/text_format_dropdown_list_options.html', {'text_format': text_format})


def handle_status(user, complete):
    if complete:
        if user.is_superuser:
            return 'R'
        else:
            return 'RR'
    else:
        return 'I'


def handle_initial_status(status, user):
    if status == 'RR':
        if not user.is_superuser:
            return {'complete': True}
    elif status == 'R':
        return {'complete': True}
