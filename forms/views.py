from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.gis.geos import Point
from forms import models
from forms import forms


# Create your views here.
class Index(TemplateView):
    template_name = "index.html"


class Articles(TemplateView):
    template_name = "tables/home.html"

    def get(self, request):
        data = models.Article.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Locations(TemplateView):
    template_name = "tables/locations.html"

    def get(self, request):
        data = models.Location.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class LocationTypes(TemplateView):
    template_name = "tables/location-types.html"

    def get(self, request):
        data = models.LocationType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Buildings(TemplateView):
    template_name = "tables/buildings.html"

    def get(self, request):
        data = models.Building.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class BuildingTypes(TemplateView):
    template_name = "tables/building-types.html"

    def get(self, request):
        data = models.BuildingType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Arts(TemplateView):
    template_name = "tables/arts.html"

    def get(self, request):
        data = models.Art.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ArtTypes(TemplateView):
    template_name = "tables/art-types.html"

    def get(self, request):
        data = models.ArtType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ArtistTypes(TemplateView):
    template_name = "tables/artist-types.html"

    def get(self, request):
        data = models.ArtistType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Artists(TemplateView):
    template_name = "tables/artists.html"

    def get(self, request):
        data = models.Artist.objects.all()
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


class AppliedArts(TemplateView):
    template_name = "tables/applied-arts.html"

    def get(self, request):
        data = models.AppliedArt.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class FormatOfTexts(TemplateView):
    template_name = "tables/text-formats.html"

    def get(self, request):
        data = models.FormatOfText.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Politics(TemplateView):
    template_name = "tables/politics.html"

    def get(self, request):
        data = models.Politics.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class PoliticsPeriod(TemplateView):
    template_name = "tables/politics-periods.html"

    def get(self, request):
        data = models.PoliticsPeriod.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Biographies(TemplateView):
    template_name = "tables/biographies.html"

    def get(self, request):
        data = models.Biography.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Relations(TemplateView):
    template_name = "tables/relations.html"

    def get(self, request):
        data = models.Relation.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class BiographyPeriod(TemplateView):
    template_name = "tables/biography-periods.html"

    def get(self, request):
        data = models.Period.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Urbanism(TemplateView):
    template_name = "tables/urbanism.html"

    def get(self, request):
        data = models.Urbanism.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Architectures(TemplateView):
    template_name = "tables/architectures.html"

    def get(self, request):
        data = models.Architecture.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class CulturalLife(TemplateView):
    template_name = "tables/cultural-life.html"

    def get(self, request):
        data = models.CulturalLife.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Literature(TemplateView):
    template_name = "tables/literature.html"

    def get(self, request):
        data = models.Literature.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Movements(TemplateView):
    template_name = "tables/movements.html"

    def get(self, request):
        data = models.Movement.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Writers(TemplateView):
    template_name = "tables/writers.html"

    def get(self, request):
        data = models.Writer.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class PopularCultures(TemplateView):
    template_name = "tables/popular-cultures.html"

    def get(self, request):
        data = models.PopularCulture.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class CultureTypes(TemplateView):
    template_name = "tables/culture-types.html"

    def get(self, request):
        data = models.CultureType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Entertainment(TemplateView):
    template_name = "tables/entertainment.html"

    def get(self, request):
        data = models.Entertainment.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Media(TemplateView):
    template_name = "tables/media.html"

    def get(self, request):
        data = models.Media.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class MediaTypes(TemplateView):
    template_name = "tables/media-types.html"

    def get(self, request):
        data = models.MediaType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Objects(TemplateView):
    template_name = "tables/objects.html"

    def get(self, request):
        data = models.ObjectsMentioned.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Psychology(TemplateView):
    template_name = "tables/psychology.html"

    def get(self, request):
        data = models.Psychology.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class SocialIssues(TemplateView):
    template_name = "tables/social-issues.html"

    def get(self, request):
        data = models.SocialIssue.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class SocialScience(TemplateView):
    template_name = "tables/social-science.html"

    def get(self, request):
        data = models.SocialScience.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Consumerism(TemplateView):
    template_name = "tables/consumerism.html"

    def get(self, request):
        data = models.Consumerism.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class ConsumerismTypes(TemplateView):
    template_name = "tables/consumerism-types.html"

    def get(self, request):
        data = models.ConsumerismType.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class MedicalScience(TemplateView):
    template_name = "tables/medical-science.html"

    def get(self, request):
        data = models.MedicalScience.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


