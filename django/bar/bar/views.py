from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.


class ListProductView(ListView):
    template_name = "product_list.html"
    model = Product


class DetailListProductView(DetailView):
    template_name = "product_detail.html"
    model = Product
