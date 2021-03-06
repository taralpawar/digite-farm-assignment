from django.urls import path, include
from .views import register, loginuser, homepg, logoutuser

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),

    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('home/', homepg, name='home')
]
