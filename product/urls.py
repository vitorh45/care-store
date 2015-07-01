# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from product.views import ProductListView, ProductDetailView

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', ProductDetailView.as_view(), name='product_detail'),
]
