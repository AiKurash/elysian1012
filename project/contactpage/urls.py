from django.urls import path
from django.contrib import admin
from contactpage import views
from contactpage.views import contactView, successView


app_name = 'contactpage'

urlpatterns = [

    path('contactpage/contact/' ,views.contactView, name='contactView'),
    path('contactpage/contact/success/',views.successView, name='successView'),

]
