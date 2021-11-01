from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .forms import RegisterForm
from .models import NeighborHood


@login_required(login_url='/login/')
def home(request):
    return render(request, 'z_neighborhood/home.html')


def neighborhood(request):
    all_neighborhoods = NeighborHood.get_all_neighborhoods()
    return render(request, 'z_neighborhood/neighborhood.html', {'all_neighborhoods': all_neighborhoods})



def profile(request):
    return None
