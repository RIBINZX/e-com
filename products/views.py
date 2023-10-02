from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categories, Subcategories, Product

class SubcategoriesList(ListView):
    model = Subcategories
    template_name = 'products/subcategories.html'

class CatogoriesList(ListView):
    model = Categories
    template_name = 'products/categories.html'

class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'