# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'core.views.home', name='home'),
]
