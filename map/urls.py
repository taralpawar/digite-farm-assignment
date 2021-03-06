from django.urls import path, include
from .views import showMap

urlpatterns = [
    path('', showMap),
]
