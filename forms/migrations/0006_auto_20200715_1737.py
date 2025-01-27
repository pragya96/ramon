# Generated by Django 3.0.7 on 2020-07-15 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_art_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aesthetic',
            name='article',
        ),
        migrations.RemoveField(
            model_name='architecture',
            name='article',
        ),
        migrations.RemoveField(
            model_name='art',
            name='article',
        ),
        migrations.RemoveField(
            model_name='building',
            name='article',
        ),
        migrations.RemoveField(
            model_name='consumerism',
            name='article',
        ),
        migrations.RemoveField(
            model_name='culturallife',
            name='article',
        ),
        migrations.RemoveField(
            model_name='entertainment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='formatoftext',
            name='article',
        ),
        migrations.RemoveField(
            model_name='historicalmemory',
            name='article',
        ),
        migrations.RemoveField(
            model_name='leisure',
            name='article',
        ),
        migrations.RemoveField(
            model_name='literature',
            name='article',
        ),
        migrations.RemoveField(
            model_name='location',
            name='article',
        ),
        migrations.RemoveField(
            model_name='media',
            name='article',
        ),
        migrations.RemoveField(
            model_name='objectsmentioned',
            name='article',
        ),
        migrations.RemoveField(
            model_name='person',
            name='article',
        ),
        migrations.RemoveField(
            model_name='personalmemory',
            name='article',
        ),
        migrations.RemoveField(
            model_name='politics',
            name='article',
        ),
        migrations.RemoveField(
            model_name='popularculture',
            name='article',
        ),
        migrations.RemoveField(
            model_name='science',
            name='article',
        ),
        migrations.RemoveField(
            model_name='urbanism',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='aesthetic',
            field=models.ManyToManyField(to='forms.Aesthetic'),
        ),
        migrations.AddField(
            model_name='article',
            name='architecture',
            field=models.ManyToManyField(to='forms.Architecture'),
        ),
        migrations.AddField(
            model_name='article',
            name='art',
            field=models.ManyToManyField(to='forms.Art'),
        ),
        migrations.AddField(
            model_name='article',
            name='building',
            field=models.ManyToManyField(to='forms.Building'),
        ),
        migrations.AddField(
            model_name='article',
            name='consumerism',
            field=models.ManyToManyField(to='forms.Consumerism'),
        ),
        migrations.AddField(
            model_name='article',
            name='cultural_life',
            field=models.ManyToManyField(to='forms.CulturalLife'),
        ),
        migrations.AddField(
            model_name='article',
            name='entertainment',
            field=models.ManyToManyField(to='forms.Entertainment'),
        ),
        migrations.AddField(
            model_name='article',
            name='format_of_text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.FormatOfText'),
        ),
        migrations.AddField(
            model_name='article',
            name='historical_memory',
            field=models.ManyToManyField(to='forms.HistoricalMemory'),
        ),
        migrations.AddField(
            model_name='article',
            name='leisure',
            field=models.ManyToManyField(to='forms.Leisure'),
        ),
        migrations.AddField(
            model_name='article',
            name='literature',
            field=models.ManyToManyField(to='forms.Literature'),
        ),
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.ManyToManyField(to='forms.Location'),
        ),
        migrations.AddField(
            model_name='article',
            name='media',
            field=models.ManyToManyField(to='forms.Media'),
        ),
        migrations.AddField(
            model_name='article',
            name='objects_mentioned',
            field=models.ManyToManyField(to='forms.ObjectsMentioned'),
        ),
        migrations.AddField(
            model_name='article',
            name='person',
            field=models.ManyToManyField(to='forms.Person'),
        ),
        migrations.AddField(
            model_name='article',
            name='personal_memory',
            field=models.ManyToManyField(to='forms.PersonalMemory'),
        ),
        migrations.AddField(
            model_name='article',
            name='politics',
            field=models.ManyToManyField(to='forms.Politics'),
        ),
        migrations.AddField(
            model_name='article',
            name='popular_culture',
            field=models.ManyToManyField(to='forms.PopularCulture'),
        ),
        migrations.AddField(
            model_name='article',
            name='science',
            field=models.ManyToManyField(to='forms.Science'),
        ),
        migrations.AddField(
            model_name='article',
            name='urbanism',
            field=models.ManyToManyField(to='forms.Urbanism'),
        ),
    ]
