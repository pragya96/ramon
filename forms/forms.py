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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    location = forms.ModelMultipleChoiceField(required=False, queryset=models.Location.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    building = forms.ModelMultipleChoiceField(required=False, queryset=models.Building.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    type_of_format = forms.ModelChoiceField(required=False, queryset=models.TypeOfFormat.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    format_of_text = forms.ModelChoiceField(required=False, queryset=models.FormatOfText.objects.all(),
                                         widget=forms.Select(
                                             attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                         ))
    personal_memory = forms.ModelMultipleChoiceField(required=False, queryset=models.PersonalMemory.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    historical_memory = forms.ModelMultipleChoiceField(required=False, queryset=models.HistoricalMemory.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    politics = forms.ModelMultipleChoiceField(required=False, queryset=models.Politics.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    architecture = forms.ModelMultipleChoiceField(required=False, queryset=models.Architecture.objects.all(),
                                                  widget=forms.SelectMultiple(
                                                      attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                  ))
    urbanism = forms.ModelMultipleChoiceField(required=False, queryset=models.Urbanism.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    art = forms.ModelMultipleChoiceField(required=False, queryset=models.Art.objects.all(), widget=forms.SelectMultiple(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    cultural_life = forms.ModelMultipleChoiceField(required=False, queryset=models.CulturalLife.objects.all(),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                   ))
    aesthetic = forms.ModelMultipleChoiceField(required=False, queryset=models.Aesthetic.objects.all(),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                   ))
    literature = forms.ModelMultipleChoiceField(required=False, queryset=models.Literature.objects.all(),
                                                widget=forms.SelectMultiple(
                                                    attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                ))
    popular_culture = forms.ModelMultipleChoiceField(required=False, queryset=models.PopularCulture.objects.all(),
                                                     widget=forms.SelectMultiple(
                                                         attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                     ))
    entertainment = forms.ModelMultipleChoiceField(required=False, queryset=models.Entertainment.objects.all(),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                   ))
    media = forms.ModelMultipleChoiceField(required=False, queryset=models.Media.objects.all(),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    leisure = forms.ModelMultipleChoiceField(required=False, queryset=models.Leisure.objects.all(),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    consumerism = forms.ModelMultipleChoiceField(required=False, queryset=models.Consumerism.objects.all(),
                                                 widget=forms.SelectMultiple(
                                                     attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                 ))
    science = forms.ModelMultipleChoiceField(required=False, queryset=models.Science.objects.all(),
                                                 widget=forms.SelectMultiple(
                                                     attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                 ))
    objects_mentioned = forms.ModelMultipleChoiceField(required=False, queryset=models.ObjectsMentioned.objects.all(),
                                                       widget=forms.SelectMultiple(
                                                           attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                                       ))

    class Meta:
        model = models.Article
        fields = '__all__'

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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Occupation
        fields = '__all__'


class RelationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Relation
        fields = '__all__'


class PersonForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    occupation = forms.ModelMultipleChoiceField(required=False, queryset=models.Occupation.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    relation = forms.ModelMultipleChoiceField(required=False, queryset=models.Relation.objects.all(),
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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Person
        fields = '__all__'


class LocationTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
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
    old_madrid = forms.NullBooleanField(required=False, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=[(1, 'Yes'), (0, 'No'), (2, 'N/A')]
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Location
        fields = '__all__'


class BuildingTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
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
    old_madrid = forms.NullBooleanField(required=False, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=[(1, 'Yes'), (0, 'No'), (2, 'N/A')]
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Building
        fields = '__all__'


class TypeOfFormatForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.TypeOfFormat
        fields = '__all__'


class FormatOfTextForm(forms.ModelForm):
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(queryset=models.TypeOfFormat.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.FormatOfText
        fields = '__all__'


class PersonalMemoryForm(forms.ModelForm):
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.all(),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    memory = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelMultipleChoiceField(required=False, queryset=models.Building.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    location = forms.ModelMultipleChoiceField(required=False, queryset=models.Location.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    start_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
    ))
    end_date = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control datepicker'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.PersonalMemory
        fields = '__all__'


class HistoricalPeriodForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    start_year = forms.IntegerField(required=False, min_value=1800, max_value=datetime.datetime.now().year, widget=forms.NumberInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    end_year = forms.IntegerField(required=False, min_value=1800, max_value=datetime.datetime.now().year, widget=forms.NumberInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.HistoricalPeriod
        fields = '__all__'


class HistoricalMemoryForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=models.Person.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    period = forms.ModelChoiceField(required=False, queryset=models.HistoricalPeriod.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.HistoricalMemory
        fields = '__all__'


class PoliticsPeriodForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    start_year = forms.IntegerField(required=False, min_value=1800, max_value=datetime.datetime.now().year, widget=forms.NumberInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    end_year = forms.IntegerField(required=False, min_value=1800, max_value=datetime.datetime.now().year, widget=forms.NumberInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.PoliticsPeriod
        fields = '__all__'


class PoliticsForm(forms.ModelForm):
    period = forms.ModelChoiceField(queryset=models.PoliticsPeriod.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    person = forms.ModelChoiceField(required=False, queryset=models.Person.objects.all(), widget=forms.Select(
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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Politics
        fields = '__all__'


class ArchitectureForm(forms.ModelForm):
    person = forms.ModelChoiceField(required=False, queryset=models.Person.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    style = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelChoiceField(required=False, queryset=models.Building.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Architecture
        fields = '__all__'

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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Urbanism
        fields = '__all__'


class ArtCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.ArtCategory
        fields = '__all__'


class ArtTypeForm(forms.ModelForm):
    type = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    category = forms.ModelChoiceField(queryset=models.ArtCategory.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.ArtType
        fields = '__all__'


class ArtStyleForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.ArtStyle
        fields = '__all__'


class ArtisticMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.ArtisticMovement
        fields = '__all__'


class ArtForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    category = forms.ModelChoiceField(required=False, queryset=models.ArtCategory.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.ArtType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    image = forms.ImageField(required=False)
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.all(),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    style = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtStyle.objects.all(),
                                           widget=forms.SelectMultiple(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    movement = forms.ModelMultipleChoiceField(required=False, queryset=models.ArtisticMovement.objects.all(),
                                              widget=forms.SelectMultiple(
                                                  attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                              ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Art
        fields = '__all__'

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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.CulturalLife
        fields = '__all__'


class AestheticMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.AestheticMovement
        fields = '__all__'


class AestheticForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.ModelChoiceField(required=False, queryset=models.AestheticMovement.objects.all(),
                                      widget=forms.Select(
                                          attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                      ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Aesthetic
        fields = '__all__'


class LiteraryMovementForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.LiteraryMovement
        fields = '__all__'


class LiteraryGenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.LiteraryGenre
        fields = '__all__'


class LiteratureForm(forms.ModelForm):
    work = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    movement = forms.ModelChoiceField(required=False, queryset=models.LiteraryMovement.objects.all(),
                                      widget=forms.Select(
                                          attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                      ))
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.all(),
                                            widget=forms.SelectMultiple(
                                                attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                            ))
    themes = forms.CharField(required=False, max_length=500, widget=forms.Textarea(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    genre = forms.ModelChoiceField(required=False, queryset=models.LiteraryGenre.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Literature
        fields = '__all__'
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
    person = forms.ModelMultipleChoiceField(required=False, queryset=models.Person.objects.all(),
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
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.PopularCulture
        fields = '__all__'


class EntertainmentForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Entertainment
        fields = '__all__'


class MediaTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.MediaType
        fields = '__all__'


class MediaForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelMultipleChoiceField(required=False, queryset=models.MediaType.objects.all(),
                                          widget=forms.SelectMultiple(
                                              attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                          ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Media
        fields = '__all__'


class LeisureTypeForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.LeisureType
        fields = '__all__'


class LeisureForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    type = forms.ModelChoiceField(required=False, queryset=models.LeisureType.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelChoiceField(required=False, queryset=models.Building.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Leisure
        fields = '__all__'


class FashionForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Fashion
        fields = '__all__'


class ConsumerismForm(forms.ModelForm):
    shop = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    fashion = forms.ModelChoiceField(required=False, queryset=models.Fashion.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    advertisement = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Consumerism
        fields = '__all__'


class TypeOfScienceForm(forms.ModelForm):
    type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.TypeOfScience
        fields = '__all__'


class ScienceForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=models.TypeOfScience.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))

    class Meta:
        model = models.Science
        fields = '__all__'


class ObjectsMentionedForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    status = forms.CharField(max_length=2, widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'},
        choices=models.STATUS_CHOICES
    ))
    location = forms.ModelChoiceField(required=False, queryset=models.Location.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    building = forms.ModelChoiceField(required=False, queryset=models.Building.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    urbanism = forms.ModelChoiceField(required=False, queryset=models.Urbanism.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    leisure = forms.ModelChoiceField(required=False, queryset=models.Leisure.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    architecture = forms.ModelChoiceField(required=False, queryset=models.Architecture.objects.all(),
                                          widget=forms.Select(
                                              attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                          ))
    personal_memory = forms.ModelChoiceField(required=False, queryset=models.PersonalMemory.objects.all(),
                                             widget=forms.Select(
                                                 attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                             ))
    historical_memory = forms.ModelChoiceField(required=False, queryset=models.HistoricalMemory.objects.all(),
                                               widget=forms.Select(
                                                   attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                               ))
    politics = forms.ModelChoiceField(required=False, queryset=models.Politics.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    science = forms.ModelChoiceField(required=False, queryset=models.Science.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    art = forms.ModelChoiceField(required=False, queryset=models.Art.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    cultural_life = forms.ModelChoiceField(required=False, queryset=models.CulturalLife.objects.all(),
                                           widget=forms.Select(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    aesthetic = forms.ModelChoiceField(required=False, queryset=models.Aesthetic.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    literature = forms.ModelChoiceField(required=False, queryset=models.Literature.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    entertainment = forms.ModelChoiceField(required=False, queryset=models.Entertainment.objects.all(),
                                           widget=forms.Select(
                                               attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                           ))
    media = forms.ModelChoiceField(required=False, queryset=models.Media.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))
    popular_culture = forms.ModelChoiceField(required=False, queryset=models.PopularCulture.objects.all(),
                                             widget=forms.Select(
                                                 attrs={'class': 'col-sm-12 col-lg-12 form-control'}
                                             ))
    consumerism = forms.ModelChoiceField(required=False, queryset=models.Consumerism.objects.all(), widget=forms.Select(
        attrs={'class': 'col-sm-12 col-lg-12 form-control'}
    ))

    class Meta:
        model = models.ObjectsMentioned
        fields = '__all__'
