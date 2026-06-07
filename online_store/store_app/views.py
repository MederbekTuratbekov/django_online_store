from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list_url')


class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list_url')


class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list_url')