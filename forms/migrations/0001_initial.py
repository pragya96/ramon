# Generated by Django 3.0.7 on 2020-07-12 14:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aesthetic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='AestheticMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Architecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ArtCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Art Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('newspaper', models.CharField(max_length=100, null=True)),
                ('issue', models.IntegerField(null=True)),
                ('page_numbers', models.CharField(max_length=50, null=True)),
                ('url', models.URLField(null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ArtisticMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ArtStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('old_madrid', models.BooleanField(null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Consumerism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=100, null=True)),
                ('advertisement', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
            options={
                'verbose_name_plural': 'Consumerism',
            },
        ),
        migrations.CreateModel(
            name='CulturalLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.CharField(max_length=100, null=True)),
                ('associations', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
            options={
                'verbose_name_plural': 'Cultural Lives',
            },
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Fashion',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
            options={
                'verbose_name_plural': 'Historical Memories',
            },
        ),
        migrations.CreateModel(
            name='HistoricalPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Leisure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Building')),
            ],
            options={
                'verbose_name_plural': 'Leisure',
            },
        ),
        migrations.CreateModel(
            name='LeisureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='LiteraryGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='LiteraryMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=100)),
                ('themes', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.LiteraryGenre')),
                ('movement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.LiteraryMovement')),
            ],
            options={
                'verbose_name_plural': 'Literature',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coordinates', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('old_madrid', models.BooleanField(null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(null=True)),
                ('date_of_death', models.DateField(null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('occupation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Occupation')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='PoliticsPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('years', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfScience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Types of Science',
            },
        ),
        migrations.CreateModel(
            name='Urbanism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
            ],
            options={
                'verbose_name_plural': 'Urbanism',
            },
        ),
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.TypeOfScience')),
            ],
        ),
        migrations.CreateModel(
            name='PopularCulture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100, null=True)),
                ('religious_traditions', models.CharField(max_length=100, null=True)),
                ('celebrity_culture', models.CharField(max_length=100, null=True)),
                ('kitsch', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('person', models.ManyToManyField(to='forms.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100, null=True)),
                ('movement', models.CharField(max_length=100, null=True)),
                ('concepts', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.PoliticsPeriod')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Person')),
            ],
            options={
                'verbose_name_plural': 'Politics',
            },
        ),
        migrations.CreateModel(
            name='PersonalMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.CharField(max_length=500)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('fiction_character', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('building', models.ManyToManyField(to='forms.Building')),
                ('location', models.ManyToManyField(to='forms.Location')),
                ('person', models.ManyToManyField(to='forms.Person')),
            ],
            options={
                'verbose_name_plural': 'Personal Memories',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='relation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Relation'),
        ),
        migrations.CreateModel(
            name='ObjectsMentioned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='I', max_length=2)),
                ('aesthetic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Aesthetic')),
                ('architecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Architecture')),
                ('art', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Art')),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Building')),
                ('consumerism', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Consumerism')),
                ('cultural_life', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.CulturalLife')),
                ('entertainment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Entertainment')),
                ('historical_memory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.HistoricalMemory')),
                ('leisure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Leisure')),
                ('literature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Literature')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Location')),
                ('media', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Media')),
                ('personal_memory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.PersonalMemory')),
                ('politics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Politics')),
                ('popular_culture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.PopularCulture')),
                ('science', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Science')),
                ('urbanism', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Urbanism')),
            ],
            options={
                'verbose_name': 'Object',
                'verbose_name_plural': 'Objects',
            },
        ),
        migrations.AddField(
            model_name='media',
            name='type',
            field=models.ManyToManyField(to='forms.MediaType'),
        ),
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.LocationType'),
        ),
        migrations.AddField(
            model_name='literature',
            name='person',
            field=models.ManyToManyField(to='forms.Person'),
        ),
        migrations.AddField(
            model_name='leisure',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.LeisureType'),
        ),
        migrations.AddField(
            model_name='historicalmemory',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.HistoricalPeriod'),
        ),
        migrations.AddField(
            model_name='historicalmemory',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Person'),
        ),
        migrations.CreateModel(
            name='FormatOfText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
                ('article', models.ManyToManyField(to='forms.Article')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.TypeOfFormat')),
            ],
        ),
        migrations.AddField(
            model_name='consumerism',
            name='fashion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Fashion'),
        ),
        migrations.AddField(
            model_name='building',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Location'),
        ),
        migrations.AddField(
            model_name='building',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.BuildingType'),
        ),
        migrations.CreateModel(
            name='ArtType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('I', 'Incomplete'), ('RR', 'Ready for Review'), ('R', 'Reviewed')], default='RR', max_length=2)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.ArtCategory')),
            ],
        ),
        migrations.AddField(
            model_name='art',
            name='article',
            field=models.ManyToManyField(to='forms.Article'),
        ),
        migrations.AddField(
            model_name='art',
            name='movement',
            field=models.ManyToManyField(to='forms.ArtisticMovement'),
        ),
        migrations.AddField(
            model_name='art',
            name='person',
            field=models.ManyToManyField(to='forms.Person'),
        ),
        migrations.AddField(
            model_name='art',
            name='style',
            field=models.ManyToManyField(to='forms.ArtStyle'),
        ),
        migrations.AddField(
            model_name='art',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.ArtType'),
        ),
        migrations.AddField(
            model_name='architecture',
            name='article',
            field=models.ManyToManyField(to='forms.Article'),
        ),
        migrations.AddField(
            model_name='architecture',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Building'),
        ),
        migrations.AddField(
            model_name='architecture',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Person'),
        ),
        migrations.AddField(
            model_name='aesthetic',
            name='article',
            field=models.ManyToManyField(to='forms.Article'),
        ),
        migrations.AddField(
            model_name='aesthetic',
            name='movement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.AestheticMovement'),
        ),
    ]
