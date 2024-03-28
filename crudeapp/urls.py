from . import views
from django.urls import path

urlpatterns = [
    path('', views.insert_emp, name='insert_emp'),
    path('show/', views.show_emp, name='show_emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit_emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove_emp'),
]
