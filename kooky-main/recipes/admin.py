from django.contrib import admin
from .models import Category, Recipes, Review


admin.site.register(Category)
admin.site.register(Recipes)
admin.site.register(Review)
