from django.shortcuts import render
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