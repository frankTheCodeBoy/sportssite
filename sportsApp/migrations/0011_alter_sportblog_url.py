# Generated by Django 4.0.2 on 2022-02-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0010_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportblog',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
