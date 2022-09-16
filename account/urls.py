#Will map and connect with telusko URL for calc app

from django.urls import path 
from . import views     #(. = all, in this case, calc)


urlpatterns = [
    path('register', views.register ,  name = 'register'),  #homepage, can write '/' too
    path('', views.log_in, name = 'log_in'),
    path('log_in', views.log_in, name = 'log_in'),
    path('log_out', views.log_out, name = 'log_out'),
    path('reset_password', views.reset_password, name = 'reset_password'),
    path('reset_password_sent', views.reset_password_sent, name = 'reset_password_sent'),
    path('password_reset_form', views.password_reset_form, name = 'password_reset_form'),

   
]