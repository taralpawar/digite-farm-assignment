# Generated by Django 2.2.5 on 2021-03-05 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='fertilizer',
        ),
        migrations.RemoveField(
            model_name='crop',
            name='harvest_date',
        ),
    ]