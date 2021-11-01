from django.contrib import admin

from .models import NeighborHood, UserProfile, Business, Post

admin.site.register(NeighborHood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Post)