class Technologies(TemplateView):
    template_name = "tables/technologies.html"

    def get(self, request):
        data = models.Technology.objects.all()
        args = {'data': data}
        return render(request, self.template_name, args)


# FORMS ###############################################################################################################


class NewLocations(TemplateView):
    template_name = "tables/new/new-locations.html"

    def get(self, request, **kwargs):
        if 'id' in kwargs:
            instance = models.Location.objects.get(pk=kwargs['id'])
            form = forms.LocationForm(instance=instance)
        else:
            form = forms.LocationForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request, **kwargs):
        form = forms.LocationForm(request.POST)
        if form.is_valid():
            if 'id' in kwargs:
                instance = models.Location.objects.get(pk=kwargs['id'])
                form = forms.LocationForm(request.POST, instance=instance)
                models.Location.objects.filter(pk=kwargs['id']).update(name=form.data['name'],
                                                                       type=models.LocationType.objects.get(
                                                                           pk=form.data['type']),
                                                                       coordinates=form.data['coordinates'],
                                                                       old_madrid=form.data['old_madrid'], )
            else:
                pnt = Point(form.cleaned_data['coordinates'].coords[0], form.cleaned_data['coordinates'].coords[1])
                location = models.Location(name=form.cleaned_data['name'],
                                           type=form.cleaned_data['type'],
                                           coordinates=pnt,
                                           old_madrid=form.cleaned_data['old_madrid'], )
                location.save()
            return redirect(reverse('locations'))


class NewLocationType(CreateView):
    template_name = "tables/new/new-location-type.html"
    model = models.LocationType
    form_class = forms.LocationTypeForm
    success_url = reverse_lazy('location-types')


class NewBuildings(TemplateView):
    template_name = "tables/new/new-buildings.html"

    def get(self, request, **kwargs):
        if 'id' in kwargs:
            instance = models.Building.objects.get(pk=kwargs['id'])
            form = forms.BuildingForm(instance=instance)
        else:
            form = forms.BuildingForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request, **kwargs):
        form = forms.BuildingForm(request.POST)
        if form.is_valid():
            if 'id' in kwargs:
                instance = models.Building.objects.get(pk=kwargs['id'])
                form = forms.BuildingForm(request.POST, instance=instance)
                models.Building.objects.filter(pk=kwargs['id']).update(name=form.data['name'],
                                                                       type=models.BuildingType.objects.get(
                                                                           pk=form.data['type']),
                                                                       location=models.Location.objects.get(
                                                                           pk=form.data['location']),
                                                                       coordinates=form.data['coordinates'],
                                                                       old_madrid=form.data['old_madrid'], )
            else:
                pnt = Point(form.cleaned_data['coordinates'].coords[0], form.cleaned_data['coordinates'].coords[1])
                building = models.Building(name=form.cleaned_data['name'],
                                           type=form.cleaned_data['type'],
                                           location=form.cleaned_data['location'],
                                           coordinates=pnt,
                                           old_madrid=form.cleaned_data['old_madrid'], )
                building.save()
            return redirect(reverse('buildings'))


class NewBuildingType(CreateView):
    template_name = "tables/new/new-building-types.html"
    model = models.BuildingType
    form_class = forms.BuildingTypeForm
    success_url = reverse_lazy('building-types')


