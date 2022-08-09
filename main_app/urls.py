from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # path('equipment/', views.equipment_index, name='equipment_index')
]
