# Generated by Django 4.0.2 on 2022-02-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsApp', '0021_upcomingevent_delete_upcomingevents'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fav_sport',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