class NewArts(CreateView):
    template_name = "tables/new/new-arts.html"
    model = models.Art
    form_class = forms.ArtForm
    success_url = reverse_lazy('arts')


class NewArtTypes(CreateView):
    template_name = "tables/new/new-art-types.html"
    model = models.ArtType
    form_class = forms.ArtTypeForm
    success_url = reverse_lazy('art-types')


class NewArtistTypes(CreateView):
    template_name = "tables/new/new-artist-types.html"
    model = models.ArtistType
    form_class = forms.ArtistTypeForm
    success_url = reverse_lazy('artist-types')


class NewArtists(CreateView):
    template_name = "tables/new/new-artists.html"
    model = models.Artist
    form_class = forms.ArtistForm
    success_url = reverse_lazy('artists')


class NewArtStyles(CreateView):
    template_name = "tables/new/new-art-styles.html"
    model = models.ArtStyle
    form_class = forms.ArtStyleForm
    success_url = reverse_lazy('art-styles')


class NewArtisticMovements(CreateView):
    template_name = "tables/new/new-artistic-movements.html"
    model = models.ArtisticMovement
    form_class = forms.ArtisticMovementForm
    success_url = reverse_lazy('artistic-movements')


class NewAppliedArts(CreateView):
    template_name = "tables/new/new-applied-arts.html"
    model = models.AppliedArt
    form_class = forms.AppliedArtForm
    success_url = reverse_lazy('applied-arts')


class NewFormatOfTexts(CreateView):
    template_name = "tables/new/new-text-formats.html"
    model = models.FormatOfText
    form_class = forms.FormatOfTextForm
    success_url = reverse_lazy('text-formats')


class NewPoliticsPeriod(CreateView):
    template_name = "tables/new/new-politics-periods.html"
    model = models.PoliticsPeriod
    form_class = forms.PoliticsPeriodForm
    success_url = reverse_lazy('politics-periods')


class NewPolitics(CreateView):
    template_name = "tables/new/new-politics.html"
    model = models.Politics
    form_class = forms.PoliticsForm
    success_url = reverse_lazy('politics')


class NewRelations(CreateView):
    template_name = "tables/new/new-relations.html"
    model = models.Relation
    form_class = forms.RelationForm
    success_url = reverse_lazy('relations')


class NewBiographyPeriod(CreateView):
    template_name = "tables/new/new-biography-periods.html"
    model = models.Period
    form_class = forms.PeriodForm
    success_url = reverse_lazy('biography-periods')


class NewBiographies(CreateView):
    template_name = "tables/new/new-biographies.html"
    model = models.Biography
    form_class = forms.BiographyForm
    success_url = reverse_lazy('biographies')


class NewUrbanism(CreateView):
    template_name = "tables/new/new-urbanism.html"
    model = models.Urbanism
    form_class = forms.UrbanismForm
    success_url = reverse_lazy('urbanism')


class NewArchitectures(CreateView):
    template_name = "tables/new/new-architectures.html"
    model = models.Architecture
    form_class = forms.ArchitectureForm
    success_url = reverse_lazy('architectures')


class NewCulturalLife(CreateView):
    template_name = "tables/new/new-cultural-life.html"
    model = models.CulturalLife
    form_class = forms.CulturalLifeForm
    success_url = reverse_lazy('cultural-life')


class NewMovements(CreateView):
    template_name = "tables/new/new-movements.html"
    model = models.Movement
    form_class = forms.MovementForm
    success_url = reverse_lazy('movements')


class NewWriters(CreateView):
    template_name = "tables/new/new-writers.html"
    model = models.Writer
    form_class = forms.WriterForm
    success_url = reverse_lazy('writers')


class NewLiterature(CreateView):
    template_name = "tables/new/new-literature.html"
    model = models.Literature
    form_class = forms.LiteratureForm
    success_url = reverse_lazy('literature')


