from django.contrib.gis.db import models as gis_models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

STATUS_CHOICES = [
    ('I', 'Incomplete'),
    ('RR', 'Ready for Review'),
    ('R', 'Reviewed')
]


# Create your models here.


class Occupation(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type


class Relation(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.ManyToManyField(Occupation)
    relation = models.ManyToManyField(Relation)
    birthday = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    fiction_character = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People"


class LocationType(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type


class Location(gis_models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(LocationType, on_delete=models.CASCADE, null=True)
    geom = gis_models.GeometryField(blank=True, null=True)
    old_madrid = models.BooleanField(null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.name


class BuildingType(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type


class Building(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    geom = gis_models.PointField(null=True)
    old_madrid = models.BooleanField(null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.name


class TypeOfFormat(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Types of Format"


class FormatOfText(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.ForeignKey(TypeOfFormat, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        if self.name:
            return self.name


class PersonalMemory(models.Model):
    person = models.ManyToManyField(Person)
    memory = models.CharField(max_length=500)
    building = models.ManyToManyField(Building)
    location = models.ManyToManyField(Location)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.memory

    class Meta:
        verbose_name_plural = "Personal Memories"


class HistoricalPeriod(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=50, null=True)
    end_year = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class HistoricalMemory(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    period = models.ForeignKey(HistoricalPeriod, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    class Meta:
        verbose_name_plural = "Historical Memories"

    def __str__(self):
        return self.person.name


class PoliticsPeriod(models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=50, null=True)
    end_year = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class Politics(models.Model):
    period = models.ForeignKey(PoliticsPeriod, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    event = models.CharField(max_length=100, null=True)
    movement = models.CharField(max_length=100, null=True)
    concepts = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    class Meta:
        verbose_name_plural = "Politics"

    def __str__(self):
        return self.period.name


class Architecture(models.Model):
    style = models.CharField(max_length=100, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        if self.style:
            return self.person.name + " (" + self.style + ")"
        else:
            return self.person.name


class Urbanism(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Urbanism"


class ArtCategory(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Art Categories"


class ArtType(models.Model):
    type = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        if self.type:
            return self.type
        else:
            return self.category.name


class ArtStyle(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type


class ArtisticMovement(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class Art(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(ArtType, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    person = models.ManyToManyField(Person)
    style = models.ManyToManyField(ArtStyle)
    movement = models.ManyToManyField(ArtisticMovement)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.title


class CulturalLife(models.Model):
    events = models.CharField(max_length=100)
    associations = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    class Meta:
        verbose_name_plural = "Cultural Lives"

    def __str__(self):
        return self.events


class AestheticMovement(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class Aesthetic(models.Model):
    name = models.CharField(max_length=100)
    movement = models.ForeignKey(AestheticMovement, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class LiteraryMovement(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class LiteraryGenre(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.name


class Literature(models.Model):
    work = models.CharField(max_length=100)
    movement = models.ForeignKey(LiteraryMovement, on_delete=models.CASCADE, null=True)
    person = models.ManyToManyField(Person)
    themes = models.CharField(max_length=500, null=True)
    genre = models.ForeignKey(LiteraryGenre, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.work

    class Meta:
        verbose_name_plural = "Literature"


class PopularCulture(models.Model):
    event = models.CharField(max_length=100)
    person = models.ManyToManyField(Person)
    religious_traditions = models.CharField(max_length=100, null=True)
    celebrity_culture = models.CharField(max_length=100, null=True)
    kitsch = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.event


class Entertainment(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Entertainment"


class MediaType(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type


class Media(models.Model):
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(MediaType)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    class Meta:
        verbose_name_plural = "Media"

    def __str__(self):
        return self.name


class LeisureType(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type


class Leisure(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(LeisureType, on_delete=models.CASCADE, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Leisure"


class Fashion(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Fashion"


class Consumerism(models.Model):
    shop = models.CharField(max_length=100)
    fashion = models.ForeignKey(Fashion, on_delete=models.CASCADE, null=True)
    advertisement = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')

    class Meta:
        verbose_name_plural = "Consumerism"

    def __str__(self):
        return self.shop


class TypeOfScience(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Types of Science"


class Science(models.Model):
    type = models.ForeignKey(TypeOfScience, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RR')

    def __str__(self):
        if self.name:
            return self.name + " (" + self.type.type + ")"
        else:
            return self.type.type


class ObjectsMentioned(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')
    location = models.ManyToManyField(Location)
    building = models.ManyToManyField(Building)
    urbanism = models.ManyToManyField(Urbanism)
    leisure = models.ManyToManyField(Leisure)
    architecture = models.ManyToManyField(Architecture)
    personal_memory = models.ManyToManyField(PersonalMemory)
    historical_memory = models.ManyToManyField(HistoricalMemory)
    politics = models.ManyToManyField(Politics)
    science = models.ManyToManyField(Science)
    art = models.ManyToManyField(Art)
    cultural_life = models.ManyToManyField(CulturalLife)
    aesthetic = models.ManyToManyField(Aesthetic)
    literature = models.ManyToManyField(Literature)
    entertainment = models.ManyToManyField(Entertainment)
    media = models.ManyToManyField(Media)
    popular_culture = models.ManyToManyField(PopularCulture)
    consumerism = models.ManyToManyField(Consumerism)

    class Meta:
        verbose_name = "Object"
        verbose_name_plural = "Objects"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(null=True)
    place_of_publication = models.CharField(max_length=100, null=True)
    newspaper = models.CharField(max_length=100, null=True)
    issue = models.IntegerField(null=True)
    page_numbers = models.CharField(max_length=50, null=True)
    url = models.URLField(null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')
    person = models.ManyToManyField(Person)
    location = models.ManyToManyField(Location)
    building = models.ManyToManyField(Building)
    type_of_format = models.ForeignKey(TypeOfFormat, on_delete=models.CASCADE, null=True)
    format_of_text = models.ForeignKey(FormatOfText, on_delete=models.CASCADE, null=True)
    personal_memory = models.ManyToManyField(PersonalMemory)
    historical_memory = models.ManyToManyField(HistoricalMemory)
    politics = models.ManyToManyField(Politics)
    architecture = models.ManyToManyField(Architecture)
    urbanism = models.ManyToManyField(Urbanism)
    art = models.ManyToManyField(Art)
    cultural_life = models.ManyToManyField(CulturalLife)
    aesthetic = models.ManyToManyField(Aesthetic)
    literature = models.ManyToManyField(Literature)
    popular_culture = models.ManyToManyField(PopularCulture)
    entertainment = models.ManyToManyField(Entertainment)
    media = models.ManyToManyField(Media)
    leisure = models.ManyToManyField(Leisure)
    consumerism = models.ManyToManyField(Consumerism)
    science = models.ManyToManyField(Science)
    objects_mentioned = models.ManyToManyField(ObjectsMentioned)

    def __str__(self):
        return self.title
