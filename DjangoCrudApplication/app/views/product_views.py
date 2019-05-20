from django.shortcuts import render,redirect,get_object_or_404
from app.forms.product_forms import ProductForm
from app.models.product import Product
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core.files.storage import FileSystemStorage

def product_list(request):
    assert isinstance(request, HttpRequest)
    products = Product.objects.all()
    return render(request,'product/product_list.html',
                  {
                      'title':'Product List',
                      'products' : products,
                      'year':datetime.now().year,
                  })

def create_product(request):
    assert isinstance(request, HttpRequest)
    form = ProductForm(request.POST or None)

    
    if request.method == "POST" and request.FILES.get('product_image'):
        myfile = request.FILES['product_image']
        product_to_be_created = request.POST.copy()
        product_to_be_created.update({'product_image': myfile.name})
        updated_form = ProductForm(data = product_to_be_created)
        if updated_form.is_valid():
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            updated_form.save()
            return redirect('products')

    return render(request,'product/create_product.html',
                  {
                      'form' : form,
                      'title':'Create Product',
                      'year':datetime.now().year,
                  })


def product_details(request,product_id):
    assert isinstance(request, HttpRequest)

    product = get_object_or_404(Product,product_id = product_id)

    return render(request,'product/product_details.html',
                  {
                      'product' : product,
                      'title':'Product Details',
                      'year':datetime.now().year,
                  })

def update_product(request,product_id):
    assert isinstance(request, HttpRequest)
    product = get_object_or_404(Product,product_id = product_id)

    form = ProductForm(request.POST or None, instance = product)

    if request.method == "POST":
        if form.is_valid():
           form.save()
           return redirect('products')

    return render(request,'product/update_product.html',
                  {
                      'form' : form,
                      'title':'Update Product',
                      'year':datetime.now().year,
                  })

def delete_product(request,product_id):
    assert isinstance(request, HttpRequest)
    product = get_object_or_404(Product,product_id = product_id)

    if request.method == "POST":
        product.delete()
        return redirect('products')

    return render(request,'product/delete_product.html',
                  {
                      'product' : product,
                      'title':'Delete Product',
                      'year':datetime.now().year,
                  })
    

