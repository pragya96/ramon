"""ramon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from forms import views

urlpatterns = [
    url(r'^articles$', views.Articles.as_view(), name='articles'),
    url(r'^occupations$', views.Occupations.as_view(), name='occupations'),
    url(r'^relations$', views.Relations.as_view(), name='relations'),
    url(r'^people$', views.People.as_view(), name='people'),
    url(r'^location-types$', views.LocationTypes.as_view(), name='location-types'),
    url(r'^locations$', views.Locations.as_view(), name='locations'),
    url(r'^building-types$', views.BuildingTypes.as_view(), name='building-types'),
    url(r'^buildings$', views.Buildings.as_view(), name='buildings'),
    url(r'^types-of-format$', views.TypesOfFormat.as_view(), name='types-of-format'),
    url(r'^text-formats$', views.FormatOfTexts.as_view(), name='text-formats'),
    url(r'^personal-memories$', views.PersonalMemories.as_view(), name='personal-memories'),
    url(r'^historical-periods$', views.HistoricalPeriods.as_view(), name='historical-periods'),
    url(r'^historical-memories$', views.HistoricalMemories.as_view(), name='historical-memories'),
    url(r'^politics-periods$', views.PoliticsPeriods.as_view(), name='politics-periods'),
    url(r'^politics$', views.Politics.as_view(), name='politics'),
    url(r'^architectures$', views.Architectures.as_view(), name='architectures'),
    url(r'^urbanism$', views.Urbanism.as_view(), name='urbanism'),
    url(r'^art-categories$', views.ArtCategories.as_view(), name='art-categories'),
    url(r'^art-types$', views.ArtTypes.as_view(), name='art-types'),
    url(r'^art-styles$', views.ArtStyles.as_view(), name='art-styles'),
    url(r'^artistic-movements$', views.ArtisticMovements.as_view(), name='artistic-movements'),
    url(r'^arts$', views.Arts.as_view(), name='arts'),
    url(r'^cultural-lives$', views.CulturalLives.as_view(), name='cultural-lives'),
    url(r'^aesthetic-movements$', views.AestheticMovements.as_view(), name='aesthetic-movements'),
    url(r'^aesthetics$', views.Aesthetics.as_view(), name='aesthetics'),
    url(r'^literary-movements$', views.LiteraryMovements.as_view(), name='literary-movements'),
    url(r'^literary-genres$', views.LiteraryGenres.as_view(), name='literary-genres'),
    url(r'^literature$', views.Literature.as_view(), name='literature'),
    url(r'^popular-cultures$', views.PopularCultures.as_view(), name='popular-cultures'),
    url(r'^entertainment$', views.Entertainment.as_view(), name='entertainment'),
    url(r'^media-types$', views.MediaTypes.as_view(), name='media-types'),
    url(r'^media$', views.Media.as_view(), name='media'),
    url(r'^leisure-types$', views.LeisureTypes.as_view(), name='leisure-types'),
    url(r'^leisure$', views.Leisure.as_view(), name='leisure'),
    url(r'^fashion$', views.Fashion.as_view(), name='fashion'),
    url(r'^consumerism$', views.Consumerism.as_view(), name='consumerism'),
    url(r'^types-of-science$', views.TypesOfScience.as_view(), name='types-of-science'),
    url(r'^sciences$', views.Sciences.as_view(), name='sciences'),
    url(r'^objects$', views.Objects.as_view(), name='objects'),

    url(r'^new-articles/$', views.NewArticles.as_view(), name='new-articles'),
    url(r'^new-occupations/$', views.NewOccupations.as_view(), name='new-occupations'),
    url(r'^new-relations/$', views.NewRelations.as_view(), name='new-relations'),
    url(r'^new-people/$', views.NewPeople.as_view(), name='new-people'),
    url(r'^new-location-types/$', views.NewLocationType.as_view(), name='new-location-types'),
    url(r'^new-locations(?:/(?P<id>[0-9]+))?/$', views.NewLocations.as_view(), name='new-locations'),
    url(r'^new-building-types/$', views.NewBuildingType.as_view(), name='new-building-types'),
    url(r'^new-buildings(?:/(?P<id>[0-9]+))?/$', views.NewBuildings.as_view(), name='new-buildings'),
    url(r'^new-types-of-format/$', views.NewTypesOfFormat.as_view(), name='new-types-of-format'),
    url(r'^new-text-formats/$', views.NewFormatOfTexts.as_view(), name='new-text-formats'),
    url(r'^new-personal-memories/$', views.NewPersonalMemories.as_view(), name='new-personal-memories'),
    url(r'^new-historical-periods/$', views.NewHistoricalPeriods.as_view(), name='new-historical-periods'),
    url(r'^new-historical-memories/$', views.NewHistoricalMemories.as_view(), name='new-historical-memories'),
    url(r'^new-politics-periods/$', views.NewPoliticsPeriod.as_view(), name='new-politics-periods'),
    url(r'^new-politics/$', views.NewPolitics.as_view(), name='new-politics'),
    url(r'^new-architectures/$', views.NewArchitectures.as_view(), name='new-architectures'),
    url(r'^new-urbanism/$', views.NewUrbanism.as_view(), name='new-urbanism'),
    url(r'^new-art-categories/$', views.NewArtCategories.as_view(), name='new-art-categories'),
    url(r'^new-art-types/$', views.NewArtTypes.as_view(), name='new-art-types'),
    url(r'^new-art-styles/$', views.NewArtStyles.as_view(), name='new-art-styles'),
    url(r'^new-artistic-movements/$', views.NewArtisticMovements.as_view(), name='new-artistic-movements'),
    url(r'^new-arts/$', views.NewArts.as_view(), name='new-arts'),
    url(r'^new-cultural-lives/$', views.NewCulturalLives.as_view(), name='new-cultural-lives'),
    url(r'^new-aesthetic-movements/$', views.NewAestheticMovements.as_view(), name='new-aesthetic-movements'),
    url(r'^new-aesthetics/$', views.NewAesthetics.as_view(), name='new-aesthetics'),
    url(r'^new-literary-movements/$', views.NewLiteraryMovements.as_view(), name='new-literary-movements'),
    url(r'^new-literary-genres/$', views.NewLiteraryGenres.as_view(), name='new-literary-genres'),
    url(r'^new-literature/$', views.NewLiterature.as_view(), name='new-literature'),
    url(r'^new-popular-cultures/$', views.NewPopularCultures.as_view(), name='new-popular-cultures'),
    url(r'^new-entertainment/$', views.NewEntertainment.as_view(), name='new-entertainment'),
    url(r'^new-media-types/$', views.NewMediaTypes.as_view(), name='new-media-types'),
    url(r'^new-media/$', views.NewMedia.as_view(), name='new-media'),
    url(r'^new-leisure-types/$', views.NewLeisureTypes.as_view(), name='new-leisure-types'),
    url(r'^new-leisure/$', views.NewLeisure.as_view(), name='new-leisure'),
    url(r'^new-fashion/$', views.NewFashion.as_view(), name='new-fashion'),
    url(r'^new-consumerism/$', views.NewConsumerism.as_view(), name='new-consumerism'),
    url(r'^new-types-of-science/$', views.NewTypesOfScience.as_view(), name='new-types-of-science'),
    url(r'^new-sciences/$', views.NewSciences.as_view(), name='new-sciences'),
    url(r'^new-objects/$', views.NewObjects.as_view(), name='new-objects'),

    url(r'^(?P<pk>\d+)/edit-articles/$', views.EditArticles.as_view(), name='edit-articles'),
    url(r'^(?P<pk>\d+)/edit-occupations/$', views.EditOccupations.as_view(), name='edit-occupations'),
    url(r'^(?P<pk>\d+)/edit-relations/$', views.EditRelations.as_view(), name='edit-relations'),
    url(r'^(?P<pk>\d+)/edit-people/$', views.EditPeople.as_view(), name='edit-people'),
    url(r'^(?P<pk>\d+)/edit-location-types/$', views.EditLocationType.as_view(), name='edit-location-types'),
    url(r'^(?P<pk>\d+)/edit-building-types/$', views.EditBuildingType.as_view(), name='edit-building-types'),
    url(r'^(?P<pk>\d+)/edit-types-of-format/$', views.EditTypesOfFormat.as_view(), name='edit-types-of-format'),
    url(r'^(?P<pk>\d+)/edit-text-formats/$', views.EditFormatOfTexts.as_view(), name='edit-text-formats'),
    url(r'^(?P<pk>\d+)/edit-personal-memories/$', views.EditPersonalMemories.as_view(), name='edit-personal-memories'),
    url(r'^(?P<pk>\d+)/edit-historical-periods/$', views.EditHistoricalPeriods.as_view(),
        name='edit-historical-periods'),
    url(r'^(?P<pk>\d+)/edit-historical-memories/$', views.EditHistoricalMemories.as_view(),
        name='edit-historical-memories'),
    url(r'^(?P<pk>\d+)/edit-politics-periods/$', views.EditPoliticsPeriod.as_view(), name='edit-politics-periods'),
    url(r'^(?P<pk>\d+)/edit-politics/$', views.EditPolitics.as_view(), name='edit-politics'),
    url(r'^(?P<pk>\d+)/edit-architectures/$', views.EditArchitectures.as_view(), name='edit-architectures'),
    url(r'^(?P<pk>\d+)/edit-urbanism/$', views.EditUrbanism.as_view(), name='edit-urbanism'),
    url(r'^(?P<pk>\d+)/edit-art-categories/$', views.EditArtCategories.as_view(), name='edit-art-categories'),
    url(r'^(?P<pk>\d+)/edit-art-types/$', views.EditArtTypes.as_view(), name='edit-art-types'),
    url(r'^(?P<pk>\d+)/edit-art-styles/$', views.EditArtStyles.as_view(), name='edit-art-styles'),
    url(r'^(?P<pk>\d+)/edit-artistic-movements/$', views.EditArtisticMovements.as_view(),
        name='edit-artistic-movements'),
    url(r'^(?P<pk>\d+)/edit-arts/$', views.EditArts.as_view(), name='edit-arts'),
    url(r'^(?P<pk>\d+)/edit-cultural-lives/$', views.EditCulturalLives.as_view(), name='edit-cultural-lives'),
    url(r'^(?P<pk>\d+)/edit-aesthetic-movements/$', views.EditAestheticMovements.as_view(),
        name='edit-aesthetic-movements'),
    url(r'^(?P<pk>\d+)/edit-aesthetics/$', views.EditAesthetics.as_view(), name='edit-aesthetics'),
    url(r'^(?P<pk>\d+)/edit-literary-movements/$', views.EditLiteraryMovements.as_view(),
        name='edit-literary-movements'),
    url(r'^(?P<pk>\d+)/edit-literary-genres/$', views.EditLiteraryGenres.as_view(), name='edit-literary-genres'),
    url(r'^(?P<pk>\d+)/edit-literature/$', views.EditLiterature.as_view(), name='edit-literature'),
    url(r'^(?P<pk>\d+)/edit-popular-cultures/$', views.EditPopularCultures.as_view(), name='edit-popular-cultures'),
    url(r'^(?P<pk>\d+)/edit-entertainment/$', views.EditEntertainment.as_view(), name='edit-entertainment'),
    url(r'^(?P<pk>\d+)/edit-media-types/$', views.EditMediaTypes.as_view(), name='edit-media-types'),
    url(r'^(?P<pk>\d+)/edit-media/$', views.EditMedia.as_view(), name='edit-media'),
    url(r'^(?P<pk>\d+)/edit-leisure-types/$', views.EditLeisureTypes.as_view(), name='edit-leisure-types'),
    url(r'^(?P<pk>\d+)/edit-leisure/$', views.EditLeisure.as_view(), name='edit-leisure'),
    url(r'^(?P<pk>\d+)/edit-fashion/$', views.EditFashion.as_view(), name='edit-fashion'),
    url(r'^(?P<pk>\d+)/edit-consumerism/$', views.EditConsumerism.as_view(), name='edit-consumerism'),
    url(r'^(?P<pk>\d+)/edit-types-of-science/$', views.EditTypesOfScience.as_view(), name='edit-types-of-science'),
    url(r'^(?P<pk>\d+)/edit-sciences/$', views.EditSciences.as_view(), name='edit-sciences'),
    url(r'^(?P<pk>\d+)/edit-objects/$', views.EditObjects.as_view(), name='edit-objects'),

    url(r'^delete-articles/(?P<id>[0-9]+)$', views.DeleteArticles.as_view(), name='delete-articles'),
    url(r'^delete-occupations/(?P<id>[0-9]+)$', views.DeleteOccupations.as_view(), name='delete-occupations'),
    url(r'^delete-relations/(?P<id>[0-9]+)$', views.DeleteRelations.as_view(), name='delete-relations'),
    url(r'^delete-people/(?P<id>[0-9]+)$', views.DeletePeople.as_view(), name='delete-people'),
    url(r'^delete-location-types/(?P<id>[0-9]+)$', views.DeleteLocationTypes.as_view(), name='delete-location-types'),
    url(r'^delete-locations/(?P<id>[0-9]+)$', views.DeleteLocation.as_view(), name='delete-locations'),
    url(r'^delete-building-types/(?P<id>[0-9]+)$', views.DeleteBuildingTypes.as_view(), name='delete-building-types'),
    url(r'^delete-buildings/(?P<id>[0-9]+)$', views.DeleteBuildings.as_view(), name='delete-buildings'),
    url(r'^delete-types-of-format/(?P<id>[0-9]+)$', views.DeleteTypesOfFormat.as_view(), name='delete-types-of-format'),
    url(r'^delete-text-formats/(?P<id>[0-9]+)$', views.DeleteFormatOfTexts.as_view(), name='delete-text-formats'),
    url(r'^delete-personal-memories/(?P<id>[0-9]+)$', views.DeletePersonalMemories.as_view(),
        name='delete-personal-memories'),
    url(r'^delete-historical-periods/(?P<id>[0-9]+)$', views.DeleteHistoricalPeriods.as_view(),
        name='delete-historical-periods'),
    url(r'^delete-historical-memories/(?P<id>[0-9]+)$', views.DeleteHistoricalMemories.as_view(),
        name='delete-historical-memories'),
    url(r'^delete-politics-periods/(?P<id>[0-9]+)$', views.DeletePoliticsPeriod.as_view(),
        name='delete-politics-periods'),
    url(r'^delete-politics/(?P<id>[0-9]+)$', views.DeletePolitics.as_view(), name='delete-politics'),
    url(r'^delete-architectures/(?P<id>[0-9]+)$', views.DeleteArchitectures.as_view(), name='delete-architectures'),
    url(r'^delete-urbanism/(?P<id>[0-9]+)$', views.DeleteUrbanism.as_view(), name='delete-urbanism'),
    url(r'^delete-art-categories/(?P<id>[0-9]+)$', views.DeleteArtCategories.as_view(), name='delete-art-categories'),
    url(r'^delete-art-types/(?P<id>[0-9]+)$', views.DeleteArtTypes.as_view(), name='delete-art-types'),
    url(r'^delete-art-styles/(?P<id>[0-9]+)$', views.DeleteArtStyles.as_view(), name='delete-art-styles'),
    url(r'^delete-artistic-movements/(?P<id>[0-9]+)$', views.DeleteArtisticMovements.as_view(),
        name='delete-artistic-movements'),
    url(r'^delete-arts/(?P<id>[0-9]+)$', views.DeleteArts.as_view(), name='delete-arts'),
    url(r'^delete-cultural-lives/(?P<id>[0-9]+)$', views.DeleteCulturalLives.as_view(), name='delete-cultural-lives'),
    url(r'^delete-aesthetic-movements/(?P<id>[0-9]+)$', views.DeleteAestheticMovements.as_view(),
        name='delete-aesthetic-movements'),
    url(r'^delete-aesthetics/(?P<id>[0-9]+)$', views.DeleteAesthetics.as_view(), name='delete-aesthetics'),
    url(r'^delete-literary-movements/(?P<id>[0-9]+)$', views.DeleteLiteraryMovements.as_view(),
        name='delete-literary-movements'),
    url(r'^delete-literary-genres/(?P<id>[0-9]+)$', views.DeleteLiteraryGenres.as_view(),
        name='delete-literary-genres'),
    url(r'^delete-literature/(?P<id>[0-9]+)$', views.DeleteLiterature.as_view(), name='delete-literature'),
    url(r'^delete-popular-cultures/(?P<id>[0-9]+)$', views.DeletePopularCultures.as_view(),
        name='delete-popular-cultures'),
    url(r'^delete-entertainment/(?P<id>[0-9]+)$', views.DeleteEntertainment.as_view(), name='delete-entertainment'),
    url(r'^delete-media-types/(?P<id>[0-9]+)$', views.DeleteMediaTypes.as_view(), name='delete-media-types'),
    url(r'^delete-media/(?P<id>[0-9]+)$', views.DeleteMedia.as_view(), name='delete-media'),
    url(r'^delete-leisure-types/(?P<id>[0-9]+)$', views.DeleteLeisureTypes.as_view(), name='delete-leisure-types'),
    url(r'^delete-leisure/(?P<id>[0-9]+)$', views.DeleteLeisure.as_view(), name='delete-leisure'),
    url(r'^delete-fashion/(?P<id>[0-9]+)$', views.DeleteFashion.as_view(), name='delete-fashion'),
    url(r'^delete-consumerism/(?P<id>[0-9]+)$', views.DeleteConsumerism.as_view(), name='delete-consumerism'),
    url(r'^delete-types-of-science/(?P<id>[0-9]+)$', views.DeleteTypesOfScience.as_view(),
        name='delete-types-of-science'),
    url(r'^delete-sciences/(?P<id>[0-9]+)$', views.DeleteSciences.as_view(), name='delete-sciences'),
    url(r'^delete-objects/(?P<id>[0-9]+)$', views.DeleteObjects.as_view(), name='delete-objects'),

    url(r'ajax/load-art-types/$', views.load_art_types, name='ajax-load-art-types'),
    url(r'ajax/load-text-format/$', views.load_text_format, name='ajax-load-text-format'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
