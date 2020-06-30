from django.contrib.gis.db import models as gis_models
from django.db import models


# Create your models here.
class LocationType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Location(gis_models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(LocationType, on_delete=models.CASCADE, null=True)
    coordinates = gis_models.GeometryField(blank=True, null=True)
    old_madrid = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class BuildingType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Building(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    coordinates = gis_models.PointField(null=True)
    old_madrid = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class ArtType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class ArtistType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Artist(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ArtistType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + " (" + self.type.type + ")"


class ArtStyle(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class ArtisticMovement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Art(models.Model):
    title = models.CharField(max_length=100, null=True)
    type = models.ManyToManyField(ArtType)
    image = models.ImageField(upload_to='images/', null=True)
    artist = models.ManyToManyField(Artist)
    style = models.ManyToManyField(ArtStyle)
    movement = models.ManyToManyField(ArtisticMovement)
    aesthetic = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.title


class AppliedArt(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class FormatOfText(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class PoliticsPeriod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Politics(models.Model):
    period = models.ForeignKey(PoliticsPeriod, on_delete=models.CASCADE, null=True)
    figure = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Politics"

    def __str__(self):
        return self.figure


class Relation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Period(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Biography(models.Model):
    name = models.CharField(max_length=100, null=True)
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Biographies"

    def __str__(self):
        return self.name


class Urbanism(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Architecture(models.Model):
    architect = models.CharField(max_length=100, null=True)
    style = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.architect + " (" + self.style + ")"


class CulturalLife(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Cultural Lives"

    def __str__(self):
        return self.type


class Movement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Literature(models.Model):
    work = models.CharField(max_length=200, null=True)
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, null=True)
    writer = models.ManyToManyField(Writer)
    themes = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.work

    class Meta:
        verbose_name_plural = "Literature"


class CultureType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class PopularCulture(models.Model):
    type = models.ForeignKey(CultureType, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.type.type


class Entertainment(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class MediaType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Media(models.Model):
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(MediaType)

    class Meta:
        verbose_name_plural = "Media"

    def __str__(self):
        return self.name


class ObjectsMentioned(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Object"
        verbose_name_plural = "Objects"

    def __str__(self):
        return self.name


class Psychology(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Psychologies"

    def __str__(self):
        return self.name


class SocialIssue(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SocialScience(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ConsumerismType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Consumerism(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ConsumerismType, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Consumerism"

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = [
        ('I', 'Incomplete'),
        ('RR', 'Ready for Review'),
        ('R', 'Reviewed')
    ]
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='I')
    date = models.DateField(null=True)
    newspaper = models.CharField(max_length=100, null=True)
    issue = models.IntegerField(null=True)
    page_numbers = models.CharField(max_length=50, null=True)
    location = models.ManyToManyField(Location)
    building = models.ManyToManyField(Building)
    url = models.URLField(null=True)
    art = models.ManyToManyField(Art)
    applied_art = models.ManyToManyField(AppliedArt)
    text_format = models.ForeignKey(FormatOfText, on_delete=models.CASCADE, null=True)
    politics = models.ManyToManyField(Politics)
    biography = models.ManyToManyField(Biography)
    urbanism = models.ManyToManyField(Urbanism)
    architecture = models.ManyToManyField(Architecture)
    cultural_life = models.ManyToManyField(CulturalLife)
    literature = models.ManyToManyField(Literature)
    popular_culture = models.ManyToManyField(PopularCulture)
    entertainment = models.ManyToManyField(Entertainment)
    media = models.ManyToManyField(Media)
    modernity = models.CharField(max_length=200, null=True)
    objects_mentioned = models.ManyToManyField(ObjectsMentioned)
    psychology = models.ManyToManyField(Psychology)
    social_issue = models.ManyToManyField(SocialIssue)
    social_science = models.ManyToManyField(SocialScience)
    consumerism = models.ManyToManyField(Consumerism)

    def __str__(self):
        return self.title

