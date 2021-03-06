from django.shortcuts import render

# Create your views here.


def showMap(request):
    return render(request, 'map/map.html')
