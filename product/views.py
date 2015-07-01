
# Create your views here.
from django.views.generic import ListView, DetailView
from product.models import Product

class ProductList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductDetail(DetailView):
    model = Product