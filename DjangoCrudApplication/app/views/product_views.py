from django.shortcuts import render,redirect
from app.forms.product_forms import ProductForm
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Product

def product_list(request):
    assert isinstance(request, HttpRequest)
    products = Product.objects.all()
    return render(request,'product/product_list.html',
                  {
                      'products' : products,
                      'title':'Product List'
                  })

def create_product(request):
    assert isinstance(request, HttpRequest)
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
           form.save()
           return redirect('products')

    return render(request,'product/create_product.html',
                  {
                      'form' : form,
                      'title':'Create Product'
                  })


def product_details(request,product_id):
    assert isinstance(request, HttpRequest)
    product = Product.objects.get(product_id = product_id)
    return render(request,'product/product_details.html',
                  {
                      'product' : product,
                      'title':'Product Details'
                  })

def update_product(request,product_id):
    assert isinstance(request, HttpRequest)
    product = Product.objects.get(product_id = product_id)

    form = ProductForm(request.POST or None, instance = product)

    if request.method == "POST":
        if form.is_valid():
           form.save()
           return redirect('products')

    return render(request,'product/update_product.html',
                  {
                      'form' : form,
                      'title':'Update Product'
                  })

def delete_product(request,product_id):
    assert isinstance(request, HttpRequest)
    product = Product.objects.get(product_id = product_id)

    if request.method == "POST":
        product.delete()
        return redirect('products')

    return render(request,'product/delete_product.html',
                  {
                      'product' : product,
                      'title':'Delete Product'
                  })
    

