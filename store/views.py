from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class HomeView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