class NewCultureTypes(CreateView):
    template_name = "tables/new/new-culture-types.html"
    model = models.CultureType
    form_class = forms.CultureTypeForm
    success_url = reverse_lazy('culture-types')


class NewPopularCultures(CreateView):
    template_name = "tables/new/new-popular-cultures.html"
    model = models.PopularCulture
    form_class = forms.PopularCultureForm
    success_url = reverse_lazy('popular-cultures')


class NewEntertainment(CreateView):
    template_name = "tables/new/new-entertainment.html"
    model = models.Entertainment
    form_class = forms.EntertainmentForm
    success_url = reverse_lazy('entertainment')


class NewMediaTypes(CreateView):
    template_name = "tables/new/new-media-types.html"
    model = models.MediaType
    form_class = forms.MediaTypeForm
    success_url = reverse_lazy('media-types')


class NewMedia(CreateView):
    template_name = "tables/new/new-media.html"
    model = models.Media
    form_class = forms.MediaForm
    success_url = reverse_lazy('media')


class NewObjects(CreateView):
    template_name = "tables/new/new-objects.html"
    model = models.ObjectsMentioned
    form_class = forms.ObjectsMentionedForm
    success_url = reverse_lazy('objects')


class NewPsychology(CreateView):
    template_name = "tables/new/new-psychology.html"
    model = models.Psychology
    form_class = forms.PsychologyForm
    success_url = reverse_lazy('psychology')


class NewSocialIssues(CreateView):
    template_name = "tables/new/new-social-issues.html"
    model = models.SocialIssue
    form_class = forms.SocialIssueForm
    success_url = reverse_lazy('social-issues')


class NewSocialScience(CreateView):
    template_name = "tables/new/new-social-science.html"
    model = models.SocialScience
    form_class = forms.SocialScienceForm
    success_url = reverse_lazy('social-science')


class NewConsumerismTypes(CreateView):
    template_name = "tables/new/new-consumerism-types.html"
    model = models.ConsumerismType
    form_class = forms.ConsumerismTypeForm
    success_url = reverse_lazy('consumerism-types')


class NewConsumerism(CreateView):
    template_name = "tables/new/new-consumerism.html"
    model = models.Consumerism
    form_class = forms.ConsumerismForm
    success_url = reverse_lazy('consumerism')


class NewArticles(CreateView):
    template_name = "tables/new/new-articles.html"
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy('home')


class NewMedicalScience(CreateView):
    template_name = "tables/new/new-medical-science.html"
    model = models.MedicalScience
    form_class = forms.MedicalScienceForm
    success_url = reverse_lazy('medical-science')


class NewTechnologies(CreateView):
    template_name = "tables/new/new-technologies.html"
    model = models.Technology
    form_class = forms.TechnologyForm
    success_url = reverse_lazy('technologies')


# Edit Methods ########################################################################################################

class EditLocationType(UpdateView):
    template_name = "tables/new/new-location-type.html"
    model = models.LocationType
    form_class = forms.LocationTypeForm
    success_url = reverse_lazy('location-types')


class EditBuildingType(UpdateView):
    template_name = "tables/new/new-building-types.html"
    model = models.BuildingType
    form_class = forms.BuildingTypeForm
    success_url = reverse_lazy('building-types')


class EditArts(UpdateView):
    template_name = "tables/new/new-arts.html"
    model = models.Art
    form_class = forms.ArtForm
    success_url = reverse_lazy('arts')


class EditArtTypes(UpdateView):
    template_name = "tables/new/new-art-types.html"
    model = models.ArtType
    form_class = forms.ArtTypeForm
    success_url = reverse_lazy('art-types')


class EditArtistTypes(UpdateView):
    template_name = "tables/new/new-artist-types.html"
    model = models.ArtistType
    form_class = forms.ArtistTypeForm
    success_url = reverse_lazy('artist-types')


class EditArtists(UpdateView):
    template_name = "tables/new/new-artists.html"
    model = models.Artist
    form_class = forms.ArtistForm
    success_url = reverse_lazy('artists')


