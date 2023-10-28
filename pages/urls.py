from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.landingpage, name = 'Langing Page'),
    path('home/', v.home, name='HomePage'),
    path('about/', v.About, name="About"),

]
