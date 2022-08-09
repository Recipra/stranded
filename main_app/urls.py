from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('equipment/', views.equipment_index, name='equipment_index'),
  path('equipment/<int:equipment_id>', views.equipment_detail, name='equipment_detail'),
  path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create')
]
