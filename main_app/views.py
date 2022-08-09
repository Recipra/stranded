from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Equipment

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def equipment_index(request):
  tools = Equipment.objects.filter(type='T')
  shelters = Equipment.objects.filter(type='S')
  outfits = Equipment.objects.filter(type='O')
  return render(request, 'equipment/index.html', { 'tools': tools, 'shelters': shelters, 'outfits': outfits })

def equipment_detail(request, equipment_id):
  equipment = Equipment.objects.get(id=equipment_id)
  return render(request, 'equipment/detail.html', { 'equipment': equipment })

class EquipmentCreate(CreateView):
  model = Equipment
  fields = '__all__'