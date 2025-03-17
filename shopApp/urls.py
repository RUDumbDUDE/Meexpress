from django.urls import path
from shopApp.views import index, about, active_contacts

urlpatterns = [
    path('',index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', active_contacts, name='active_contacts'),
]