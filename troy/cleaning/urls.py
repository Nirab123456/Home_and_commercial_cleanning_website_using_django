from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('contact/save/',views.contact_save,name='contact_save'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('appointment/',views.appointment,name='appointment'),
    path('appointment/save/',views.appointment_save,name='appointment_save'),
    path('developer/',views.developer,name='developer'),
    path('developer/save/',views.developer_save,name='developer_save'),

]