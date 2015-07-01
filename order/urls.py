# -*- coding: utf-8 -*-
from django.conf.urls import url

urlpatterns = [
    url(r'^$', "order.views.detail", name='order_detail'),
]
