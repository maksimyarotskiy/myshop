from django.http import request
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

class ProductSearchView(ListView):
    template_name = 'store/home.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Фильтрация продуктов поиском
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
