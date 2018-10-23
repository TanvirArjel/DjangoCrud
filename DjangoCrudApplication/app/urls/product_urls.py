from django.urls import path
from django.conf.urls import url, include
from app.views import product_views

urlpatterns = [
    url(r'^products$', product_views.product_list, name = 'products'),
    url('product/create-product', product_views.create_product, name = 'create-product'),
    path('product/product_details/<int:product_id>', product_views.product_details, name = 'product_details'),
    path('product/update_product/<int:product_id>', product_views.update_product, name = 'update_product'),
    path('product/delete_product/<int:product_id>', product_views.delete_product, name = 'delete_product')
]
