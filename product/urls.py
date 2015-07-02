# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from product.views import product_list, product

urlpatterns = [
    url(r'^$', product_list),
    url(r'^(?P<slug>[\w_-]+)/$', product),
]
