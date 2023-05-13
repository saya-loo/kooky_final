from django import forms
from .models import Recipes
from django.views.generic import DetailView


class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ["image"]


class EmpImageDisplay(DetailView):
    model = Recipes
    context_object_name = 'recipe'