class EditArtStyles(UpdateView):
    template_name = "tables/new/new-art-styles.html"
    model = models.ArtStyle
    form_class = forms.ArtStyleForm
    success_url = reverse_lazy('art-styles')


class EditArtisticMovements(UpdateView):
    template_name = "tables/new/new-artistic-movements.html"
    model = models.ArtisticMovement
    form_class = forms.ArtisticMovementForm
    success_url = reverse_lazy('artistic-movements')


class EditAppliedArts(UpdateView):
    template_name = "tables/new/new-applied-arts.html"
    model = models.AppliedArt
    form_class = forms.AppliedArtForm
    success_url = reverse_lazy('applied-arts')


class EditFormatOfTexts(UpdateView):
    template_name = "tables/new/new-text-formats.html"
    model = models.FormatOfText
    form_class = forms.FormatOfTextForm
    success_url = reverse_lazy('text-formats')


class EditPoliticsPeriod(UpdateView):
    template_name = "tables/new/new-politics-periods.html"
    model = models.PoliticsPeriod
    form_class = forms.PoliticsPeriodForm
    success_url = reverse_lazy('politics-periods')


class EditPolitics(UpdateView):
    template_name = "tables/new/new-politics.html"
    model = models.Politics
    form_class = forms.PoliticsForm
    success_url = reverse_lazy('politics')


class EditRelations(UpdateView):
    template_name = "tables/new/new-relations.html"
    model = models.Relation
    form_class = forms.RelationForm
    success_url = reverse_lazy('relations')


class EditBiographyPeriod(UpdateView):
    template_name = "tables/new/new-biography-periods.html"
    model = models.Period
    form_class = forms.PeriodForm
    success_url = reverse_lazy('biography-periods')


class EditBiographies(UpdateView):
    template_name = "tables/new/new-biographies.html"
    model = models.Biography
    form_class = forms.BiographyForm
    success_url = reverse_lazy('biographies')


class EditUrbanism(UpdateView):
    template_name = "tables/new/new-urbanism.html"
    model = models.Urbanism
    form_class = forms.UrbanismForm
    success_url = reverse_lazy('urbanism')


class EditArchitectures(UpdateView):
    template_name = "tables/new/new-architectures.html"
    model = models.Architecture
    form_class = forms.ArchitectureForm
    success_url = reverse_lazy('architectures')


class EditCulturalLife(UpdateView):
    template_name = "tables/new/new-cultural-life.html"
    model = models.CulturalLife
    form_class = forms.CulturalLifeForm
    success_url = reverse_lazy('cultural-life')


class EditMovements(UpdateView):
    template_name = "tables/new/new-movements.html"
    model = models.Movement
    form_class = forms.MovementForm
    success_url = reverse_lazy('movements')


class EditWriters(UpdateView):
    template_name = "tables/new/new-writers.html"
    model = models.Writer
    form_class = forms.WriterForm
    success_url = reverse_lazy('writers')


class EditLiterature(UpdateView):
    template_name = "tables/new/new-literature.html"
    model = models.Literature
    form_class = forms.LiteratureForm
    success_url = reverse_lazy('literature')


class EditCultureTypes(UpdateView):
    template_name = "tables/new/new-culture-types.html"
    model = models.CultureType
    form_class = forms.CultureTypeForm
    success_url = reverse_lazy('culture-types')


class EditPopularCultures(UpdateView):
    template_name = "tables/new/new-popular-cultures.html"
    model = models.PopularCulture
    form_class = forms.PopularCultureForm
    success_url = reverse_lazy('popular-cultures')


class EditEntertainment(UpdateView):
    template_name = "tables/new/new-entertainment.html"
    model = models.Entertainment
    form_class = forms.EntertainmentForm
    success_url = reverse_lazy('entertainment')


