from django import forms
from django.contrib.gis import forms as gis_forms
from forms import models


class LocationTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.LocationType
        fields = '__all__'


class LocationForm(gis_forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.LocationType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    coordinates = gis_forms.PointField(widget=gis_forms.OSMWidget(
        attrs={}
    ))
    old_madrid = forms.NullBooleanField(required=False, widget=forms.RadioSelect(
        attrs={'class': 'radio'},
        choices=[(1, 'Yes'), (0, 'No'), (2, 'N/A')]
    ))

    class Meta:
        model = models.Location
        fields = '__all__'


class BuildingTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.BuildingType
        fields = '__all__'


class BuildingForm(gis_forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.BuildingType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    location = forms.ModelChoiceField(required=False, queryset=models.Location.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    coordinates = gis_forms.PointField(widget=gis_forms.OSMWidget(
        attrs={}
    ))
    old_madrid = forms.NullBooleanField(required=False, widget=forms.RadioSelect(
        attrs={'class': 'radio'},
        choices=[(1, 'Yes'), (0, 'No'), (2, 'N/A')]
    ))

    class Meta:
        model = models.Building
        fields = '__all__'


class ArtTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ArtType
        fields = '__all__'


class ArtistTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ArtistType
        fields = '__all__'


class ArtistForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.ArtistType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Artist
        fields = '__all__'


class ArtStyleForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ArtStyle
        fields = '__all__'


class ArtisticMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ArtisticMovement
        fields = '__all__'


class ArtForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtType.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    # image = forms.ImageField(required=False)
    artist = forms.ModelMultipleChoiceField(required=False, queryset=models.Artist.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    style = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtStyle.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtisticMovement.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    aesthetic = forms.CharField(required=False, max_length=500, widget=forms.Textarea(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Art
        fields = '__all__'


class AppliedArtForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.AppliedArt
        fields = '__all__'


class FormatOfTextForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.FormatOfText
        fields = '__all__'


class PoliticsPeriodForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.PoliticsPeriod
        fields = '__all__'


class PoliticsForm(forms.ModelForm):
    figure = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    period = forms.ModelChoiceField(required=False, queryset=models.PoliticsPeriod.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Politics
        fields = '__all__'


class RelationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Relation
        fields = '__all__'


class PeriodForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Period
        fields = '__all__'


class BiographyForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    relation = forms.ModelChoiceField(required=False, queryset=models.Relation.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    period = forms.ModelChoiceField(required=False, queryset=models.Period.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Biography
        fields = '__all__'


class UrbanismForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Urbanism
        fields = '__all__'


class ArchitectureForm(forms.ModelForm):
    architect = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    style = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Architecture
        fields = '__all__'


class CulturalLifeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.CulturalLife
        fields = '__all__'


class MovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Movement
        fields = '__all__'


class WriterForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Writer
        fields = '__all__'


class LiteratureForm(forms.ModelForm):
    work = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.ModelChoiceField(required=False, queryset=models.Movement.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    writer = forms.ModelMultipleChoiceField(required=False, queryset=models.Writer.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    themes = forms.CharField(required=False, max_length=500, widget=forms.Textarea(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Literature
        fields = '__all__'


class CultureTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.CultureType
        fields = '__all__'


class PopularCultureForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=models.CultureType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    description = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.PopularCulture
        fields = '__all__'


class EntertainmentForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Entertainment
        fields = '__all__'


class MediaTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.MediaType
        fields = '__all__'


class MediaForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelMultipleChoiceField(required=False, queryset=models.MediaType.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Media
        fields = '__all__'


class ObjectsMentionedForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ObjectsMentioned
        fields = '__all__'


class PsychologyForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Psychology
        fields = '__all__'


class SocialIssueForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.SocialIssue
        fields = '__all__'


class SocialScienceForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.SocialScience
        fields = '__all__'


class ConsumerismTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ConsumerismType
        fields = '__all__'


class ConsumerismForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.ConsumerismType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Consumerism
        fields = '__all__'


class MedicalScienceForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.MedicalScience
        fields = '__all__'


class TechnologyForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.Technology
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    newspaper = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    issue = forms.IntegerField(required=False, widget=forms.NumberInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    page_numbers = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    location = forms.ModelMultipleChoiceField(required=False, queryset=models.Location.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelMultipleChoiceField(required=False, queryset=models.Building.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    url = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    art = forms.ModelMultipleChoiceField(required=False, queryset=models.Art.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    applied_art = forms.ModelMultipleChoiceField(required=False, queryset=models.AppliedArt.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    text_format = forms.ModelChoiceField(required=False, queryset=models.FormatOfText.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    politics = forms.ModelMultipleChoiceField(required=False, queryset=models.Politics.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    biography = forms.ModelMultipleChoiceField(required=False, queryset=models.Biography.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    urbanism = forms.ModelMultipleChoiceField(required=False, queryset=models.Urbanism.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    architecture = forms.ModelMultipleChoiceField(required=False, queryset=models.Architecture.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    cultural_life = forms.ModelMultipleChoiceField(required=False, queryset=models.CulturalLife.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    literature = forms.ModelMultipleChoiceField(required=False, queryset=models.Literature.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    popular_culture = forms.ModelMultipleChoiceField(required=False, queryset=models.PopularCulture.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    entertainment = forms.ModelMultipleChoiceField(required=False, queryset=models.Entertainment.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    media = forms.ModelMultipleChoiceField(required=False, queryset=models.Media.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    modernity = forms.CharField(required=False, max_length=200, widget=forms.Textarea(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    objects_mentioned = forms.ModelMultipleChoiceField(required=False, queryset=models.ObjectsMentioned.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    psychology = forms.ModelMultipleChoiceField(required=False, queryset=models.Psychology.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    social_issue = forms.ModelMultipleChoiceField(required=False, queryset=models.SocialIssue.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    social_science = forms.ModelMultipleChoiceField(required=False, queryset=models.SocialScience.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    consumerism = forms.ModelMultipleChoiceField(required=False, queryset=models.Consumerism.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.Article.STATUS_CHOICES
    ))

    class Meta:
        model = models.Article
        fields = '__all__'
