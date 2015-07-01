# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from product.views import ProductList

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product_list'),
    url(r'^([\w-]+)/$', ProductList.as_view(), name='product_detailt'),
]
