# Generated by Django 2.2.5 on 2021-03-05 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('plant_date', models.DateField()),
                ('growth_time', models.IntegerField()),
                ('harvest_date', models.DateField()),
                ('land_preparation', models.IntegerField()),
                ('irrigation_period', models.IntegerField()),
                ('fertilizer', models.CharField(max_length=100)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.Farm')),
            ],
        ),
    ]