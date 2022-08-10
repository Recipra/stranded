from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Equipment

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def equipment_index(request):
  tools = Equipment.objects.filter(type='T', user=request.user)
  shelters = Equipment.objects.filter(type='S', user=request.user)
  outfits = Equipment.objects.filter(type='O', user=request.user)
  return render(request, 'equipment/index.html', { 'tools': tools, 'shelters': shelters, 'outfits': outfits })

@login_required
def equipment_detail(request, equipment_id):
  equipment = Equipment.objects.get(id=equipment_id)
  return render(request, 'equipment/detail.html', { 'equipment': equipment })

class EquipmentCreate(LoginRequiredMixin, CreateView):
  model = Equipment
  fields = ['name', 'type', 'description', 'durability', 'rating']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EquipmentRecycle(LoginRequiredMixin, UpdateView):
  model = Equipment
  fields = ['name', 'type', 'description', 'durability', 'rating']

class EquipmentUpdate(LoginRequiredMixin, UpdateView):
  model = Equipment
  fields = ['description', 'durability', 'rating']

class EquipmentDelete(LoginRequiredMixin, DeleteView):
  model = Equipment
  success_url = '/equipment/'