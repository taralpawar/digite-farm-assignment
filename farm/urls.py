from django.urls import path, include
from .views import myfarms, addfarm, farmdetails, addcrop, deletecrop, updatecrop

app_name = 'farm'

urlpatterns = [
    path('', myfarms, name='myfarms'),
    path('addfarm/', addfarm, name="addfarm"),
    path('farmdetails/<int:id>/', farmdetails, name="farmdetails"),
    path('farmdetails/<int:id>/addcrop/', addcrop, name="addcrop"),
    path('farmdetails/<int:id>/deletecrop/<int:cropid>/',
         deletecrop, name="deletecrop"),
    path('farmdetails/<int:id>/updatecrop/<int:cropid>/',
         updatecrop, name="updatecrop"),
]
