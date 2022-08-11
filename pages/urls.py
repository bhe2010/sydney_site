from django.urls import path
from . import views

urlpatterns = [
    #request is sent to the index function in the views.py file
    #path('', views.index, name='index'),
    
    path('', views.index, {'pagename':''}, name = 'home'),

    #Order matters!!!
    path('contact', views.contact, name = 'contact'),

    #first part captures everything behind default and sends as pagename
    #for example: Parameter: pagename = 'About me'

    path('<str:pagename>', views.index, name='index'),

]