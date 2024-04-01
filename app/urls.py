from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('appointment',views.appointment,name='appointment'),
    path('newsletter',views.newsletter,name='newsletter'),
]
