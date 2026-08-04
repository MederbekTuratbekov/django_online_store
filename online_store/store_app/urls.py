from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_url'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail_url'),
    path('create/', ProductCreateView.as_view(), name='product_create_url'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_url'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_url'),
]
