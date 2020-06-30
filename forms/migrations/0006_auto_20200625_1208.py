# Generated by Django 3.0.7 on 2020-06-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20200624_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.ArtistType'),
        ),
    ]