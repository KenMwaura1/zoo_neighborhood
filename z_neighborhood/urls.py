from django.urls import include, path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('neighborhood', views.neighborhood, name='neighborhood'),
    path('neighborhood/<int:neighborhood_id>', views.neighborhood, name='neighborhood'),
    # path('neighborhood/<int:neighborhood_id>/new', views.new_business, name='new_business'),
    # path('neighborhood/<int:neighborhood_id>/<int:business_id>', views.business, name='business'),
    # path('neighborhood/<int:neighborhood_id>/<int:business_id>/edit', views.edit_business, name='edit_business'),
    # path('neighborhood/<int:neighborhood_id>/<int:business_id>/delete', views.delete_business,
    # name='delete_business'), path('neighborhood/<int:neighborhood_id>/<int:business_id>/new_review',
    # views.new_review, name='new_review'), path(
    # 'neighborhood/<int:neighborhood_id>/<int:business_id>/<int:review_id>', views.review, name='review'),
    # path('neighborhood/<int:neighborhood_id>/<int:business_id>/<int:review_id>/edit', views.edit_review,
    # name='edit_review'), path('neighborhood/<int:neighborhood_id>/<int:business_id>/<int:review_id>/delete',
    # views.delete_review, name='delete_review'),

    ]
