
# Create your views here.
from django.views.generic import ListView, DetailView
from product.models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context