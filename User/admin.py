from django.contrib import admin
from .models import User,Post
from Products.models import Products

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Products)

