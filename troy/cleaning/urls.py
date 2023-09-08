from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
]