class EditMediaTypes(UpdateView):
    template_name = "tables/new/new-media-types.html"
    model = models.MediaType
    form_class = forms.MediaTypeForm
    success_url = reverse_lazy('media-types')


class EditMedia(UpdateView):
    template_name = "tables/new/new-media.html"
    model = models.Media
    form_class = forms.MediaForm
    success_url = reverse_lazy('media')


class EditObjects(UpdateView):
    template_name = "tables/new/new-objects.html"
    model = models.ObjectsMentioned
    form_class = forms.ObjectsMentionedForm
    success_url = reverse_lazy('objects')


class EditPsychology(UpdateView):
    template_name = "tables/new/new-psychology.html"
    model = models.Psychology
    form_class = forms.PsychologyForm
    success_url = reverse_lazy('psychology')


class EditSocialIssues(UpdateView):
    template_name = "tables/new/new-social-issues.html"
    model = models.SocialIssue
    form_class = forms.SocialIssueForm
    success_url = reverse_lazy('social-issues')


class EditSocialScience(UpdateView):
    template_name = "tables/new/new-social-science.html"
    model = models.SocialScience
    form_class = forms.SocialScienceForm
    success_url = reverse_lazy('social-science')


class EditConsumerismTypes(UpdateView):
    template_name = "tables/new/new-consumerism-types.html"
    model = models.ConsumerismType
    form_class = forms.ConsumerismTypeForm
    success_url = reverse_lazy('consumerism-types')


class EditConsumerism(UpdateView):
    template_name = "tables/new/new-consumerism.html"
    model = models.Consumerism
    form_class = forms.ConsumerismForm
    success_url = reverse_lazy('consumerism')


class EditArticles(UpdateView):
    template_name = "tables/new/new-articles.html"
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy('home')


class EditMedicalScience(UpdateView):
    template_name = "tables/new/new-medical-science.html"
    model = models.MedicalScience
    form_class = forms.MedicalScienceForm
    success_url = reverse_lazy('medical-science')


class EditTechnologies(UpdateView):
    template_name = "tables/new/new-technologies.html"
    model = models.Technology
    form_class = forms.TechnologyForm
    success_url = reverse_lazy('technologies')


# Delete Methods ######################################################################################################

class DeleteLocation(TemplateView):

    def get(self, request, id):
        models.Location.objects.filter(id=id).delete()
        return redirect(reverse('locations'))


class DeleteLocationTypes(TemplateView):

    def get(self, request, id):
        models.LocationType.objects.filter(id=id).delete()
        return redirect(reverse('location-types'))


class DeleteBuildings(TemplateView):

    def get(self, request, id):
        models.Building.objects.filter(id=id).delete()
        return redirect(reverse('buildings'))


class DeleteBuildingTypes(TemplateView):

    def get(self, request, id):
        models.BuildingType.objects.filter(id=id).delete()
        return redirect(reverse('building-types'))


class DeleteArts(TemplateView):

    def get(self, request, id):
        models.Art.objects.filter(id=id).delete()
        return redirect(reverse('arts'))


class DeleteArtTypes(TemplateView):

    def get(self, request, id):
        models.ArtType.objects.filter(id=id).delete()
        return redirect(reverse('art-types'))


class DeleteArtistTypes(TemplateView):

    def get(self, request, id):
        models.ArtistType.objects.filter(id=id).delete()
        return redirect(reverse('artist-types'))


class DeleteArtist(TemplateView):

    def get(self, request, id):
        models.Artist.objects.filter(id=id).delete()
        return redirect(reverse('artists'))


class DeleteArtStyles(TemplateView):

    def get(self, request, id):
        models.ArtStyle.objects.filter(id=id).delete()
        return redirect(reverse('art-styles'))


class DeleteArtisticMovements(TemplateView):

    def get(self, request, id):
        models.ArtisticMovement.objects.filter(id=id).delete()
        return redirect(reverse('artistic-movements'))


