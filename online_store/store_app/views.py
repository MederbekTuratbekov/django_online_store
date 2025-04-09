from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.reverse import reverse_lazy # башкы бетке кайтканга
from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'list_product_view'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product_detail_view'

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm # ушу класстын формасын колдон
    success_url = reverse_lazy('product_list_url') # тузгондон кийин башкы бетке чыкканга

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list_url')

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list_url')
