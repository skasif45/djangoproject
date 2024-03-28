from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('yash/', hello1),
    path('yash1/',hello2, name = 'hello2'),
    path('',newhomepage, name = 'newhomepage'),
    path('yash3/',travelpackage, name = 'travelpackage'),
    path('yash5/',print1,name = 'print1'),
    path('yash4/', print_to_console, name='print_to_console'),
    path('ran/',random123, name='random123'),
    path('yash6/',getdate1, name='getdate1'),
    path('yash7/',get_date, name = 'get_date'),
    path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    path('Register/',pagecall,name='pagecall'),
    path('yash8/',registerloginfunction,name='registerloginfunction'),
    path('yash9/',pie_chart, name= 'pie_chart'),
    path('yash10/',destinations, name= 'destinations'),
    path('yash11/',weather, name= 'weather'),
    path('yash12/',weatherlogic, name= 'weatherlogic'),
    path('yash13/',login,name='login'),
    path('yash14/',signup,name='signup'),
    path('yash15/',login1,name='login1'),
    path('yash16/',signup1,name='signup1'),
    path('yash17/',logout,name='logout'),
    path('yash18/',feedback,name='feedback'),
    path('yash19/',contactmail,name='contactmail'),
]






