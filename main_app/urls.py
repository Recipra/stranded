from django.urls import path
from . import views

urlpatterns = [
  path('accounts/signup', views.signup, name='signup'),
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('equipment/', views.equipment_index, name='equipment_index'),
  path('equipment/<int:equipment_id>', views.equipment_detail, name='equipment_detail'),
  path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
  path('equipment/<int:pk>/recycle/', views.EquipmentRecycle.as_view(), name='equipment_recycle'),
  path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
  path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete')
]
