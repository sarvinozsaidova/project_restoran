from django.urls import path
from .views import *

urlpatterns = [
    path('', wine, name='index'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('service/', service, name='service'),
    path('booking/', booking, name='booking'),   
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
    # path('team/', team, name='team'),
]