class DeleteAppliedArts(TemplateView):

    def get(self, request, id):
        models.AppliedArt.objects.filter(id=id).delete()
        return redirect(reverse('applied-arts'))


class DeleteFormatOfTexts(TemplateView):

    def get(self, request, id):
        models.FormatOfText.objects.filter(id=id).delete()
        return redirect(reverse('text-formats'))


class DeletePoliticsPeriod(TemplateView):

    def get(self, request, id):
        models.PoliticsPeriod.objects.filter(id=id).delete()
        return redirect(reverse('politics-periods'))


class DeletePolitics(TemplateView):

    def get(self, request, id):
        models.Politics.objects.filter(id=id).delete()
        return redirect(reverse('politics'))


class DeleteRelations(TemplateView):

    def get(self, request, id):
        models.Relation.objects.filter(id=id).delete()
        return redirect(reverse('relations'))


class DeleteBiographyPeriod(TemplateView):

    def get(self, request, id):
        models.Period.objects.filter(id=id).delete()
        return redirect(reverse('biography-periods'))


class DeleteBiographies(TemplateView):

    def get(self, request, id):
        models.Biography.objects.filter(id=id).delete()
        return redirect(reverse('biographies'))


class DeleteUrbanism(TemplateView):

    def get(self, request, id):
        models.Urbanism.objects.filter(id=id).delete()
        return redirect(reverse('urbanism'))


class DeleteArchitectures(TemplateView):

    def get(self, request, id):
        models.Architecture.objects.filter(id=id).delete()
        return redirect(reverse('architectures'))


class DeleteCulturalLife(TemplateView):

    def get(self, request, id):
        models.CulturalLife.objects.filter(id=id).delete()
        return redirect(reverse('cultural-life'))


class DeleteMovements(TemplateView):

    def get(self, request, id):
        models.Movement.objects.filter(id=id).delete()
        return redirect(reverse('movements'))


class DeleteWriters(TemplateView):

    def get(self, request, id):
        models.Writer.objects.filter(id=id).delete()
        return redirect(reverse('writers'))


class DeleteLiterature(TemplateView):

    def get(self, request, id):
        models.Literature.objects.filter(id=id).delete()
        return redirect(reverse('literature'))


class DeleteCultureTypes(TemplateView):

    def get(self, request, id):
        models.CultureType.objects.filter(id=id).delete()
        return redirect(reverse('culture-types'))


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


class DeleteObjects(TemplateView):

    def get(self, request, id):
        models.ObjectsMentioned.objects.filter(id=id).delete()
        return redirect(reverse('objects'))


class DeletePsychology(TemplateView):

    def get(self, request, id):
        models.Psychology.objects.filter(id=id).delete()
        return redirect(reverse('psychology'))


class DeleteSocialIssues(TemplateView):

    def get(self, request, id):
        models.SocialIssue.objects.filter(id=id).delete()
        return redirect(reverse('social-issues'))


class DeleteSocialScience(TemplateView):

    def get(self, request, id):
        models.SocialScience.objects.filter(id=id).delete()
        return redirect(reverse('social-science'))


class DeleteConsumerismTypes(TemplateView):

    def get(self, request, id):
        models.ConsumerismType.objects.filter(id=id).delete()
        return redirect(reverse('consumerism-types'))


class DeleteConsumerism(TemplateView):

    def get(self, request, id):
        models.Consumerism.objects.filter(id=id).delete()
        return redirect(reverse('consumerism'))


class DeleteArticles(TemplateView):

    def get(self, request, id):
        models.Article.objects.filter(id=id).delete()
        return redirect(reverse('home'))


class DeleteMedicalScience(TemplateView):

    def get(self, request, id):
        models.MedicalScience.objects.filter(id=id).delete()
        return redirect(reverse('medical-science'))


class DeleteTechnologies(TemplateView):

    def get(self, request, id):
        models.Technology.objects.filter(id=id).delete()
        return redirect(reverse('technologies'))
