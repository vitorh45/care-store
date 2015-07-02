
# Create your views here.
from django.shortcuts import render_to_response
from product.models import Product, Category


def product_list(request):
    product_list = Product.objects.all()
    product_category = Category.objects.all()
    return render_to_response('product/product_list.html', { 'product_list': product_list, 'product_category': product_category })


def product(request, slug):
    product = Product.objects.get(slug=slug)
    return render_to_response('product/product_detail.html', { 'product': product })
