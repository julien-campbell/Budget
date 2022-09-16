#Will map and connect with telusko URL for calc app

from django.urls import path 
from . import views     #(. = all, in this case, calc)

urlpatterns = [
    path('', views.index, name = 'index'),  #homepage, can write '/' too
    path('addmoney', views.addmoney, name = 'addmoney'),
    path('info', views.info, name = 'info'),
    path('profile', views.profile, name = 'profile'),
    path('weekly', views.weekly, name = 'weekly'),
    path('stats', views.stats, name = 'stats'),
    path('charts', views.charts, name = 'charts'),
    path('tables', views.tables, name = 'tables'),
    
    
]