from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, NeighborHoodForm, BusinessForm, PostForm, UpdateProfileForm
from .models import NeighborHood, Business, Post, UserProfile


@login_required(login_url='/login/')
def home(request):
    return render(request, 'z_neighborhood/home.html')


def neighborhood(request):
    all_neighborhoods = NeighborHood.get_all_neighborhoods()
    print(all_neighborhoods)
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
    business = Business.get_business_by_neighbourhood(hood)
    posts = Post.get_posts_by_neighbourhood(hood)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz_form = form.save(commit=False)
            biz_form.neighborhood = hood
            biz_form.user = request.user.userprofile
            biz_form.save()
            return redirect('home')
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'posts': posts,
        'form': form
    }
    return render(request, 'z_neighborhood/hood_details.html', params)


def hood_members(request, neighborhood_id):
    hood = NeighborHood.objects.get(id=neighborhood_id)
    print(hood)
    members = UserProfile.objects.filter(neighbourhood=hood)
    return render(request, 'z_neighborhood/hood_members.html', {'members': members})


def create_post(request, hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.userprofile
            post.save()
            return redirect('single-hood', hood.id)
    else:
        form = PostForm()
    params = {
        'form': form,
        'hood': hood
    }
    return render(request, 'z_neighborhood/create_post.html', params)


def profile(request, username):
    return render(request, 'z_neighborhood/profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.userprofile)
    return render(request, 'z_neighborhood/edit_profile.html', {'form': form})


def search_business(request):
    return None


def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighborHood, id=id)
    request.user.userprofile.neighbourhood = neighbourhood
    request.user.userprofile.save()
    return redirect('neighborhood')


def leave_hood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.userprofile.neighbourhood = None
    request.user.userprofile.save()
    return redirect('neighborhood')
