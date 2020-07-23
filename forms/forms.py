from django import forms
from django.contrib.gis import forms as gis_forms
from django.core.exceptions import ObjectDoesNotExist
from forms import models
import datetime


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
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
    url = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    location = forms.ModelMultipleChoiceField(required=False, queryset=models.Location.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    building = forms.ModelMultipleChoiceField(required=False, queryset=models.Building.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    type_of_format = forms.ModelChoiceField(required=False, queryset=models.TypeOfFormat.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    format_of_text = forms.ModelChoiceField(required=False, queryset=models.FormatOfText.objects.filter(status='R'),
                                         widget=forms.Select(
                                             attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                         ))
    personal_memory = forms.ModelMultipleChoiceField(required=False, queryset=models.PersonalMemory.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    historical_memory = forms.ModelMultipleChoiceField(required=False, queryset=models.HistoricalMemory.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    politics = forms.ModelMultipleChoiceField(required=False, queryset=models.Politics.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    architecture = forms.ModelMultipleChoiceField(required=False, queryset=models.Architecture.objects.filter(status='R'),
                                                  widget=forms.SelectMultiple(
                                                      attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                  ))
    urbanism = forms.ModelMultipleChoiceField(required=False, queryset=models.Urbanism.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    art = forms.ModelMultipleChoiceField(required=False, queryset=models.Art.objects.filter(status='R'), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    cultural_life = forms.ModelMultipleChoiceField(required=False, queryset=models.CulturalLife.objects.filter(status='R'),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                   ))
    aesthetic = forms.ModelMultipleChoiceField(required=False, queryset=models.Aesthetic.objects.filter(status='R'),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                   ))
    literature = forms.ModelMultipleChoiceField(required=False, queryset=models.Literature.objects.filter(status='R'),
                                                widget=forms.SelectMultiple(
                                                    attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                ))
    popular_culture = forms.ModelMultipleChoiceField(required=False, queryset=models.PopularCulture.objects.filter(status='R'),
                                                     widget=forms.SelectMultiple(
                                                         attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                     ))
    entertainment = forms.ModelMultipleChoiceField(required=False, queryset=models.Entertainment.objects.filter(status='R'),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                   ))
    media = forms.ModelMultipleChoiceField(required=False, queryset=models.Media.objects.filter(status='R'),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    leisure = forms.ModelMultipleChoiceField(required=False, queryset=models.Leisure.objects.filter(status='R'),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    consumerism = forms.ModelMultipleChoiceField(required=False, queryset=models.Consumerism.objects.filter(status='R'),
                                                 widget=forms.SelectMultiple(
                                                     attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                 ))
    science = forms.ModelMultipleChoiceField(required=False, queryset=models.Science.objects.filter(status='R'),
                                                 widget=forms.SelectMultiple(
                                                     attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                 ))
    objects_mentioned = forms.ModelMultipleChoiceField(required=False, queryset=models.ObjectsMentioned.objects.filter(status='R'),
                                                       widget=forms.SelectMultiple(
                                                           attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                       ))

    class Meta:
        model = models.Article
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['format_of_text'].queryset = models.FormatOfText.objects.none()

        if 'type_of_format' in self.data:
            try:
                type_of_format_id = int(self.data.get('type_of_format'))
                self.fields['format_of_text'].queryset = models.FormatOfText.objects.filter(type_id=type_of_format_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.type_of_format:
            self.fields['format_of_text'].queryset = models.FormatOfText.objects.filter(type_id=self.instance.type_of_format.id)


class OccupationForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Occupation
        exclude = ['status']


class RelationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Relation
        exclude = ['status']


class PersonForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    occupation = forms.ModelMultipleChoiceField(required=False, queryset=models.Occupation.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    relation = forms.ModelMultipleChoiceField(required=False, queryset=models.Relation.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    birthday = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
    ))
    date_of_death = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
    ))
    fiction_character = forms.BooleanField(required=False)
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Person
        exclude = ['status']


class LocationTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.LocationType
        exclude = ['status']


class LocationForm(gis_forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.LocationType.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    coordinates = gis_forms.PointField(widget=gis_forms.OSMWidget(
        attrs={}
    ))
    old_madrid = forms.NullBooleanField(required=False, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=[(1, 'Yes'), (0, 'No'), (2, 'N/A')]
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Location
        exclude = ['status']


class BuildingTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.BuildingType
        exclude = ['status']


class BuildingForm(gis_forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.BuildingType.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    location = forms.ModelChoiceField(required=False, queryset=models.Location.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    coordinates = gis_forms.PointField(widget=gis_forms.OSMWidget(
        attrs={}
    ))
    old_madrid = forms.NullBooleanField(required=False, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=[(1, 'Yes'), (0, 'No'), (2, 'N/A')]
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Building
        exclude = ['status']


class TypeOfFormatForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.TypeOfFormat
        exclude = ['status']


class FormatOfTextForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(queryset=models.TypeOfFormat.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.FormatOfText
        exclude = ['status']


class PersonalMemoryForm(forms.ModelForm):
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.filter(status='R'),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    memory = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelMultipleChoiceField(required=False, queryset=models.Building.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    location = forms.ModelMultipleChoiceField(required=False, queryset=models.Location.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    start_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
    ))
    end_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.PersonalMemory
        exclude = ['status']


class HistoricalPeriodForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    start_year = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    end_year = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.HistoricalPeriod
        exclude = ['status']


class HistoricalMemoryForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=models.Person.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    period = forms.ModelChoiceField(required=False, queryset=models.HistoricalPeriod.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.HistoricalMemory
        exclude = ['status']


class PoliticsPeriodForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    start_year = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    end_year = forms.CharField(required=False, max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.PoliticsPeriod
        exclude = ['status']


class PoliticsForm(forms.ModelForm):
    period = forms.ModelChoiceField(queryset=models.PoliticsPeriod.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    person = forms.ModelChoiceField(required=False, queryset=models.Person.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    event = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    concepts = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Politics
        exclude = ['status']


class ArchitectureForm(forms.ModelForm):
    person = forms.ModelChoiceField(required=False, queryset=models.Person.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    style = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelChoiceField(required=False, queryset=models.Building.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Architecture
        exclude = ['status']

    # Filters the dropdown elements
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     try:
    #         occupation = models.Occupation.objects.get(type="Architect")
    #     except ObjectDoesNotExist:
    #         occupation = None
    #     if occupation:
    #         self.fields['person'].queryset = models.Person.objects.filter(occupation=occupation)
    #     else:
    #         self.fields['person'].queryset = models.Person.objects.none()


class UrbanismForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Urbanism
        exclude = ['status']


class ArtCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.ArtCategory
        exclude = ['status']


class ArtTypeForm(forms.ModelForm):
    type = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    category = forms.ModelChoiceField(queryset=models.ArtCategory.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.ArtType
        exclude = ['status']


class ArtStyleForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.ArtStyle
        exclude = ['status']


class ArtisticMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.ArtisticMovement
        exclude = ['status']


class ArtForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    category = forms.ModelChoiceField(required=False, queryset=models.ArtCategory.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.ArtType.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    image = forms.ImageField(required=False)
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.filter(status='R'),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    style = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtStyle.objects.filter(status='R'),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    movement = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtisticMovement.objects.filter(status='R'),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Art
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = models.ArtType.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['type'].queryset = models.ArtType.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['type'].queryset = models.ArtType.objects.filter(category_id=self.instance.category.id)


class CulturalLifeForm(forms.ModelForm):
    events = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    associations = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.CulturalLife
        exclude = ['status']


class AestheticMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.AestheticMovement
        exclude = ['status']


class AestheticForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.ModelChoiceField(required=False, queryset=models.AestheticMovement.objects.filter(status='R'),
                                      widget=forms.Select(
                                          attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                      ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Aesthetic
        exclude = ['status']


class LiteraryMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.LiteraryMovement
        exclude = ['status']


class LiteraryGenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.LiteraryGenre
        exclude = ['status']


class LiteratureForm(forms.ModelForm):
    work = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.ModelChoiceField(required=False, queryset=models.LiteraryMovement.objects.filter(status='R'),
                                      widget=forms.Select(
                                          attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                      ))
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.filter(status='R'),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    themes = forms.CharField(required=False, max_length=500, widget=forms.Textarea(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    genre = forms.ModelChoiceField(required=False, queryset=models.LiteraryGenre.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Literature
        exclude = ['status']
        widgets = {
            'person': forms.SelectMultiple(attrs={'class': 'col-sm-12 col-lg-12 form-control'})
        }

    # Filters the dropdown elements
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     try:
    #         occupation = models.Occupation.objects.get(type="Writer")
    #     except ObjectDoesNotExist:
    #         occupation = None
    #     if occupation:
    #         self.fields['person'].queryset = models.Person.objects.filter(occupation=occupation)
    #     else:
    #         self.fields['person'].queryset = models.Person.objects.none()


class PopularCultureForm(forms.ModelForm):
    event = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.filter(status='R'),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    religious_traditions = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    celebrity_culture = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    kitsch = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.PopularCulture
        exclude = ['status']


class EntertainmentForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Entertainment
        exclude = ['status']


class MediaTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.MediaType
        exclude = ['status']


class MediaForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelMultipleChoiceField(required=False, queryset=models.MediaType.objects.filter(status='R'),
                                          widget=forms.SelectMultiple(
                                              attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                          ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Media
        exclude = ['status']


class LeisureTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.LeisureType
        exclude = ['status']


class LeisureForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.LeisureType.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelChoiceField(required=False, queryset=models.Building.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Leisure
        exclude = ['status']


class FashionForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Fashion
        exclude = ['status']


class ConsumerismForm(forms.ModelForm):
    shop = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    fashion = forms.ModelChoiceField(required=False, queryset=models.Fashion.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    advertisement = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Consumerism
        exclude = ['status']


class TypeOfScienceForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.TypeOfScience
        exclude = ['status']


class ScienceForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=models.TypeOfScience.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.Science
        exclude = ['status']


class ObjectsMentionedForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    location = forms.ModelChoiceField(required=False, queryset=models.Location.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelChoiceField(required=False, queryset=models.Building.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    urbanism = forms.ModelChoiceField(required=False, queryset=models.Urbanism.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    leisure = forms.ModelChoiceField(required=False, queryset=models.Leisure.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    architecture = forms.ModelChoiceField(required=False, queryset=models.Architecture.objects.filter(status='R'),
                                          widget=forms.Select(
                                              attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                          ))
    personal_memory = forms.ModelChoiceField(required=False, queryset=models.PersonalMemory.objects.filter(status='R'),
                                             widget=forms.Select(
                                                 attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                             ))
    historical_memory = forms.ModelChoiceField(required=False, queryset=models.HistoricalMemory.objects.filter(status='R'),
                                               widget=forms.Select(
                                                   attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                               ))
    politics = forms.ModelChoiceField(required=False, queryset=models.Politics.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    science = forms.ModelChoiceField(required=False, queryset=models.Science.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    art = forms.ModelChoiceField(required=False, queryset=models.Art.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    cultural_life = forms.ModelChoiceField(required=False, queryset=models.CulturalLife.objects.filter(status='R'),
                                           widget=forms.Select(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    aesthetic = forms.ModelChoiceField(required=False, queryset=models.Aesthetic.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    literature = forms.ModelChoiceField(required=False, queryset=models.Literature.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    entertainment = forms.ModelChoiceField(required=False, queryset=models.Entertainment.objects.filter(status='R'),
                                           widget=forms.Select(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    media = forms.ModelChoiceField(required=False, queryset=models.Media.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    popular_culture = forms.ModelChoiceField(required=False, queryset=models.PopularCulture.objects.filter(status='R'),
                                             widget=forms.Select(
                                                 attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                             ))
    consumerism = forms.ModelChoiceField(required=False, queryset=models.Consumerism.objects.filter(status='R'), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    complete = forms.BooleanField(required=False)

    class Meta:
        model = models.ObjectsMentioned
        exclude = ['status']
