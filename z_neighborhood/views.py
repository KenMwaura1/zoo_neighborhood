from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, NeighborHoodForm, BusinessForm, PostForm, UpdateProfileForm
from .models import NeighborHood, Business, Post, UserProfile


@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'z_neighborhood/home.html')


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def add_hood(request):
    if request.method == "POST":
        form = NeighborHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.userprofile
            hood.save()
            return redirect('home')
    else:
        form = NeighborHoodForm()
    return render(request, 'z_neighborhood/add_hood.html', {'form': form})


@login_required(login_url='/accounts/login/')
def hood_details(request, hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz_form = form.save(commit=False)
            biz_form.neighbourhood = hood
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


@login_required(login_url='/accounts/login/')
def create_post(request, hood_id):
    hood = NeighborHood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.userprofile
            post.save()
            return redirect('hood_details', hood.id)
    else:
        form = PostForm()
    params = {
        'form': form,
        'hood': hood
    }
    return render(request, 'z_neighborhood/create_post.html', params)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    return render(request, 'z_neighborhood/profile.html')


@login_required(login_url='/accounts/login/')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.userprofile)
    return render(request, 'z_neighborhood/edit_profile.html', {'form': form})


def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"
        params = {
            'message': message,
            'businesses': searched_business
        }
        return render(request, 'z_neighborhood/search.html', params)
    else:
        message = "You haven't searched for any term"
        return render(request, 'z_neighborhood/search.html', {'message': message})


@login_required(login_url='/accounts/login/')
def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighborHood, id=id)
    request.user.userprofile.neighbourhood = neighbourhood
    request.user.userprofile.save()
    return redirect('neighborhood')


@login_required(login_url='/accounts/login/')
def leave_hood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.userprofile.neighbourhood = None
    request.user.userprofile.save()
    return redirect('neighborhood')


@login_required(login_url='/accounts/login/')
def hood_business(request, neighborhood_id):
    businesses = Business.objects.filter(neighbourhood=neighborhood_id)
    return render(request, 'z_neighborhood/hood_business.html', {'businesses': businesses})
