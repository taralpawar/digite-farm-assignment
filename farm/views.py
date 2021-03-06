from django.shortcuts import render, redirect
from .models import Farm
from datetime import datetime, timedelta
from crop.models import Crop
# Create your views here.


def myfarms(request):
    allfarms = Farm.objects.filter(owner=request.user)
    return render(request, 'farm/myfarm.html', {'allfarms': allfarms})


def addfarm(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        area = request.POST['area']
        owner = request.user

        newfarm = Farm(name=name, location=location, area=area, owner=owner)
        newfarm.save()

        return redirect('/farm/')

    else:
        return render(request, 'farm/addfarm.html')


def farmdetails(request, id):
    farm = Farm.objects.get(id=id)
    allcrops = Crop.objects.filter(farm=farm)
    return render(request, 'farm/details.html', {'farm': farm, 'allcrops': allcrops})


def addcrop(request, id):
    if request.method == 'POST':
        farm = Farm.objects.get(id=id)
        name = request.POST['name']
        season = request.POST['season']
        quantity = request.POST['quantity']
        plant_date = request.POST['plant_date']
        growth_time = int(request.POST['growth_time'])
        land_preparation = request.POST['land_preparation']
        irrigation_period = request.POST['irrigation_period']
        fertilizer_name = request.POST['fertilizer_name']
        fertilizer_quantity = request.POST['fertilizer_quantity']

        harvest_date = (
            (datetime.strptime(plant_date, '%Y-%m-%d') + timedelta(days=int(growth_time))))

        prepare_date = (
            (datetime.strptime(plant_date, '%Y-%m-%d') - timedelta(days=int(land_preparation))))

        newcrop = Crop(farm=farm, name=name, season=season, quantity=quantity, plant_date=plant_date, growth_time=growth_time,
                       land_preparation=land_preparation, irrigation_period=irrigation_period, fertilizer_name=fertilizer_name, fertilizer_quantity=fertilizer_quantity, harvest_date=harvest_date, prepare_date=prepare_date)

        newcrop.save()
        return redirect('/farm/farmdetails/{}/'.format(id))

    else:
        return render(request, 'farm/addcrop.html', {'id': id})


def deletecrop(request, id, cropid):
    crop = Crop.objects.get(id=cropid)
    crop.delete()
    return redirect('/farm/farmdetails/{}/'.format(id))


def updatecrop(request, id, cropid):
    if request.method == 'POST':
        crop = Crop.objects.get(id=cropid)
        crop.name = request.POST['name']
        crop.season = request.POST['season']
        crop.quantity = request.POST['quantity']
        crop.plant_date = request.POST['plant_date']
        crop.growth_time = int(request.POST['growth_time'])
        crop.land_preparation = request.POST['land_preparation']
        crop.irrigation_period = request.POST['irrigation_period']
        crop.fertilizer_name = request.POST['fertilizer_name']
        crop.fertilizer_quantity = request.POST['fertilizer_quantity']

        crop.harvest_date = (
            (datetime.strptime(crop.plant_date, '%Y-%m-%d') + timedelta(days=int(crop.growth_time))))

        crop.prepare_date = (
            (datetime.strptime(crop.plant_date, '%Y-%m-%d') - timedelta(days=int(crop.land_preparation))))

        crop.save()
        return redirect('/farm/farmdetails/{}/'.format(id))

    else:
        crop = Crop.objects.get(id=cropid)
        return render(request, 'farm/updatecrop.html', {'id': id, 'crop': crop})
