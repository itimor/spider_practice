# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import viewsets
from models import ProxyPool
from serializers import ProxySerializer
from filters import ProxyFilter


class ProxyViewSet(viewsets.ModelViewSet):
    queryset = ProxyPool.objects.all()
    serializer_class = ProxySerializer
    filter_class = ProxyFilter
    ordering_fields = ('speed',)