from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *

def redirect_to_store_home(request):
    return redirect('/store/home/')

class HomeView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
