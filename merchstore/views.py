from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Product, ProductType, Transaction


class ProductListView(ListView):
    model = Product
    template_name = "merchstore/product_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_types"] = ProductType.objects.all()
        return context
    


class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore/product_detail.html"


class ProductCreateView(CreateView):
    model = Product
    template_name = "merchstore/product_create.html"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "merchstore/product_update.html"


class CartView(ListView):
    model = Transaction
    template_name = "merchstore/cart.html"

class TransactionListView(ListView):
    model = Transaction
    template_name = "merchstore/transaction_list.html"