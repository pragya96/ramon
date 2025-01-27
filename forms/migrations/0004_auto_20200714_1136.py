# Generated by Django 3.0.7 on 2020-07-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200712_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entertainment',
            options={'verbose_name_plural': 'Entertainment'},
        ),
        migrations.AlterModelOptions(
            name='typeofformat',
            options={'verbose_name_plural': 'Types of Format'},
        ),
        migrations.RemoveField(
            model_name='personalmemory',
            name='fiction_character',
        ),
        migrations.AddField(
            model_name='person',
            name='fiction_character',
            field=models.BooleanField(default=False),
        ),
    ]
