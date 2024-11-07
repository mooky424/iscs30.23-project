from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from user_management.models import Profile

from .forms import ProductForm, TransactionForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TransactionForm()

        # set max amount of products to be equal to remaining stock
        form.fields["amount"].widget.attrs["max"] = context["product"].stock

        context["form"] = form
        return context

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        product = self.get_object()
        if form.is_valid():
            if request.user.is_authenticated:
                transaction = Transaction()
                transaction.product = product
                transaction.amount = form.cleaned_data["amount"]
                transaction.buyer = request.user.profile
                transaction.save()
                product.stock -= form.cleaned_data["amount"]
                return redirect("merchstore:cart")
            else:
                return redirect_to_login(next=request.get_full_path())
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "merchstore/product_create.html"
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context["form"]
        form.fields["owner"].initial = Profile.objects.get(user=self.request.user)
        form.fields["owner"].disabled = True
        context["form"] = form
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "merchstore/product_create.html"
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context["form"]
        form.fields["owner"].initial = Profile.objects.get(user=self.request.user)
        form.fields["owner"].disabled = True
        context["form"] = form
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        product = self.get_object()
        if form.is_valid() and product.stock == 0:
            form.instance.status = "Out of Stock"
        return super().form_valid(form)


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owners"] = Profile.objects.all()
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "merchstore/transaction_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buyers"] = Profile.objects.all()
        return context
