# -*- coding: utf-8 -*-
# author: itimor

from django_filters import rest_framework as filters
from models import ProxyPool

class ProxyFilter(filters.FilterSet):
    class Meta:
        model = ProxyPool
        fields = {
            'ip': ['exact'],
            'scheme': ['exact'],
            'speed': ['gt'],
            'alive': ['exact'],
        }
