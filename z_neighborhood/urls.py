from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('neighborhood', views.neighborhood, name='neighborhood'),
    path('neighborhood/<int:hood_id>', views.hood_details, name='hood_details'),
    path('search/', views.search_business, name='search'),
    path('add-hood', views.add_hood, name='add-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
    path('neighborhood/<int:neighborhood_id>/members', views.hood_members, name='members'),
    path('neighborhood/<int:neighborhood_id>/business', views.hood_business, name='business'),

    ]
