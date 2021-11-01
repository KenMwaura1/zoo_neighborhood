from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .forms import RegisterForm, NeighborHoodForm
from .models import NeighborHood


@login_required(login_url='/login/')
def home(request):
    return render(request, 'z_neighborhood/home.html')


def neighborhood(request):
    all_neighborhoods = NeighborHood.get_all_neighborhoods()
    return render(request, 'z_neighborhood/neighborhood.html', {'all_neighborhoods': all_neighborhoods})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})

def add_hood(request):
    if request.method == "POST":
        form = NeighborHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.userprofile
            hood.save()
            return redirect('home')
    else:
        form = NeighborHoodForm()
    return render(request, 'z_neighborhood/add_hood.html', {'form': form})


def hood_details(request, hood_id):
    hood = NeighborHood.find_neighborhood(hood_id)
    return render(request, 'z_neighborhood/hood_details.html', {'hood': hood})

def profile(request):
    return None


def search_business(request):
    return None